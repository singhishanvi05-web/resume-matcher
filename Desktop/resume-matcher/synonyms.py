SKILL_SYNONYMS = {
    "machine learning": ["ml", "machine-learning"],
    "natural language processing": ["nlp", "text mining"],
    "kubernetes": ["k8s"],
    "javascript": ["js"],
    "python": ["py"],
    "postgresql": ["postgres", "psql"],
    "amazon web services": ["aws"],
    "continuous integration": ["ci/cd", "cicd"],
    "deep learning": ["dl", "neural networks"],
}

def normalize_skill(skill):
    skill = skill.lower().strip()
    for canonical, aliases in SKILL_SYNONYMS.items():
        if skill == canonical or skill in aliases:
            return canonical
    return skill