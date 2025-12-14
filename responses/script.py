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

def print_and_log(text=""):
    """Print to console and write to log file"""
    print(text)
    if output_file:
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
    
    mapping_file = output_dir / "text_id_mapping.txt"
    
    with open(mapping_file, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("TEXT ID TO TITLE MAPPING\n")
        f.write("=" * 80 + "\n\n")
        
        for _, row in text_mapping.iterrows():
            f.write(f"Text {row['text__id']}: {row['text__title']}\n")
    
    print_and_log(f"\n✓ Text ID mapping saved to: {mapping_file}")
    
    # Also print to console
    print("\n" + "=" * 80)
    print("TEXT ID TO TITLE MAPPING")
    print("=" * 80 + "\n")
    for _, row in text_mapping.iterrows():
        print(f"Text {row['text__id']}: {row['text__title']}")

def descriptive_statistics(df):
    """Calculate and display descriptive statistics"""
    print_and_log("=" * 80)
    print_and_log("DESCRIPTIVE STATISTICS")
    print_and_log("=" * 80)
    
    # Participant information
    participants = df.groupby('participant__id').first()
    print_and_log(f"\nNumber of participants: {len(participants)}")
    print_and_log(f"\nParticipant demographics:")
    print_and_log(f"  Mean teaching experience: {participants['participant__experience'].mean():.2f} years (SD={participants['participant__experience'].std():.2f})")
    print_and_log(f"  Range: {participants['participant__experience'].min():.0f} - {participants['participant__experience'].max():.0f} years")
    print_and_log(f"\nDepartments represented:")
    print_and_log(participants['participant__department'].value_counts().to_string())
    
    # Text information
    print_and_log(f"\nTotal number of texts: {df['text__id'].nunique()}")
    print_and_log(f"AI-generated texts: {df[df['text__origin'] == 'ai']['text__id'].nunique()}")
    print_and_log(f"Human-written texts: {df[df['text__origin'] == 'human']['text__id'].nunique()}")
    
    # Response information
    print_and_log(f"\nTotal responses collected: {len(df)}")
    print_and_log(f"\nClassifications:")
    print_and_log(f"  Classified as AI: {(df['classification'] == 'ai').sum()}")
    print_and_log(f"  Classified as Human: {(df['classification'] == 'human').sum()}")
    
    # Confidence ratings
    print_and_log(f"\nConfidence ratings:")
    print_and_log(f"  Mean: {df['confidence'].mean():.2f} (SD={df['confidence'].std():.2f})")
    print_and_log(f"  Median: {df['confidence'].median():.0f}")
    print_and_log(f"  Range: {df['confidence'].min():.0f} - {df['confidence'].max():.0f}")
    
    # Response times (convert from ms to seconds)
    df['response_time_sec'] = df['response_time'] / 1000
    print_and_log(f"\nResponse times:")
    print_and_log(f"  Mean: {df['response_time_sec'].mean():.2f} seconds (SD={df['response_time_sec'].std():.2f})")
    print_and_log(f"  Median: {df['response_time_sec'].median():.2f} seconds")
    print_and_log(f"  Range: {df['response_time_sec'].min():.2f} - {df['response_time_sec'].max():.2f} seconds")

def accuracy_analysis(df):
    """Analyze classification accuracy"""
    print_and_log("\n" + "=" * 80)
    print_and_log("ACCURACY ANALYSIS")
    print_and_log("=" * 80)
    
    # Overall accuracy
    overall_accuracy = df['correct'].mean() * 100
    print_and_log(f"\nOverall accuracy: {overall_accuracy:.2f}%")
    
    # Accuracy by participant
    participant_accuracy = df.groupby('participant__id')['correct'].mean() * 100
    print_and_log(f"\nAccuracy by participant:")
    print_and_log(f"  Mean: {participant_accuracy.mean():.2f}% (SD={participant_accuracy.std():.2f}%)")
    print_and_log(f"  Range: {participant_accuracy.min():.2f}% - {participant_accuracy.max():.2f}%")
    
    # Accuracy by text origin
    print_and_log(f"\nAccuracy by text origin:")
    for origin in ['ai', 'human']:
        origin_df = df[df['text__origin'] == origin]
        accuracy = origin_df['correct'].mean() * 100
        print_and_log(f"  {origin.upper()}-generated: {accuracy:.2f}% ({origin_df['correct'].sum()}/{len(origin_df)})")
    
    # Confusion matrix
    confusion = pd.crosstab(df['text__origin'], df['classification'], margins=True)
    print_and_log(f"\nConfusion Matrix:")
    print_and_log(confusion.to_string())
    
    # Sensitivity and Specificity
    ai_texts = df[df['text__origin'] == 'ai']
    human_texts = df[df['text__origin'] == 'human']
    
    # Sensitivity: correctly identified AI texts
    sensitivity = (ai_texts['classification'] == 'ai').mean() * 100
    # Specificity: correctly identified human texts
    specificity = (human_texts['classification'] == 'human').mean() * 100
    
    print_and_log(f"\nDiagnostic measures:")
    print_and_log(f"  Sensitivity (True Positive Rate): {sensitivity:.2f}%")
    print_and_log(f"  Specificity (True Negative Rate): {specificity:.2f}%")
    
    return participant_accuracy

def hypothesis_testing(df, participant_accuracy):
    """Test hypotheses using statistical tests"""
    print_and_log("\n" + "=" * 80)
    print_and_log("HYPOTHESIS TESTING")
    print_and_log("=" * 80)
    
    # One-sample t-test against chance (50%)
    print_and_log("\nH0: Accuracy = 50% (chance level)")
    print_and_log("H1: Accuracy ≠ 50%")
    
    t_stat, p_value = ttest_1samp(participant_accuracy, 50)
    
    print_and_log(f"\nOne-sample t-test:")
    print_and_log(f"  t({len(participant_accuracy)-1}) = {t_stat:.3f}")
    print_and_log(f"  p-value = {p_value:.4f}")
    print_and_log(f"  Mean accuracy: {participant_accuracy.mean():.2f}%")
    print_and_log(f"  95% CI: [{participant_accuracy.mean() - 1.96 * participant_accuracy.sem():.2f}%, "
          f"{participant_accuracy.mean() + 1.96 * participant_accuracy.sem():.2f}%]")
    
    if p_value < 0.05:
        print_and_log(f"\n  Result: REJECT H0 (p < 0.05)")
        if participant_accuracy.mean() > 50:
            print_and_log(f"  Conclusion: Participants performed significantly BETTER than chance.")
        else:
            print_and_log(f"  Conclusion: Participants performed significantly WORSE than chance.")
    else:
        print_and_log(f"\n  Result: FAIL TO REJECT H0 (p ≥ 0.05)")
        print_and_log(f"  Conclusion: No significant difference from chance level.")
    
    # Effect size (Cohen's d)
    cohens_d = (participant_accuracy.mean() - 50) / participant_accuracy.std()
    print_and_log(f"\n  Effect size (Cohen's d): {cohens_d:.3f}")
    if abs(cohens_d) < 0.2:
        effect_interpretation = "negligible"
    elif abs(cohens_d) < 0.5:
        effect_interpretation = "small"
    elif abs(cohens_d) < 0.8:
        effect_interpretation = "medium"
    else:
        effect_interpretation = "large"
    print_and_log(f"  Interpretation: {effect_interpretation} effect")

def correlation_analysis(df):
    """Analyze correlations between variables"""
    print_and_log("\n" + "=" * 80)
    print_and_log("CORRELATION ANALYSIS")
    print_and_log("=" * 80)
    
    # Aggregate by participant
    participant_data = df.groupby('participant__id').agg({
        'correct': 'mean',
        'confidence': 'mean',
        'response_time': 'mean',
        'participant__experience': 'first'
    })
    participant_data['accuracy'] = participant_data['correct'] * 100
    
    # Accuracy vs. Confidence
    r_conf, p_conf = pearsonr(participant_data['accuracy'], participant_data['confidence'])
    print_and_log(f"\nAccuracy vs. Confidence:")
    print_and_log(f"  Pearson r = {r_conf:.3f}, p = {p_conf:.4f}")
    
    # Accuracy vs. Response Time
    r_time, p_time = pearsonr(participant_data['accuracy'], participant_data['response_time'])
    print_and_log(f"\nAccuracy vs. Response Time:")
    print_and_log(f"  Pearson r = {r_time:.3f}, p = {p_time:.4f}")
    
    # Accuracy vs. Experience
    r_exp, p_exp = pearsonr(participant_data['accuracy'], participant_data['participant__experience'])
    print_and_log(f"\nAccuracy vs. Teaching Experience:")
    print_and_log(f"  Pearson r = {r_exp:.3f}, p = {p_exp:.4f}")
    
    # Confidence vs. Correctness (per response)
    print_and_log(f"\nConfidence by correctness:")
    correct_conf = df[df['correct'] == 1]['confidence'].mean()
    incorrect_conf = df[df['correct'] == 0]['confidence'].mean()
    print_and_log(f"  Correct responses: M = {correct_conf:.2f} (SD = {df[df['correct'] == 1]['confidence'].std():.2f})")
    print_and_log(f"  Incorrect responses: M = {incorrect_conf:.2f} (SD = {df[df['correct'] == 0]['confidence'].std():.2f})")
    
    t_stat, p_value = stats.ttest_ind(df[df['correct'] == 1]['confidence'], 
                                       df[df['correct'] == 0]['confidence'])
    print_and_log(f"  t-test: t = {t_stat:.3f}, p = {p_value:.4f}")

def text_difficulty_analysis(df):
    """Analyze which texts were most difficult to classify"""
    print_and_log("\n" + "=" * 80)
    print_and_log("TEXT DIFFICULTY ANALYSIS")
    print_and_log("=" * 80)
    
    # Use only text ID, not title
    text_stats = df.groupby(['text__id', 'text__origin']).agg({
        'correct': 'mean',
        'confidence': 'mean',
        'response_time': 'mean'
    }).round(2)
    text_stats['accuracy'] = (text_stats['correct'] * 100).round(1)
    text_stats = text_stats.sort_values('accuracy')
    
    print_and_log("\nTexts ranked by difficulty (lowest accuracy first):")
    print_and_log("\n" + text_stats[['accuracy', 'confidence', 'response_time']].to_string())

def create_visualizations(df, participant_accuracy):
    """Create all necessary visualizations"""
    print_and_log("\n" + "=" * 80)
    print_and_log("GENERATING VISUALIZATIONS")
    print_and_log("=" * 80)
    
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
    print_and_log("✓ Saved: accuracy/histogram.png")
    
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
    print_and_log("✓ Saved: accuracy/boxplot.png")
    
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
    print_and_log("✓ Saved: accuracy/by_origin.png")
    
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
    print_and_log("✓ Saved: accuracy/confusion_matrix.png")
    
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
    print_and_log("✓ Saved: confidence_time/confidence_distribution.png")
    
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
    print_and_log("✓ Saved: confidence_time/confidence_by_correctness.png")
    
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
    print_and_log("✓ Saved: confidence_time/response_time_distribution.png")
    
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
    print_and_log("✓ Saved: confidence_time/response_time_by_correctness.png")
    
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
    print_and_log("✓ Saved: correlations/experience_vs_accuracy.png")
    
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
    print_and_log("✓ Saved: correlations/confidence_vs_accuracy.png")
    
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
    print_and_log("✓ Saved: by_text/accuracy_by_text.png")

def main():
    """Main analysis function"""
    global output_file, output_dir
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Create output directory structure
    output_dir = create_output_structure(filepath)
    
    # Create output log file
    log_filename = output_dir / "analysis_results.txt"
    
    with open(log_filename, 'w') as output_file:
        print_and_log("\n" + "=" * 80)
        print_and_log("AI TEXT DETECTION STUDY - STATISTICAL ANALYSIS")
        print_and_log("=" * 80)
        print_and_log(f"\nAnalysis date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print_and_log(f"Loading data from: {filepath}\n")
        
        # Load data
        df = load_data(filepath)
        
        # Export text ID mapping
        export_text_mapping(df)
        
        # Run analyses
        descriptive_statistics(df)
        participant_accuracy = accuracy_analysis(df)
        hypothesis_testing(df, participant_accuracy)
        correlation_analysis(df)
        text_difficulty_analysis(df)
        create_visualizations(df, participant_accuracy)
        
        print_and_log("\n" + "=" * 80)
        print_and_log("ANALYSIS COMPLETE")
        print_and_log("=" * 80)
        print_and_log(f"\nAll results saved to: {output_dir}")
        print_and_log("\nGenerated structure:")
        print_and_log("  analysis_results.txt")
        print_and_log("  text_id_mapping.txt")
        print_and_log("  accuracy/")
        print_and_log("    - histogram.png")
        print_and_log("    - boxplot.png")
        print_and_log("    - by_origin.png")
        print_and_log("    - confusion_matrix.png")
        print_and_log("  confidence_time/")
        print_and_log("    - confidence_distribution.png")
        print_and_log("    - confidence_by_correctness.png")
        print_and_log("    - response_time_distribution.png")
        print_and_log("    - response_time_by_correctness.png")
        print_and_log("  correlations/")
        print_and_log("    - experience_vs_accuracy.png")
        print_and_log("    - confidence_vs_accuracy.png")
        print_and_log("  by_text/")
        print_and_log("    - accuracy_by_text.png")
        print_and_log("\n")
    
    print(f"\nAll results saved to: {output_dir}")

if __name__ == "__main__":
    main()