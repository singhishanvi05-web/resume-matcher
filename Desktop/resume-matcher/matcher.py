from ner_extractor import extract_skills
from keyword_extractor import extract_keywords

def match(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills     = extract_skills(jd_text)
    jd_keywords   = set(extract_keywords(jd_text))

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    bonus   = resume_skills - jd_skills

    all_required = jd_skills | jd_keywords
    match_pct = round(len(matched) / len(all_required) * 100) if all_required else 0

    return {
        "match_%":        match_pct,
        "matched_skills": matched,
        "missing_skills": missing,
        "bonus_skills":   bonus,
        "jd_keywords":    jd_keywords,
    }