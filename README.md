🌍 Global Career Navigator

Global Career Navigator is a Streamlit-based web application that helps students and professionals explore global internship and job opportunities. It integrates with SerpAPI to fetch real-time job postings and provides insights into industries, salaries, and locations. This tool is designed to give you a clear view of career prospects worldwide in a simple and interactive way.


 🚀 Features
- 🔎 Search for global internships and job opportunities.
- 🌐 Filter by role, country, or company.
- 📊 Compare opportunities across different regions.
- 🖥️ Interactive and user-friendly Streamlit interface.
- 📄 Upload resumes for personalized AI-assisted guidance.
- 🌍 Wide coverage of career fields and target countries.


🛠️ Tech Stack
- Python 3.10+
- Streamlit (Web UI)  
- spaCy (Natural Language Processing for resume parsing)  
- SerpAPI (Real-time career/job search)  
- Pandas & Requests (Data handling and API requests)  
- PDFPlumber (Extracting text from resumes)

 
 ⚙️ Installation & Setup

 1. Clone the Repository
```bash
git clone https://github.com/Dharrsu/Global_Career_Navigator.git
cd Global_Career_Navigator
```

2. Create a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate   # Mac/Linux
# OR
.\env\Scripts\activate    # Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
> If you don’t have `requirements.txt`, you can create it with:  
```bash
pip freeze > requirements.txt
```

 4. Add API Keys
Create a `.streamlit/secrets.toml` file and add your API keys:

```toml
SERPAPI_KEY = "your_serpapi_key_here"
```
> Replace `"your_serpapi_key_here"` with your actual SerpAPI key.  

5. Run the App
```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501` to use the app.

📌 Usage
1. Upload your resume in PDF format.  
2. Select your career interest from the broad list.  
3. Choose your target country to explore opportunities.  
4. Click **Analyze Opportunities** to fetch AI-assisted insights.  

