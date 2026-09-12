# 🎯 Resume Match Analyzer

An AI-powered resume screening application that evaluates how well a candidate's resume matches a given job description.

## 🚀 Features

- 📄 Upload resumes in **PDF** or **DOCX** format
- 📝 Enter a custom job description
- 🤖 AI-powered resume parsing using **Groq**
- 🎯 Generate an overall **match score**
- 💪 Identify candidate strengths
- ⚠️ Detect missing required skills
- ⭐ Identify missing preferred skills
- 💼 Evaluate experience fit
- 🚨 Highlight important candidate concerns
- 🏆 Provide a recruitment recommendation:
  - `SHORTLIST`
  - `CONSIDER`
  - `LOW FIT`

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web interface
- **Groq API** – AI-powered analysis
- **Pydantic** – Structured data validation
- **PyPDF** – PDF text extraction
- **python-docx** – DOCX text extraction
- **python-dotenv** – Environment variable management
- **uv** – Python package and project management

## 📂 Project Structure

```text
resume-matcher/
│
├── app.py                  # Streamlit frontend
├── resume_matcher.py       # Resume/JD parsing and matching logic
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files
│
└── src/
    └── resume_matcher/
        └── __init__.py
