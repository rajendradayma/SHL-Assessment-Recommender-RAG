# SHL-Assessment-Recommender-RAG
[SHL Assessment Recommender (RAG)](https://shl-assessment-recommender-rag-fn6qzbnnsqb3s2ejrv9ps3.streamlit.app/)

A Streamlit-based application that takes a user query or job description and returns the most relevant SHL assessment from a provided catalog using semantic search.

---

## 🔍 Problem Statement

Given a dataset of SHL assessments, build an intelligent system that recommends the most relevant test based on a user-provided input query or job description. The goal is to simplify and optimize assessment selection for hiring and development purposes.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Pandas
- **Vector Search**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **Data**: SHL assessment catalog (CSV)
- **Deployment**: Streamlit Cloud / Localhost

---

## 📊 Architecture

![System Architecture]("![shl architecture](https://github.com/user-attachments/assets/59c455cc-d0c8-4968-bac6-a274421c7af9)
")
---


## 🚀 Features

- Uploads and processes SHL catalog data
- Embeds assessment descriptions using Sentence Transformers
- Accepts user input (query/job description)
- Returns top N matching assessments with scores
- Simple, responsive UI using Streamlit

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/SHL-Assessment-Recommender.git
cd SHL-Assessment-Recommender
pip install -r requirements.txt
streamlit run app.py

POST /recommend
{
  "query": "We need a test for leadership and decision-making"
}

Response:
[
  {
    "assessment": "Situational Judgement Test",
    "score": 0.89,
    "link": "https://example.com/assessment"
  }
]


├── app.py
├── shl_catalog_detailed.csv
├── README.md
├── requirements.txt
└── architecture.png


