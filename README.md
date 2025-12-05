# ai-generated-texts

An empirical research project investigating the ability of university instructors to distinguish between AI-generated and human-written student essays.

## Research Question

**"Do university instructors spot AI?"** – This study examines to what extent university instructors can differentiate between AI-generated texts and authentic student writing from BA/MA students at RWTH Aachen University.

## Hypotheses

- **H0:** University instructors cannot distinguish between AI-generated and human-written student essays better than chance (accuracy ≠ 50%)
- **H1:** University instructors can distinguish between AI-generated and human-written student essays better than chance (accuracy > 50%)

## Methodology

- **Sample:** 10 texts total (5 AI-generated, 5 human-written)  
- **Source:** BA student essays from RWTH Aachen University  
- **Presentation:** Randomized order for each participant  
- **Data collected:**
  - Participant demographics: Name, years of teaching experience, Department
  - Binary classification per text (AI vs. Human)
  - Confidence rating (1-5 Likert scale)
  - Response time per text

## Tech Stack

- **Backend:** Django 5.0+  
- **Database:** SQLite3  
- **Frontend:** Vanilla CSS, Vanilla JavaScript  
- **Deployment:** PythonAnywhere (venv name: "venv")

## Local Development

```bash
git clone https://github.com/LStoneyy/ai-generated-texts.git
cd ai-generated-texts/
docker-compose -f docker-compose.dev.yml up --build
```

Access at `http://localhost:8000`

## License

MIT

## Contact

Lukas Schaffrath  
lukas.schaffrath2@rwth-aachen.de


