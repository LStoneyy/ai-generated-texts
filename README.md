# ai-generated-texts

An empirical research project investigating the ability of university instructors to distinguish between AI-generated and human-written student essays.

## Research Question

**"Do university instructors spot AI?"** – This study examines to what extent university instructors can differentiate between AI-generated texts and authentic student writing from BA/MA students at RWTH Aachen University.

## Hypotheses

- **H₀ (Null Hypothesis):** University instructors cannot distinguish between AI-generated and human-written student essays better than chance (mean accuracy = 50%)
- **H₁ (Alternative Hypothesis):** University instructors can distinguish between AI-generated and human-written student essays at a rate different from chance (mean accuracy ≠ 50%)

## Methodology

### Data Collection

- **Sample:** 10 texts total (5 AI-generated, 5 human-written)  
- **Source:** BA student essays from RWTH Aachen University  
- **Presentation:** Randomized order for each participant  
- **Data collected:**
  - Participant demographics: Name, years of teaching experience, Department
  - Binary classification per text (AI vs. Human)
  - Confidence rating (1-5 Likert scale)
  - Response time per text (in milliseconds)

### Statistical Analysis

The project includes a comprehensive statistical analysis pipeline (`responses/script.py`) that performs:

- **Descriptive Statistics:** Participant demographics, response patterns, confidence ratings, and response times
- **Accuracy Analysis:** Overall accuracy, participant-level accuracy, accuracy by text origin, confusion matrix, sensitivity/specificity
- **Hypothesis Testing:** One-sample t-test against chance level (50%), effect size calculation (Cohen's d), 95% confidence intervals
- **Correlation Analysis:** Relationships between accuracy, confidence, response time, and teaching experience
- **Text Difficulty Analysis:** Item-level analysis identifying which texts were most/least difficult to classify

#### Running the Analysis

```bash
cd responses
python -m venv .venv
source .venv/bin/activate  # Unix/macOS
# .venv\Scripts\activate    # Windows

pip install pandas numpy matplotlib seaborn scipy
python script.py script.csv
```

The script generates:
- **Markdown Reports:**
  - `analysis_results.md` - Comprehensive statistical analysis with formatted tables and results
  - `text_id_mapping.md` - Reference mapping text IDs to full titles
- **Visualizations:** 
  - Accuracy distributions and performance metrics
  - Confidence and response time analyses
  - Correlation plots
  - Item-level difficulty analysis

## Project Structure

```
ai-generated-texts/
├── responses/
│   ├── script.py                    # Statistical analysis pipeline
│   └── analysis_*/                  # Generated analysis outputs
├── static/                          # CSS, JavaScript, images
├── config/                          # Configuration and base app
├── study/                           # study app
├── docker-compose.dev.yml           # Docker development configuration
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Tech Stack

- **Backend:** Django 5.0+  
- **Database:** SQLite3 (Django included) 
- **Frontend:** Vanilla CSS, Vanilla JavaScript  
- **Analysis:** Python (pandas, numpy, matplotlib, seaborn, scipy)
- **Deployment:** PythonAnywhere (venv name: "venv")

## Local Development

### Using Docker

```bash
git clone https://github.com/LStoneyy/ai-generated-texts.git
cd ai-generated-texts/
docker-compose -f docker-compose.dev.yml up --build
```

Access at `http://localhost:8000`

### Manual Setup

```bash
git clone https://github.com/LStoneyy/ai-generated-texts.git
cd ai-generated-texts/
python -m venv venv
source venv/bin/activate  # Unix/macOS
# venv\Scripts\activate    # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Access at `http://127.0.0.1:8000`

## Documentation

For detailed information about the statistical methods and formulas used in the analysis, see:
- `responses/statistics.md` - Complete analytical framework with formulas and LaTeX code

## License

MIT

## Contact

Lukas Schaffrath  
lukas.schaffrath2@rwth-aachen.de


