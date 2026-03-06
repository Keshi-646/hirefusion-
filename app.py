from flask import Flask, render_template, request, send_from_directory
import os
import pandas as pd
from ai_skills import get_role_skills, normalize_skills
from parser import extract_text, extract_name, extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------- RESUME VALIDATION ----------------

def is_valid_resume(text):

    resume_keywords = [
        "education",
        "experience",
        "skills",
        "projects",
        "internship",
        "certifications",
        "summary",
        "profile",
        "objective"
    ]

    text = text.lower()

    count = 0
    for word in resume_keywords:
        if word in text:
            count += 1

    return count >= 2


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ANALYZE RESUMES ----------------

@app.route("/analyze", methods=["POST"])
def analyze():

    role = request.form.get("role").strip().title()
    files = request.files.getlist("resumes")

    if len(files) == 0:
        return render_template(
            "index.html",
            error="Please upload resumes."
        )

    role_skills = get_role_skills(role)

    if not role_skills:
        print("Could not fetch skills for this role.")

    candidates = []

    for file in files:

        if file.filename == "":
            continue

        if not allowed_file(file.filename):
            return render_template(
                "index.html",
                error="Upload a valid PDF resume."
            )

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)

        file.save(filepath)

        text = extract_text(filepath)

        # --------- CHECK IF FILE IS RESUME ---------

        if text == "" or len(text) < 100:
            return render_template(
                "index.html",
                error="File does not contain enough content to analyze."
            )

        if not is_valid_resume(text):
            return render_template(
                "index.html",
                error="❌ This document does not appear to be a resume. Please upload a valid resume."
            )

        # --------- EXTRACT INFO ---------

        name = extract_name(text)

        resume_skills = extract_skills(text)

        resume_skills = resume_skills + normalize_skills(resume_skills)

        resume_skills = list(set(resume_skills))

        # --------- SKILL MATCHING ---------

        matched = []

        for r in resume_skills:
            for j in role_skills:
                if r in j or j in r:
                    matched.append(r)

        matched = list(set(matched))

        missing = list(set(role_skills) - set(resume_skills))

        if len(role_skills) > 0:
            score = round((len(matched) / len(role_skills)) * 100)
        else:
            score = 0

        # --------- AI RECOMMENDATION ---------

        if score >= 75:
            recommendation = "Highly Recommended"
        elif score >= 50:
            recommendation = "Consider for Interview"
        else:
            recommendation = "Skill Gap Detected"

        # --------- EXPLAINABLE AI ---------

        explanation = f"{len(matched)} out of {len(role_skills)} required skills matched"

        candidates.append({
            "name": name,
            "resume": file.filename,
            "score": score,
            "matched": matched,
            "missing": missing,
            "recommendation": recommendation,
            "explanation": explanation,
            "filename": file.filename
        })

    if len(candidates) == 0:
        return render_template(
            "index.html",
            error="No valid resumes detected."
        )

    # --------- SORT CANDIDATES ---------

    df = pd.DataFrame(candidates)

    df = df.sort_values(by="score", ascending=False)

    # --------- ADD RANKING ---------

    df["rank"] = range(1, len(df) + 1)

    table = df.to_dict(orient="records")

    # --------- BEST CANDIDATE ---------

    best = table[0]

    return render_template(
        "index.html",
        table=table,
        best=best
    )


# ---------------- OPEN RESUME ----------------

@app.route("/resume/<filename>")
def open_resume(filename):

    return send_from_directory(UPLOAD_FOLDER, filename)


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(debug=True)