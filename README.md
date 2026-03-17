# Resume Matcher

**NLP-powered resume analysis tool that matches your skills to any job description.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=flat-square)
![spaCy](https://img.shields.io/badge/spaCy-3.x-09a3d5?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF-orange?style=flat-square)

</div>

---

## Overview

Resume Matcher is a full-stack NLP application that takes your resume and a job description, runs them through a complete NLP pipeline, and returns a match score with detailed skill breakdown — matched skills, missing skills, bonus skills, and top JD keywords.

---

## NLP Pipeline
Raw Text → Tokenization → Stopword Removal → NER → TF-IDF → Synonym Normalization → Skill Match

---

## Features

- Match score percentage based on resume vs job description
- Matched skills — skills you have that the job wants
- Missing skills — gaps to address before applying
- Bonus skills — extra skills you have beyond requirements
- Synonym handling — ML = Machine Learning, k8s = Kubernetes
- Dark themed Flask web interface with animated pipeline steps

---

## Tech Stack

| Layer | Technology |
|---|---|
| NLP | spaCy, NLTK |
| Keyword Extraction | scikit-learn TF-IDF |
| Backend | Python 3, Flask |
| Frontend | HTML, CSS, JavaScript |
| Visualization | Matplotlib |

---

## Project Structure
resume-matcher/
├── app.py                  # Flask server and API routes
├── matcher.py              # Core skill matching logic
├── ner_extractor.py        # spaCy Named Entity Recognition
├── keyword_extractor.py    # TF-IDF keyword extraction
├── synonyms.py             # Skill synonym normalization
├── preprocessor.py         # Tokenization and stopword removal
├── visualizer.py           # Matplotlib chart generation
├── templates/
│   └── index.html          # Frontend web interface
└── requirements.txt

---

## Getting Started
```bash
# 1. Clone the repository
git clone https://github.com/singhishanvi05-web/resume-matcher.git
cd resume-matcher

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download spaCy model
python -m spacy download en_core_web_sm

# 5. Run the app
python app.py
```

Open http://127.0.0.1:5000 in your browser.

---

## How to Use

1. Paste your resume text in the left panel
2. Paste the job description in the right panel
3. Click Analyze Match
4. Watch the NLP pipeline run step by step
5. Review your match score and skill breakdown

---

## What I Learned

- Building an end-to-end NLP pipeline from scratch
- Using spaCy for Named Entity Recognition on domain-specific text
- Applying TF-IDF to rank keywords by relevance
- Handling synonyms and abbreviations in real-world text
- Connecting a Python NLP backend to a Flask web interface
