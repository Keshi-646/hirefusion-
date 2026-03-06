HIREFUSION – AI Powered Resume Screening & Skill Matching Platform

**Hirefusion** is an AI-powered resume screening platform that helps recruiters quickly analyze resumes and match them with job roles based on required skills.

The system extracts skills from uploaded resumes, compares them with role-specific skills, and calculates a **matching score**. It also highlights **matching skills and missing skills**, helping both recruiters and candidates understand the suitability of the resume.
This platform reduces manual resume screening and improves hiring efficiency using **AI-driven skill analysis**.
 
 Problem Statement

Recruiters often receive hundreds of resumes for a single job role. Manually analyzing these resumes is time-consuming and inefficient.
**AlgoMatch solves this problem by:**

* Automatically extracting skills from resumes
* Comparing them with job role requirements
* Providing an instant skill match score

 Key Features
 Resume Upload
Upload multiple resumes in PDF format.
Skill Extraction
Automatically extracts candidate skills from resumes.
Role-Based Matching
Compares resume skills with job role skills.
Matching Score
Displays percentage of skill match.
Matching Skills Highlight
Shows skills that match the job role.
Missing Skills Detection
Identifies important skills missing from the resume.
Explainable AI
Shows how the score was calculated.
Collaboration Features
Allows HR teams to evaluate candidates efficiently.
 Tech Stack

**Frontend**
* HTML
* CSS
* JavaScript
**Backend**
* Python
* Flask
Libraries & Tools
* Pandas
* PDF Parser
* Google Gemini API (AI skill extraction)
 How It Works

Upload candidate resumes
System extracts text from the resume
AI identifies skills in the resume
Skills are compared with job role requirements
Matching score is calculated
Matching and missing skills are displayed
Project Structure

```
AlgoMatch
│
├── app.py
├── ai_skills.py
├── parser.py
├── requirements.txt
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
└── uploads
```

---

## ▶️ Installation & Setup

Clone the repository
```
git clone https://github.com/yourusername/AlgoMatch.git
```
Navigate to the project folder
```
cd AlgoMatch
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application

```
python app.py
```
Open in browser

```
http://127.0.0.1:5000
```
 Future Improvements

* Resume ranking system
* Support for DOCX resumes
* HR dashboard
* Candidate recommendation system
* AI interview question generation

  #demo screenshot
  <img width="1879" height="869" alt="image" src="https://github.com/user-attachments/assets/7bbaf322-5f3a-4d4a-ad82-3d197d83634a" />

#author
**Keshiya V**
Artificial Intelligence & Data Science Student
Passionate about AI, Web Development, and Problem Solving.


