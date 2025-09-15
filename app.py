import streamlit as st
import pandas as pd
import spacy
from serpapi import GoogleSearch
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nlp = spacy.load("en_core_web_sm")


st.set_page_config(page_title="Global Career Navigator", page_icon="🌍", layout="wide")


st.markdown(
    """
    <style>
        body { background-color: #121212; color: #f5f5f5; }
        .stButton>button {
            background-color: #4CAF50; color: white; border-radius: 10px; padding: 10px 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Global Career Navigator</h1>", unsafe_allow_html=True)
st.write("Your AI-powered assistant to explore career opportunities worldwide. 🚀")

st.header("📄 Upload Your Resume")
resume_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

resume_text = ""
if resume_file:
    st.success("✅ Resume uploaded successfully!")
    try:
        pdf_reader = PyPDF2.PdfReader(resume_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text() or ""
    except Exception as e:
        st.error(f"Error reading resume: {e}")

st.header("🎯 Select Your Career Interest")
career_interest = st.selectbox(
    "Choose a field you’re interested in:",
    [
        "Artificial Intelligence", "Machine Learning", "Data Science", "Cybersecurity",
        "Cloud Computing", "DevOps", "Software Engineering", "Web Development",
        "Mobile App Development", "Game Development", "UI/UX Design", "Blockchain",
        "FinTech", "Healthcare Technology", "Biotechnology", "Pharmaceuticals",
        "Renewable Energy", "Civil Engineering", "Mechanical Engineering",
        "Electrical Engineering", "Robotics", "Space/Aerospace Engineering",
        "Education Technology", "Digital Marketing", "Business Analysis",
        "Finance & Banking", "Accounting", "Economics", "Human Resources",
        "Consulting", "Entrepreneurship", "Legal/Compliance", "Supply Chain",
        "Hospitality & Tourism", "Creative Arts & Media", "Sports Science",
        "Psychology & Mental Health", "Social Impact & NGOs"
    ]
)
st.write(f"🌟 You selected: **{career_interest}**")

st.header("🌏 Choose Your Target Country")
countries = [
    "United States", "Canada", "United Kingdom", "Germany", "France", "Spain", "Italy",
    "Netherlands", "Sweden", "Norway", "Denmark", "Finland", "Switzerland", "Australia",
    "New Zealand", "Singapore", "Malaysia", "Japan", "South Korea", "India", "China",
    "Brazil", "Mexico", "South Africa", "United Arab Emirates", "Saudi Arabia", "Qatar",
    "Vietnam", "Thailand", "Philippines", "Indonesia", "Turkey", "Ireland", "Poland",
    "Czech Republic", "Portugal", "Greece", "Belgium", "Austria"
]
country = st.selectbox("Select your target country:", countries)
st.write(f"🌐 Exploring **{career_interest}** jobs in **{country}**...")

if st.button("🔍 Find Real Job Openings"):
    st.info("Fetching live jobs... please wait ⏳")

    query = f"{career_interest} jobs in {country}"
    params = {
        "engine": "google_jobs",
        "q": query,
        "api_key": st.secrets["SERPAPI_KEY"]
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    jobs = results.get("jobs_results", [])

    if jobs:
        st.success(f"✅ Found {len(jobs)} jobs in {country} for {career_interest}!")

        job_list = []
        for job in jobs:
            job_text = f"{job.get('title', '')} {job.get('company_name', '')} {job.get('description', '')}"

            # Match score (resume vs job description)
            if resume_text.strip():
                vectorizer = TfidfVectorizer().fit_transform([resume_text, job_text])
                similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
                match_score = round(similarity * 100, 2)
            else:
                match_score = "N/A"

            job_list.append({
                "Job Title": job.get("title", "N/A"),
                "Company": job.get("company_name", "N/A"),
                "Location": job.get("location", "N/A"),
                "Apply Link": job.get("apply_link", "N/A"),
                "Match Score (%)": match_score
            })

        df = pd.DataFrame(job_list)
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Job List with Match Scores", csv, "jobs.csv", "text/csv")
    else:
        st.error("⚠️ No jobs found. Try another country or career field.")
