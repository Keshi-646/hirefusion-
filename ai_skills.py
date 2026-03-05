import re
from google import genai

# 🔑 Put your Gemini API key here
client = genai.Client(api_key="AIzaSyDzWdwgHX7XDbhl1pUVEsgo5jctTvVkEzE")


# fallback skills if AI fails
fallback_roles = {

# ---------------- SOFTWARE DEVELOPMENT ----------------

"software engineer": ["java","python","c++","data structures","algorithms","oop","git"],

"software developer": ["java","python","c++","oop","software development"],

"backend developer": ["python","java","nodejs","flask","django","spring","sql","api"],

"frontend developer": ["html","css","javascript","react","angular","vue","ui"],

"full stack developer": ["html","css","javascript","react","nodejs","python","flask","django","sql"],

"web developer": ["html","css","javascript","react","php"],

"api developer": ["rest api","flask","django","nodejs","microservices"],

"microservices developer": ["docker","kubernetes","spring","java","microservices"],

"software architect": ["system design","microservices","scalability","architecture"],

"application developer": ["java","python","software development","oop"],


# ---------------- DATA & AI ----------------

"data analyst": ["excel","sql","python","pandas","power bi","tableau","data visualization"],

"data scientist": ["python","machine learning","statistics","pandas","numpy","sql"],

"machine learning engineer": ["python","machine learning","deep learning","tensorflow","pytorch"],

"ai engineer": ["python","deep learning","nlp","transformers","llm"],

"data engineer": ["python","sql","spark","hadoop","etl","data pipelines"],

"nlp engineer": ["python","nlp","spacy","bert","transformers"],

"computer vision engineer": ["python","opencv","deep learning","tensorflow","pytorch"],

"analytics engineer": ["sql","python","data modeling"],

"bi developer": ["sql","power bi","tableau","data warehouse"],

"ml ops engineer": ["mlops","docker","kubernetes","machine learning deployment"],


# ---------------- MOBILE DEVELOPMENT ----------------

"mobile app developer": ["flutter","react native","java","kotlin","swift"],

"android developer": ["java","kotlin","android studio","firebase"],

"ios developer": ["swift","objective c","xcode","ios development"],

"flutter developer": ["dart","flutter","mobile development"],

"react native developer": ["javascript","react native"],


# ---------------- CLOUD ----------------

"cloud engineer": ["aws","azure","gcp","cloud computing"],

"cloud architect": ["aws","cloud architecture","microservices"],

"cloud developer": ["aws","docker","kubernetes","api"],

"cloud security engineer": ["aws","network security","cloud security"],


# ---------------- DEVOPS ----------------

"devops engineer": ["docker","kubernetes","jenkins","git","linux","ci cd"],

"site reliability engineer": ["linux","docker","kubernetes","monitoring"],

"platform engineer": ["kubernetes","terraform","cloud"],

"build engineer": ["jenkins","ci cd","git"],

"release engineer": ["deployment","ci cd","git"],


# ---------------- CYBER SECURITY ----------------

"cyber security engineer": ["network security","ethical hacking","penetration testing","linux"],

"security analyst": ["siem","threat detection","incident response"],

"penetration tester": ["ethical hacking","kali linux","penetration testing"],

"information security analyst": ["risk assessment","security compliance"],

"security engineer": ["encryption","network security"],


# ---------------- TESTING ----------------

"software tester": ["manual testing","test cases","qa","bug tracking"],

"qa engineer": ["testing","automation testing","selenium","testng"],

"automation tester": ["selenium","python","java","automation testing"],

"performance tester": ["jmeter","performance testing"],

"test engineer": ["testing","qa","automation testing"],


# ---------------- DATABASE ----------------

"database administrator": ["sql","mysql","postgresql","database management"],

"database developer": ["sql","plsql","database design"],

"data warehouse engineer": ["etl","data warehouse","sql"],

"big data engineer": ["hadoop","spark","big data"],


# ---------------- SYSTEM / NETWORK ----------------

"system administrator": ["linux","windows server","networking"],

"network engineer": ["tcp ip","routing","switching","networking"],

"it support engineer": ["troubleshooting","hardware","windows"],

"technical support engineer": ["network troubleshooting","customer support"],


# ---------------- UI / UX ----------------

"ui designer": ["figma","ui design","prototyping"],

"ux designer": ["user research","wireframing","figma"],

"product designer": ["ui ux","design thinking"],


# ---------------- BLOCKCHAIN ----------------

"blockchain developer": ["solidity","ethereum","web3"],

"smart contract developer": ["solidity","smart contracts"],


# ---------------- EMERGING ROLES ----------------

"prompt engineer": ["prompt engineering","llm","ai"],

"generative ai engineer": ["transformers","llm","pytorch"],

"ai researcher": ["machine learning","deep learning","research"],


# ---------------- TESTING / QA ROLES ----------------

"manual tester": [
    "manual testing","test cases","bug reporting","qa"
],

"automation tester": [
    "selenium","python","java","automation testing","testng"
],

"qa tester": [
    "manual testing","qa","test cases","bug tracking"
],

"qa analyst": [
    "quality assurance","test cases","defect tracking"
],

"qa automation engineer": [
    "selenium","cypress","automation testing","python","java"
],

"sdet": [
    "automation testing","java","python","selenium","test frameworks"
],

"software development engineer in test": [
    "automation testing","selenium","java","python"
],

"performance tester": [
    "jmeter","load testing","performance testing"
],

"security tester": [
    "security testing","penetration testing","vulnerability testing"
],

"api tester": [
    "postman","rest api","api testing"
],

"mobile tester": [
    "mobile testing","android testing","ios testing"
],

"game tester": [
    "game testing","bug tracking","qa"
],

"uat tester": [
    "user acceptance testing","qa","test cases"
],


# ---------------- SUPPORT / IT SERVICE ----------------

"technical support engineer": [
    "troubleshooting","network troubleshooting","customer support"
],

"application support engineer": [
    "application support","sql","incident management"
],

"production support engineer": [
    "production support","linux","sql","incident management"
],

"it support specialist": [
    "troubleshooting","hardware","networking"
],

"help desk engineer": [
    "technical support","ticketing systems","troubleshooting"
],


# ---------------- DEVOPS ADVANCED ----------------

"devops architect": [
    "aws","kubernetes","docker","infrastructure","devops"
],

"cloud devops engineer": [
    "aws","docker","kubernetes","ci cd"
],

"infrastructure engineer": [
    "linux","cloud","networking","infrastructure"
],

"site reliability engineer": [
    "monitoring","linux","kubernetes","cloud"
],


# ---------------- ADVANCED SOFTWARE ROLES ----------------

"embedded software engineer": [
    "c","c++","embedded systems","microcontrollers"
],

"firmware engineer": [
    "c","embedded systems","firmware development"
],

"systems engineer": [
    "system design","architecture","linux"
],

"solutions architect": [
    "cloud architecture","aws","system design"
],

"technical architect": [
    "system architecture","microservices","cloud"
],


# ---------------- DATA ADVANCED ROLES ----------------

"big data developer": [
    "hadoop","spark","scala","big data"
],

"data warehouse developer": [
    "etl","data warehouse","sql"
],

"analytics consultant": [
    "data analysis","business intelligence","sql"
],


# ---------------- AI ADVANCED ROLES ----------------

"deep learning engineer": [
    "deep learning","tensorflow","pytorch"
],

"ai developer": [
    "python","machine learning","deep learning"
],

"computer vision developer": [
    "opencv","deep learning","python"
],

"nlp developer": [
    "nlp","transformers","spacy"
]

}


def get_role_skills(role):

    role = role.lower().strip()

    # ✅ If role exists → use dataset
    if role in fallback_roles:
        return normalize_skills(fallback_roles[role])

    # 🤖 If role unknown → use Gemini AI
    prompt = f"""
You are an expert HR recruiter.

List the most important technical skills required for the job role: {role}

Rules:
- Return ONLY comma separated skills
- No explanation
- Maximum 12 skills

Example:
python, machine learning, pandas, numpy, sql
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text.lower()

        # clean unwanted characters
        text = re.sub(r"[^a-z0-9,+ ]", "", text)

        skills = text.split(",")

        skills = [s.strip() for s in skills if s.strip()]

        skills = normalize_skills(skills)

        if len(skills) > 0:
            return skills

    except Exception as e:
        print("AI error:", e)

    return []


def normalize_skills(skills):

    alias = {
        "ml": "machine learning",
        "dl": "deep learning",
        "ai": "artificial intelligence",
        "py": "python",
        "structured query language": "sql",
        "js": "javascript",
        "reactjs": "react",
        "node": "nodejs"
    }

    normalized = []

    for s in skills:

        s = s.lower().strip()

        if s in alias:
            s = alias[s]

        normalized.append(s)

    return list(set(normalized))
