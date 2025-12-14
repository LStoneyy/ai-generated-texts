import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_1samp, pearsonr, spearmanr, chi2_contingency
import sys
import os
from datetime import datetime
from pathlib import Path

"""
To run:
python -m venv .venv
source .venv/bin/activate  #unix
.venv\Scripts\activate #windows
cd responses
pip install pandas numpy matplotlib seaborn scipy
python ./script.py path_to_your_data.csv
"""

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Global variables
output_file = None
output_dir = None

def print_and_log(text="", console_only=False):
    """Print to console and optionally write to log file"""
    print(text)
    if output_file and not console_only:
        output_file.write(text + "\n")

def create_output_structure(csv_filepath):
    """Create output directory structure based on CSV filename"""
    global output_dir
    
    # Get CSV filename without extension
    csv_name = Path(csv_filepath).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create main output directory
    output_dir = Path(f"analysis_{csv_name}_{timestamp}")
    output_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    subdirs = ['accuracy', 'confidence_time', 'correlations', 'by_text']
    for subdir in subdirs:
        (output_dir / subdir).mkdir(exist_ok=True)
    
    return output_dir

def load_data(filepath):
    """Load and prepare the data"""
    df = pd.read_csv(filepath)
    
    # Add a column for correctness
    df['correct'] = (df['classification'] == df['text__origin']).astype(int)
    
    return df

def export_text_mapping(df):
    """Export text ID to title mapping"""
    text_mapping = df[['text__id', 'text__title']].drop_duplicates().sort_values('text__id')
    
    mapping_file = output_dir / "text_id_mapping.md"
    
    with open(mapping_file, 'w') as f:
        f.write("# Text ID to Title Mapping\n\n")
        f.write("This document maps each Text ID used in the analysis to its full title.\n\n")
        f.write("---\n\n")
        
        for _, row in text_mapping.iterrows():
            f.write(f"**Text {row['text__id']}:** {row['text__title']}\n\n")
    
    print_and_log(f"✓ Text ID mapping saved to: `{mapping_file.name}`\n")
    
    # Also print to console
    print("\n" + "=" * 80)
    print("TEXT ID TO TITLE MAPPING")
    print("=" * 80 + "\n")
    for _, row in text_mapping.iterrows():
        print(f"Text {row['text__id']}: {row['text__title']}")

def descriptive_statistics(df):
    """Calculate and display descriptive statistics"""
    # Participant information
    participants = df.groupby('participant__id').first()
    
    print_and_log(f"**Number of participants:** {len(participants)}\n")
    
    print_and_log("### Participant Demographics\n")
    print_and_log(f"- **Mean teaching experience:** {participants['participant__experience'].mean():.2f} years (SD = {participants['participant__experience'].std():.2f})")
    print_and_log(f"- **Range:** {participants['participant__experience'].min():.0f} - {participants['participant__experience'].max():.0f} years\n")
    
    print_and_log("**Departments represented:**\n")
    dept_counts = participants['participant__department'].value_counts()
    for dept, count in dept_counts.items():
        print_and_log(f"- {dept}: {count}")
    print_and_log("")
    
    # Text information
    print_and_log("### Text Information\n")
    print_and_log(f"- **Total number of texts:** {df['text__id'].nunique()}")
    print_and_log(f"- **AI-generated texts:** {df[df['text__origin'] == 'ai']['text__id'].nunique()}")
    print_and_log(f"- **Human-written texts:** {df[df['text__origin'] == 'human']['text__id'].nunique()}\n")
    
    # Response information
    print_and_log("### Response Information\n")
    print_and_log(f"**Total responses collected:** {len(df)}\n")
    print_and_log("**Classifications:**")
    print_and_log(f"- Classified as AI: {(df['classification'] == 'ai').sum()}")
    print_and_log(f"- Classified as Human: {(df['classification'] == 'human').sum()}\n")
    
    # Confidence ratings
    print_and_log("### Confidence Ratings\n")
    print_and_log(f"- **Mean:** {df['confidence'].mean():.2f} (SD = {df['confidence'].std():.2f})")
    print_and_log(f"- **Median:** {df['confidence'].median():.0f}")
    print_and_log(f"- **Range:** {df['confidence'].min():.0f} - {df['confidence'].max():.0f}\n")
    
    # Response times (convert from ms to seconds)
    df['response_time_sec'] = df['response_time'] / 1000
    print_and_log("### Response Times\n")
    print_and_log(f"- **Mean:** {df['response_time_sec'].mean():.2f} seconds (SD = {df['response_time_sec'].std():.2f})")
    print_and_log(f"- **Median:** {df['response_time_sec'].median():.2f} seconds")
    print_and_log(f"- **Range:** {df['response_time_sec'].min():.2f} - {df['response_time_sec'].max():.2f} seconds\n")

def accuracy_analysis(df):
    """Analyze classification accuracy"""
    # Overall accuracy
    overall_accuracy = df['correct'].mean() * 100
    print_and_log(f"**Overall accuracy:** {overall_accuracy:.2f}%\n")
    
    # Accuracy by participant
    participant_accuracy = df.groupby('participant__id')['correct'].mean() * 100
    print_and_log("### Participant-Level Accuracy\n")
    print_and_log(f"- **Mean:** {participant_accuracy.mean():.2f}% (SD = {participant_accuracy.std():.2f}%)")
    print_and_log(f"- **Range:** {participant_accuracy.min():.2f}% - {participant_accuracy.max():.2f}%\n")
    
    # Accuracy by text origin
    print_and_log("### Accuracy by Text Origin\n")
    for origin in ['ai', 'human']:
        origin_df = df[df['text__origin'] == origin]
        accuracy = origin_df['correct'].mean() * 100
        print_and_log(f"- **{origin.upper()}-generated:** {accuracy:.2f}% ({origin_df['correct'].sum()}/{len(origin_df)} correct)")
    print_and_log("")
    
    # Confusion matrix
    confusion = pd.crosstab(df['text__origin'], df['classification'], margins=True)
    print_and_log("### Confusion Matrix\n")
    print_and_log("| Actual \\ Classified | AI | Human | Total |")
    print_and_log("|---------------------|----:|------:|------:|")
    
    for idx in confusion.index:
        if idx == 'All':
            print_and_log(f"| **Total** | **{confusion.loc[idx, 'ai']}** | **{confusion.loc[idx, 'human']}** | **{confusion.loc[idx, 'All']}** |")
        else:
            print_and_log(f"| **{idx.upper()}** | {confusion.loc[idx, 'ai']} | {confusion.loc[idx, 'human']} | {confusion.loc[idx, 'All']} |")
    print_and_log("")
    
    # Sensitivity and Specificity
    ai_texts = df[df['text__origin'] == 'ai']
    human_texts = df[df['text__origin'] == 'human']
    
    sensitivity = (ai_texts['classification'] == 'ai').mean() * 100
    specificity = (human_texts['classification'] == 'human').mean() * 100
    
    print_and_log("### Diagnostic Measures\n")
    print_and_log(f"- **Sensitivity (True Positive Rate):** {sensitivity:.2f}%")
    print_and_log(f"- **Specificity (True Negative Rate):** {specificity:.2f}%\n")
    
    return participant_accuracy

def hypothesis_testing(df, participant_accuracy):
    """Test hypotheses using statistical tests"""
    print_and_log("### Hypotheses\n")
    print_and_log("- **H₀ (Null Hypothesis):** Accuracy = 50% (chance level)")
    print_and_log("- **H₁ (Alternative Hypothesis):** Accuracy ≠ 50%\n")
    
    # One-sample t-test against chance (50%)
    t_stat, p_value = ttest_1samp(participant_accuracy, 50)
    
    print_and_log("### One-Sample t-Test Results\n")
    print_and_log(f"- **t-statistic:** t({len(participant_accuracy)-1}) = {t_stat:.3f}")
    print_and_log(f"- **p-value:** {p_value:.4f}")
    print_and_log(f"- **Mean accuracy:** {participant_accuracy.mean():.2f}%")
    print_and_log(f"- **95% Confidence Interval:** [{participant_accuracy.mean() - 1.96 * participant_accuracy.sem():.2f}%, "
          f"{participant_accuracy.mean() + 1.96 * participant_accuracy.sem():.2f}%]\n")
    
    print_and_log("### Interpretation\n")
    if p_value < 0.05:
        print_and_log(f"**Result:** REJECT H₀ (p < 0.05)\n")
        if participant_accuracy.mean() > 50:
            print_and_log(f"**Conclusion:** Participants performed significantly **better than chance**.\n")
        else:
            print_and_log(f"**Conclusion:** Participants performed significantly **worse than chance**.\n")
    else:
        print_and_log(f"**Result:** FAIL TO REJECT H₀ (p ≥ 0.05)\n")
        print_and_log(f"**Conclusion:** No significant difference from chance level.\n")
    
    # Effect size (Cohen's d)
    cohens_d = (participant_accuracy.mean() - 50) / participant_accuracy.std()
    if abs(cohens_d) < 0.2:
        effect_interpretation = "negligible"
    elif abs(cohens_d) < 0.5:
        effect_interpretation = "small"
    elif abs(cohens_d) < 0.8:
        effect_interpretation = "medium"
    else:
        effect_interpretation = "large"
    
    print_and_log("### Effect Size\n")
    print_and_log(f"- **Cohen's d:** {cohens_d:.3f}")
    print_and_log(f"- **Interpretation:** {effect_interpretation} effect\n")

def correlation_analysis(df):
    """Analyze correlations between variables"""
    # Aggregate by participant
    participant_data = df.groupby('participant__id').agg({
        'correct': 'mean',
        'confidence': 'mean',
        'response_time': 'mean',
        'participant__experience': 'first'
    })
    participant_data['accuracy'] = participant_data['correct'] * 100
    
    print_and_log("### Participant-Level Correlations\n")
    
    # Accuracy vs. Confidence
    r_conf, p_conf = pearsonr(participant_data['accuracy'], participant_data['confidence'])
    print_and_log("**Accuracy vs. Confidence:**")
    print_and_log(f"- Pearson r = {r_conf:.3f}, p = {p_conf:.4f}\n")
    
    # Accuracy vs. Response Time
    r_time, p_time = pearsonr(participant_data['accuracy'], participant_data['response_time'])
    print_and_log("**Accuracy vs. Response Time:**")
    print_and_log(f"- Pearson r = {r_time:.3f}, p = {p_time:.4f}\n")
    
    # Accuracy vs. Experience
    r_exp, p_exp = pearsonr(participant_data['accuracy'], participant_data['participant__experience'])
    print_and_log("**Accuracy vs. Teaching Experience:**")
    print_and_log(f"- Pearson r = {r_exp:.3f}, p = {p_exp:.4f}\n")
    
    # Confidence vs. Correctness (per response)
    print_and_log("### Response-Level Analysis\n")
    print_and_log("**Confidence by Correctness:**\n")
    
    correct_conf = df[df['correct'] == 1]['confidence'].mean()
    incorrect_conf = df[df['correct'] == 0]['confidence'].mean()
    correct_sd = df[df['correct'] == 1]['confidence'].std()
    incorrect_sd = df[df['correct'] == 0]['confidence'].std()
    
    print_and_log(f"- **Correct responses:** M = {correct_conf:.2f} (SD = {correct_sd:.2f})")
    print_and_log(f"- **Incorrect responses:** M = {incorrect_conf:.2f} (SD = {incorrect_sd:.2f})\n")
    
    t_stat, p_value = stats.ttest_ind(df[df['correct'] == 1]['confidence'], 
                                       df[df['correct'] == 0]['confidence'])
    print_and_log(f"**Independent t-test:** t = {t_stat:.3f}, p = {p_value:.4f}\n")

def text_difficulty_analysis(df):
    """Analyze which texts were most difficult to classify"""
    # Use only text ID, not title
    text_stats = df.groupby(['text__id', 'text__origin']).agg({
        'correct': 'mean',
        'confidence': 'mean',
        'response_time': 'mean'
    }).round(2)
    text_stats['accuracy'] = (text_stats['correct'] * 100).round(1)
    text_stats = text_stats.sort_values('accuracy')
    
    print_and_log("Texts ranked by difficulty (lowest accuracy first):\n")
    print_and_log("| Text ID | Origin | Accuracy (%) | Confidence | Response Time (ms) |")
    print_and_log("|--------:|:-------|-------------:|-----------:|-------------------:|")
    
    for (text_id, origin), row in text_stats.iterrows():
        print_and_log(f"| {text_id} | {origin.upper()} | {row['accuracy']:.1f} | {row['confidence']:.2f} | {row['response_time']:.0f} |")
    print_and_log("")

def create_visualizations(df, participant_accuracy):
    """Create all necessary visualizations"""
    print_and_log("Generating visualizations...\n")
    
    # 1. Accuracy visualizations
    # Histogram of participant accuracy
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(participant_accuracy, bins=10, edgecolor='black', alpha=0.7)
    ax.axvline(50, color='red', linestyle='--', label='Chance level (50%)')
    ax.axvline(participant_accuracy.mean(), color='green', linestyle='-', 
               label=f'Mean ({participant_accuracy.mean():.1f}%)')
    ax.set_xlabel('Accuracy (%)')
    ax.set_ylabel('Number of Participants')
    ax.set_title('Distribution of Participant Accuracy')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'accuracy' / 'histogram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `accuracy/histogram.png`")
    
    # Box plot of accuracy
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot([participant_accuracy], labels=['Participants'])
    ax.axhline(50, color='red', linestyle='--', label='Chance level')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Accuracy Distribution (Box Plot)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'accuracy' / 'boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `accuracy/boxplot.png`")
    
    # Accuracy by text origin
    fig, ax = plt.subplots(figsize=(8, 6))
    origin_accuracy = df.groupby('text__origin')['correct'].mean() * 100
    ax.bar(['AI-generated', 'Human-written'], 
           [origin_accuracy['ai'], origin_accuracy['human']], 
           color=['#e74c3c', '#3498db'], alpha=0.7, edgecolor='black')
    ax.axhline(50, color='red', linestyle='--', label='Chance level')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Accuracy by Text Origin')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(output_dir / 'accuracy' / 'by_origin.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `accuracy/by_origin.png`")
    
    # Confusion matrix heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    confusion = pd.crosstab(df['text__origin'], df['classification'])
    sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['AI', 'Human'], yticklabels=['AI', 'Human'])
    ax.set_xlabel('Classified as')
    ax.set_ylabel('Actual origin')
    ax.set_title('Confusion Matrix')
    plt.tight_layout()
    plt.savefig(output_dir / 'accuracy' / 'confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `accuracy/confusion_matrix.png`")
    
    # 2. Confidence and Response Time visualizations
    # Confidence distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['confidence'], bins=5, edgecolor='black', alpha=0.7, range=(0.5, 5.5))
    ax.set_xlabel('Confidence Rating')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Confidence Ratings')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(output_dir / 'confidence_time' / 'confidence_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `confidence_time/confidence_distribution.png`")
    
    # Confidence by correctness
    fig, ax = plt.subplots(figsize=(8, 6))
    correct_conf = df[df['correct'] == 1]['confidence']
    incorrect_conf = df[df['correct'] == 0]['confidence']
    ax.boxplot([correct_conf, incorrect_conf], labels=['Correct', 'Incorrect'])
    ax.set_ylabel('Confidence Rating')
    ax.set_title('Confidence by Response Correctness')
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(output_dir / 'confidence_time' / 'confidence_by_correctness.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `confidence_time/confidence_by_correctness.png`")
    
    # Response time distribution (in seconds)
    df['response_time_sec'] = df['response_time'] / 1000
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['response_time_sec'], bins=20, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Response Time (seconds)')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Response Times')
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(output_dir / 'confidence_time' / 'response_time_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `confidence_time/response_time_distribution.png`")
    
    # Response time by correctness
    fig, ax = plt.subplots(figsize=(8, 6))
    correct_time = df[df['correct'] == 1]['response_time_sec']
    incorrect_time = df[df['correct'] == 0]['response_time_sec']
    ax.boxplot([correct_time, incorrect_time], labels=['Correct', 'Incorrect'])
    ax.set_ylabel('Response Time (seconds)')
    ax.set_title('Response Time by Correctness')
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(output_dir / 'confidence_time' / 'response_time_by_correctness.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `confidence_time/response_time_by_correctness.png`")
    
    # 3. Correlation visualizations
    participant_data = df.groupby('participant__id').agg({
        'correct': 'mean',
        'participant__experience': 'first',
        'confidence': 'mean'
    })
    participant_data['accuracy'] = participant_data['correct'] * 100
    
    # Experience vs Accuracy
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(participant_data['participant__experience'], 
               participant_data['accuracy'], s=100, alpha=0.6)
    ax.axhline(50, color='red', linestyle='--', label='Chance level')
    
    # Add trend line
    z = np.polyfit(participant_data['participant__experience'], 
                   participant_data['accuracy'], 1)
    p = np.poly1d(z)
    ax.plot(participant_data['participant__experience'], 
            p(participant_data['participant__experience']), 
            "r--", alpha=0.5, label='Trend line')
    
    ax.set_xlabel('Teaching Experience (years)')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Teaching Experience vs. Accuracy')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'correlations' / 'experience_vs_accuracy.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `correlations/experience_vs_accuracy.png`")
    
    # Confidence vs Accuracy
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(participant_data['confidence'], 
               participant_data['accuracy'], s=100, alpha=0.6)
    ax.axhline(50, color='red', linestyle='--', label='Chance level')
    ax.set_xlabel('Mean Confidence Rating')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Confidence vs. Accuracy')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'correlations' / 'confidence_vs_accuracy.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `correlations/confidence_vs_accuracy.png`")
    
    # 4. Text-level analysis (using text ID only)
    fig, ax = plt.subplots(figsize=(12, 8))
    
    text_stats = df.groupby(['text__id', 'text__origin']).agg({
        'correct': 'mean'
    })
    text_stats['accuracy'] = text_stats['correct'] * 100
    text_stats = text_stats.sort_values('accuracy')
    
    colors = ['#e74c3c' if origin == 'ai' else '#3498db' 
              for origin in text_stats.index.get_level_values('text__origin')]
    
    bars = ax.barh(range(len(text_stats)), text_stats['accuracy'], 
                   color=colors, alpha=0.7, edgecolor='black')
    ax.axvline(50, color='red', linestyle='--', label='Chance level')
    ax.set_yticks(range(len(text_stats)))
    # Use text ID instead of title
    ax.set_yticklabels([f"Text {text_id}" 
                        for text_id in text_stats.index.get_level_values('text__id')])
    ax.set_xlabel('Accuracy (%)')
    ax.set_title('Classification Accuracy by Text')
    
    # Custom legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#e74c3c', alpha=0.7, label='AI-generated'),
                       Patch(facecolor='#3498db', alpha=0.7, label='Human-written'),
                       plt.Line2D([0], [0], color='red', linestyle='--', label='Chance level')]
    ax.legend(handles=legend_elements, loc='lower right')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'by_text' / 'accuracy_by_text.png', dpi=300, bbox_inches='tight')
    plt.close()
    print_and_log("- ✓ `by_text/accuracy_by_text.png`\n")

def main():
    """Main analysis function"""
    global output_file, output_dir
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Create output directory structure
    output_dir = create_output_structure(filepath)
    
    # Create output log file (now in markdown)
    log_filename = output_dir / "analysis_results.md"
    
    with open(log_filename, 'w') as output_file:
        print_and_log("# AI Text Detection Study - Statistical Analysis\n")
        print_and_log(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ")
        print_and_log(f"**Data Source:** `{filepath}`\n")
        print_and_log("---\n")
        
        # Load data
        df = load_data(filepath)
        
        # Export text ID mapping
        export_text_mapping(df)
        
        # Run analyses
        print_and_log("## 1. Descriptive Statistics\n")
        descriptive_statistics(df)
        
        print_and_log("---\n")
        print_and_log("## 2. Accuracy Analysis\n")
        participant_accuracy = accuracy_analysis(df)
        
        print_and_log("---\n")
        print_and_log("## 3. Hypothesis Testing\n")
        hypothesis_testing(df, participant_accuracy)
        
        print_and_log("---\n")
        print_and_log("## 4. Correlation Analysis\n")
        correlation_analysis(df)
        
        print_and_log("---\n")
        print_and_log("## 5. Text Difficulty Analysis\n")
        text_difficulty_analysis(df)
        
        print_and_log("---\n")
        print_and_log("## 6. Visualizations\n")
        create_visualizations(df, participant_accuracy)
        
        print_and_log("---\n")
        print_and_log("## Summary\n")
        print_and_log(f"Analysis complete! All results have been saved to: `{output_dir.name}`\n")
        print_and_log("### Generated Files\n")
        print_and_log("**Reports:**")
        print_and_log("- `analysis_results.md` - This comprehensive analysis report")
        print_and_log("- `text_id_mapping.md` - Reference guide mapping text IDs to titles\n")
        print_and_log("**Visualizations:**")
        print_and_log("- `accuracy/` - Accuracy distribution and performance metrics")
        print_and_log("- `confidence_time/` - Confidence and response time analyses")
        print_and_log("- `correlations/` - Relationship analyses between variables")
        print_and_log("- `by_text/` - Item-level difficulty analysis\n")
    
    print(f"\n{'='*80}")
    print(f"Analysis complete! Results saved to: {output_dir}")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()