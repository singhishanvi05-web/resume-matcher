from flask import Flask, render_template, request, jsonify
from matcher import match

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data        = request.get_json()
    resume_text = data.get("resume", "")
    jd_text     = data.get("jd", "")

    if not resume_text or not jd_text:
        return jsonify({"error": "Both fields are required"}), 400

    result = match(resume_text, jd_text)

    return jsonify({
        "match_pct":      result["match_%"],
        "matched_skills": list(result["matched_skills"]),
        "missing_skills": list(result["missing_skills"]),
        "bonus_skills":   list(result["bonus_skills"]),
        "jd_keywords":    list(result["jd_keywords"])[:8],
    })

if __name__ == "__main__":
    app.run(debug=True)
