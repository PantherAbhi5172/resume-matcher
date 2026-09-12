# 🎯 AI-Powered Resume Match Analyzer

<p align="center">
  <b>AI-powered resume screening and job-fit analysis for smarter hiring decisions.</b>
</p>

<p align="center">
  <a href="https://resume-matcher01.streamlit.app/">
    🚀 <b>Try the Live Demo</b>
  </a>
</p>

---

## 📌 Overview

**Resume Match Analyzer** is an AI-powered candidate screening application that compares a candidate's resume with a given job description and provides an actionable hiring assessment.

Instead of manually going through every resume, recruiters can upload a resume, provide a job description, and instantly receive:

- 🎯 Overall Match Score
- 💪 Candidate Strengths
- ⚠️ Missing Required Skills
- ⭐ Missing Preferred Skills
- 💼 Experience Fit
- 🚨 Key Concerns
- 🏆 Hiring Recommendation

The goal is simple:

> **Screen smarter. Hire faster.**

---

## 🚀 Live Demo

### 👉 [Open Resume Match Analyzer](https://resume-matcher01.streamlit.app/)

Upload a **PDF/DOCX resume**, paste a job description, and click **Analyze Resume**.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📄 Resume Upload | Supports PDF and DOCX resumes |
| 🤖 AI Resume Parsing | Extracts structured candidate information |
| 📝 JD Analysis | Converts job descriptions into structured requirements |
| 🎯 Match Score | Calculates overall resume-to-JD fit |
| 💪 Strength Analysis | Identifies relevant candidate strengths |
| ⚠️ Skill Gap Detection | Finds missing required skills |
| ⭐ Preferred Skills | Highlights missing desirable skills |
| 💼 Experience Analysis | Evaluates experience against job requirements |
| 🚨 Concern Detection | Highlights important candidate weaknesses |
| 🏆 Hiring Recommendation | SHORTLIST / CONSIDER / LOW FIT |
| ☁️ Cloud Deployment | Deployed using Streamlit Cloud |

---

## 🧠 How It Works

```text
                ┌─────────────────────┐
                │   Candidate Resume  │
                │      PDF / DOCX     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Text Extraction   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    AI Resume Parser │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Structured Resume   │
                │       Data          │
                └──────────┬──────────┘
                           │
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
┌───────────────────┐               ┌───────────────────┐
│   Job Description │               │ Candidate Resume │
└─────────┬─────────┘               └─────────┬─────────┘
          │                                   │
          ▼                                   ▼
┌───────────────────┐               ┌───────────────────┐
│    AI JD Parser   │               │ Structured Resume │
└─────────┬─────────┘               └─────────┬─────────┘
          │                                   │
          └────────────────┬──────────────────┘
                           ▼
                ┌─────────────────────┐
                │   AI Match Engine   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Candidate Analysis  │
                ├─────────────────────┤
                │ Match Score         │
                │ Strengths           │
                │ Skill Gaps          │
                │ Experience Fit      │
                │ Concerns            │
                │ Recommendation      │
                └─────────────────────┘
