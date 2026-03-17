from matcher import match
from visualizer import plot_results

resume = """
Software Engineer with 3 years experience.
Skills: Python, Flask, Docker, AWS, PostgreSQL, Git, Machine Learning, Pandas
"""

jd = """
Looking for a Backend Engineer.
Required: Python, AWS, Docker, Kubernetes, SQL, CI/CD, ML experience preferred.
"""

result = match(resume, jd)

print(f"\n Match Score     : {result['match_%']}%")
print(f" Matched Skills  : {result['matched_skills']}")
print(f" Missing Skills  : {result['missing_skills']}")
print(f" Bonus Skills    : {result['bonus_skills']}")

plot_results(result["matched_skills"], result["missing_skills"], result["match_%"])