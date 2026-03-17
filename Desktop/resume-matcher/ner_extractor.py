import spacy
from synonyms import normalize_skill

nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = {
    "python", "sql", "java", "react", "docker", "aws", "ml",
    "machine learning", "pandas", "flask", "kubernetes", "git",
    "nlp", "deep learning", "postgresql", "mongodb", "tensorflow",
    "pytorch", "scikit-learn", "fastapi", "redis", "kafka", "spark"
}

def extract_skills(text):
    doc = nlp(text)
    found = set()

    for ent in doc.ents:
        if ent.label_ in ("ORG", "PRODUCT"):
            found.add(ent.text.lower())

    text_lower = text.lower()
    for skill in SKILL_KEYWORDS:
        if skill in text_lower:
            found.add(skill)

    return {normalize_skill(s) for s in found}