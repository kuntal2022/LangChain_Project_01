# 🦜 LangChain Projects — by Kuntal

> A collection of AI projects built while learning LangChain, OpenAI, and Streamlit from scratch.

---

## 🚀 Projects

### 1. 🔌 OpenAI — SDK vs Without SDK
My first step into AI APIs. Learned how to call OpenAI:
- **Without SDK** — Raw `requests.post()` hitting the endpoint directly
- **With SDK** — Using the `openai` Python library
- Understood what endpoints, payloads, and headers are

---

### 2. 📄 CV Analyzer (ATS Tool) — Parallel Chains
Upload your CV and paste a Job Description — get an AI-powered ATS match score!

**Features:**
- Upload CV as PDF or DOCX
- Paste any Job Description
- Get matching score (e.g. 84.3%)
- Detailed JD vs CV comparison table
- Improvement suggestions

**Tech Used:**
- `RunnableParallel` — Skills, Projects, Others analyzed simultaneously
- `RunnableLambda` — Pass JD through the chain
- GPT-4o + GPT-4o-mini
- Streamlit UI
- PyMuPDF + python-docx

---

### 3. 😊 Emotion Detector — Branch Chains
Type your mood or emoji — get a response based on how you feel!

**Features:**
- Detects mood — Happy, Sad, Angry, Other
- Different AI response for each mood
- Structured Output with Pydantic

**Tech Used:**
- `RunnableBranch` — Different chain for each mood
- `with_structured_output` — Pydantic BaseModel
- `RunnableLambda` — Convert Pydantic object to dict
- GPT-3.5-turbo + GPT-4o-mini
- Streamlit UI

---

### 4. 🎬 Movie Recommendation System — Branch Chains
Give a one-liner story — get movie recommendations based on the genre!

**Features:**
- Detects genre from your story — Horror, Romance, SciFi, Comedy, etc.
- Recommends Bollywood + Hollywood movies
- 10+ genre support

**Tech Used:**
- `RunnableBranch` — Different chain for each genre
- `with_structured_output` — Pydantic BaseModel
- `RunnableLambda` — Convert object to dict
- GPT-4.1-mini
- Streamlit UI

---

## 🛠️ Tech Stack

| Technology | Use |
|---|---|
| 🦜 LangChain | Chains, Runnables, Prompts |
| 🤖 OpenAI API | GPT-4o, GPT-4o-mini, GPT-4.1 |
| 🖥️ Streamlit | UI for all projects |
| 🐍 Pydantic | Structured outputs |
| 📄 PyMuPDF | PDF reading |
| 📝 python-docx | DOCX reading |
| 🔐 python-dotenv | API key management |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/your-repo.git

# Go to project folder
cd your-repo

# Install dependencies
pip install langchain langchain-openai streamlit python-dotenv pymupdf python-docx pydantic
```

---

## 🔐 Setup

Create a `.env` file in the root folder:

```
OPENAI_API_KEY=your-api-key-here
```

---

## ▶️ Run any project

```bash
streamlit run cv_analyzer.py
streamlit run emotion_detector.py
streamlit run movie_recommendation.py
```

---

## 📚 What I Learned

- How OpenAI API works — endpoints, payloads, headers
- Difference between SDK and raw requests
- LangChain Runnables — `RunnableParallel`, `RunnableBranch`, `RunnableLambda`, `RunnablePassthrough`
- Structured outputs with Pydantic
- Building Streamlit UIs
- Managing API keys securely with `.env` and `.gitignore`

---

## 👨‍💻 Author

**Kuntal** — Learning AI one project at a time 🚀

---

⭐ If you found this helpful, give it a star!
