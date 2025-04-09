import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss

class SHLRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.df.fillna("", inplace=True)
        self.texts = (
            self.df['Individual Test Solutions'] + ". " +
            self.df['Description'] + ". " +
            self.df['Job Levels'] + ". " +
            self.df['Test Type']
        ).tolist()

        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.model.encode(self.texts, show_progress_bar=True)

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def query(self, user_query, top_k=5):
        query_embedding = self.model.encode([user_query])
        _, indices = self.index.search(query_embedding, top_k)
        results = self.df.iloc[indices[0]].to_dict(orient="records")
        return results

recommender = SHLRecommender("shl_catalog_detailed.csv")

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("🔍 SHL Assessment Recommender")

user_query = st.text_input("Enter your job role, skills, or test topic:", "entry level python developer")

if st.button("Recommend Assessments") and user_query:
    with st.spinner("Searching for relevant assessments..."):
        recommendations = recommender.query(user_query)

    st.subheader("📋 Recommended Assessments")
    for rec in recommendations:
        st.markdown(f"**{rec['Individual Test Solutions']}**")
        st.markdown(f"- 🔗 [Link]({rec['URL']})")
        st.markdown(f"- 📄 Description: {rec['Description']}")
        st.markdown(f"- 💼 Job Levels: {rec['Job Levels']}")
        st.markdown(f"- 🧪 Test Type: {rec['Test Type']}")
        st.markdown("---")
