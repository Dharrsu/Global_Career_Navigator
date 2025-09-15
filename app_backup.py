import streamlit as st
import pandas as pd
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Set page config (must be first Streamlit command)
st.set_page_config(page_title="Global Career Navigator", page_icon="🌍")

# Title
st.title("🌍 Global Career Navigator")
st.write("Your AI-powered assistant to explore career opportunities worldwide.")

# Step 1: Upload Resume
st.header("📄 Upload Your Resume")
resume_file = st.file_uploader("Upload a PDF resume", type=["pdf"])

if resume_file:
    st.success("Resume uploaded successfully! (We’ll process this later.)")

# Step 2: Choose Career Interest
st.header("🎯 Select Your Career Interest")
career_interest = st.selectbox(
    "Choose a field you’re interested in:",
    ["Artificial Intelligence", "Cybersecurity", "Healthcare", "Finance", "Software Engineering"]
)

st.write(f"You selected: **{career_interest}**")

# Step 3: Choose Country
st.header("🌏 Choose Your Target Country")
country = st.selectbox(
    "Where would you like to work?",
    ["United States", "Singapore", "United Kingdom", "Germany", "Australia"]
)

st.write(f"Exploring {career_interest} jobs in {country}...")

# Placeholder for analysis
if st.button("🔍 Analyze Opportunities"):
    st.success("Analysis feature coming soon! 🚀")
