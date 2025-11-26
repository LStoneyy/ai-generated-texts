
# ai-generated-texts

An empirical research project investigating the ability of university instructors to distinguish between AI-generated and human-written student essays in higher education, presented via a modern, minimalist, Gruvbox Dark-themed web interface.

## Research Question

**"Do university instructors spot AI?"** – This study examines to what extent university instructors can differentiate between AI-generated texts and authentic student writing from BA/MA students at RWTH Aachen University.

## Hypotheses

- **H0:** University instructors cannot distinguish between AI-generated and human-written student essays better than chance (accuracy ≠ 50%)
- **H1:** University instructors can distinguish between AI-generated and human-written student essays better than chance (accuracy > 50%)

## Methodology

- **Sample:** 10 texts total (5 AI-generated, 5 human-written)  
- **Source:** BA/MA student essays from RWTH Aachen University  
- **Presentation:** Randomized order for each participant  
- **Data collected:**
  - Participant demographics: Name, years of teaching experience, Department
  - Binary classification per text (AI vs. Human)
  - Confidence rating (1-5 Likert scale)
  - Response time per text

## Tech Stack

- **Backend:** Django 5.0+  
- **Database:** SQLite3  
- **Frontend:** Vanilla CSS (Gruvbox Dark theme), Clash Display (Headings), Epilogue (Body), Vanilla JavaScript  
- **Deployment:** Docker + Docker Compose + Nginx + Gunicorn  
- **VPS:** IONOS

## Project Structure
```
ai_detection_study/
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── Dockerfile
├── requirements.txt
├── manage.py
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── study/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│   └── templates/study/
├── static/
│   ├── css/
│   │   ├── base.css
│   │   ├── forms.css
│   │   ├── header.css
│   └── js/
└── nginx/
```

## Setup & Development

### Local Development
```bash
# Clone repository
git clone <repository-url>
cd ai_detection_study

# Start development server with livereload
docker-compose -f docker-compose.dev.yml up --build

# First-time setup
docker-compose -f docker-compose.dev.yml exec web python manage.py makemigrations
docker-compose -f docker-compose.dev.yml exec web python manage.py migrate
docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

# Access at http://localhost:8000
```

### Production Deployment (VPS)
```bash
# On VPS
git clone <repository-url>
cd ai_detection_study

# Build and start production stack
docker-compose -f docker-compose.prod.yml up -d --build

# Run migrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate

# Collect static files
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

## Branch Strategy

- `main` → Local development  
- `vps` → Production deployment on VPS

## Data Analysis

Collected data will be analyzed using:

- Accuracy calculation: `(correct classifications / total) × 100`  
- One-sample t-test (mean accuracy vs. 50% chance level)  
- Correlation/regression analysis for confidence ratings and response times

## Research Context

This project is inspired by the study:

> Fleckenstein, J., Meyer, J., Jansen, T., Keller, S. D., Köller, O., & Möller, J. (2024). Do teachers spot AI? Evaluating the detectability of AI-generated texts among student essays. *Computers and Education: Artificial Intelligence*, 6, 100209.

The original study focused on K-12 teachers; this replication extends the investigation to the university context.

## License
MIT, see LICENSE

## Contact
Lukas Schaffrath
lukas.schaffrath2@rwth-aachen.de


