# Resume Matcher

An NLP-powered tool that matches your resume against a job description.

## Features
- Tokenization + stopword removal
- Named Entity Recognition with spaCy
- TF-IDF keyword extraction
- Synonym handling (ML = Machine Learning)
- Match score with visual breakdown
- Flask web interface

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Run
```bash
python app.py
```
Then open http://127.0.0.1:5000 in your browser.

## Tech Stack
Python · Flask · spaCy · NLTK · scikit-learn · Matplotlib
