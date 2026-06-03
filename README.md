# HeathcareAPP
# 🩸 Blood Report Analyser

An AI-powered Streamlit application that analyses blood reports, extracts key parameters, flags abnormal values, and recommends personalised Indian diet plans — built with LangChain, Groq, and Llama 3.3.

---

## 📸 Demo

> Paste or upload a blood report → Get instant analysis + Indian diet recommendations

---

## ✨ Features

- **Automatic Parameter Extraction** — Pulls all values from CBC, Lipid, Metabolic, and Liver panels
- **Smart Status Detection** — Flags each parameter as High / Low / Normal with risk level
- **Overall Risk Assessment** — Summarises urgent parameters at a glance
- **Indian Diet Recommendations** — Personalised meal plan based on your specific report
- **JSON Export** — Download structured analysis data for further use
- **File Upload Support** — Paste text or upload a `.txt` blood report file
- **Clean Dashboard UI** — Dark-themed, card-based layout with category grouping

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **LLM Framework** | LangChain |
| **LLM Provider** | Groq (free tier) |
| **Model** | Llama 3.3 70B Versatile |
| **Language** | Python 3.12 |
| **Environment** | python-dotenv |

---

## 📁 Project Structure

```
Heathcare_App/
├── Stream_lit_app/
│   └── blood_report_app.py     # Main Streamlit app
├── notebooks/
│   └── blood_analysis.ipynb    # Development notebook
├── .streamlit/
│   └── secrets.toml            # API keys (never push to GitHub)
├── .env                        # Local environment variables (never push)
├── .gitignore                  # Files excluded from git
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## ⚙️ Setup and Installation

### Prerequisites
- Python 3.10 or higher
- A free Groq API key from [console.groq.com](https://console.groq.com)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/heathcareapp.git
cd heathcareapp
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Or create `.streamlit/secrets.toml` for Streamlit:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### 5. Run the App

```bash
streamlit run Stream_lit_app/blood_report_app.py
```

Open your browser at `http://localhost:8501`

---

## 📦 Requirements

Create a `requirements.txt` with:

```
streamlit
langchain
langchain-groq
langchain-core
python-dotenv
```

Generate automatically with:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Deploy to Streamlit Cloud

1. Push your code to GitHub (make sure `.env` and `secrets.toml` are in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set your secret under **Manage App → Secrets**:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

5. Click **Deploy**

---

## 🔒 Security

- Never commit `.env` or `secrets.toml` to GitHub
- Never commit patient blood report files
- API keys are loaded via environment variables only
- See `.gitignore` for full list of excluded files

---

## 📊 Sample Blood Report Format

The app accepts blood reports in plain text format:

```
Patient: Rajesh Sharma, Age 48, Male
Date: May 7, 2026

COMPLETE BLOOD COUNT (CBC)
Hemoglobin: 15.1 g/dL (Normal: 13.5–17.5)
WBC: 6.8 x10^3/uL (Normal: 4.5–11.0)

LIPID PANEL
Total Cholesterol: 238 mg/dL (Normal: <200)
LDL Cholesterol: 162 mg/dL (Normal: <100)
...
```

---

## 🧠 How It Works

```
User inputs blood report
        ↓
LangChain sends to Groq (Llama 3.3)
        ↓
Model extracts parameters → returns JSON
        ↓
App renders parameter cards with status
        ↓
Second LLM call generates Indian diet plan
        ↓
User views analysis + downloads JSON
```

---

## ⚠️ Disclaimer

This application is for **informational and educational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical decisions.

---

## 👨‍💻 Author

**Lekshmi**
- Built as part of AI Projects portfolio
- Location: Kochi, Kerala, India

---

## 📄 License

This project is for personal and educational use only. Not for commercial distribution.
