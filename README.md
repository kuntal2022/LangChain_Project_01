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

### 5. 📱 Customer Personalized SMS Generator — Branch Chains
Upload a customer CSV — get AI-generated personalized SMS for each customer segment!

**Features:**
- Upload customer CSV file
- Auto-detects RFM Segment (Champion, At_Risk, Lost)
- Unique combination of Nationality + Vintage + Customer Bucket
- Personalized SMS for each unique combination
- Timer shows processing time
- Final SMS exported to Excel

**Tech Used:**
- `RunnableBranch` — Different SMS strategy for each RFM segment
- `with_structured_output` — Pydantic BaseModel for RFM detection
- `RunnableLambda` — Convert object to dict
- Pandas — CSV reading + unique combinations
- GPT-4o-mini
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
| 🐼 Pandas | Data processing |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/your-repo.git

# Go to project folder
cd your-repo

# Install dependencies
pip install langchain langchain-openai langchain-community streamlit python-dotenv pymupdf python-docx pydantic pandas openpyxl
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
streamlit run sms_generation.py
```

---

## 📚 What I Learned

- How OpenAI API works — endpoints, payloads, headers
- Difference between SDK and raw requests
- LangChain Runnables — `RunnableParallel`, `RunnableBranch`, `RunnableLambda`, `RunnablePassthrough`
- Structured outputs with Pydantic
- Building Streamlit UIs
- Managing API keys securely with `.env` and `.gitignore`
- Generator, Iterator, Iterable in Python
- LangChain Document Loaders — PDF, DOCX, TXT, CSV, Directory

---

## 🐍 Python Concepts Documented

### Generator, Iterator, Iterable
Built a full Streamlit documentation page covering:

**Generator Function**
- `yield` vs `return` — yield pauses the function, return ends it
- `next()` — retrieves values one by one from a generator
- Generator object — memory efficient, does not load all data at once
- Real examples — Fibonacci series, String character generator

```python
# Generator example
def my_gen(n):
    for i in range(n):
        yield i  # returns one value at a time

g = my_gen(100)
print(next(g))  # 0
print(next(g))  # 1
```

**Iterator vs Iterable**
- Iterable — any object that can be passed to `iter()` (list, string, tuple)
- Iterator — any object that works with `next()`
- `iter()` — converts an Iterable into an Iterator

**Connection to LangChain**
- `lazy_load()` is also a generator
- Loads large PDF files one page at a time — memory efficient!

---

## 📂 LangChain Document Loaders

Learned `langchain_community` document loaders:

### Loaders Covered

| Loader | File Type | Best For |
|---|---|---|
| `TextLoader` | `.txt` | Plain text files |
| `Docx2txtLoader` | `.docx` | Word documents |
| `PyPDFLoader` | `.pdf` | Text-based PDFs |
| `DirectoryLoader` | Folder | Multiple files at once |
| `CSVLoader` | `.csv` | CSV data files |

### load() vs lazy_load()

```python
# load() — loads everything into memory at once
docs = loader.load()           # heavy for large files

# lazy_load() — generator — loads one page at a time
for doc in loader.lazy_load(): # memory efficient
    print(doc.page_content)
```

`lazy_load()` is a generator — best for large PDFs as it loads one page at a time without filling up memory.

### PDF Loader Guide — Which One to Use?

| Situation | Best Loader |
|---|---|
| Normal text-based PDF | `PyPDFLoader` |
| PDF with tables | `PDFPlumberLoader` |
| Scanned / Image PDF | `UnstructuredPDFLoader` (uses OCR) |
| Excel file | `pandas.read_excel()` |
| CSV file | `CSVLoader` or `pandas.read_csv()` |

```python
# Text-based PDF
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("file.pdf")

# PDF with tables
from langchain_community.document_loaders import PDFPlumberLoader
loader = PDFPlumberLoader("file.pdf")

# Scanned or image-based PDF — requires OCR
from langchain_community.document_loaders import UnstructuredPDFLoader
loader = UnstructuredPDFLoader("file.pdf")

# Word Document
from langchain_community.document_loaders import Docx2txtLoader
loader = Docx2txtLoader("file.docx")

# Entire folder at once
from langchain_community.document_loaders import DirectoryLoader
loader = DirectoryLoader("./folder/", glob="**/*.pdf")

# CSV file
from langchain_community.document_loaders import CSVLoader
loader = CSVLoader("file.csv")
```

---

---

### 6. 📚 Multi-Books RAG — Question Answering System

Ask questions across **7 ML/AI books** and get context-aware answers with full chat history support.

**Books Covered:**
- Building Machine Learning Systems with Python
- Deep Learning from Scratch
- Machine Learning for Mathematics
- ML CookBook
- Must-Read on AI Agents
- Pandas Datetime Book
- Practical Statistics for Data Scientists

**Features:**
- Ask any question — answer comes strictly from the books
- Multi-turn chat history (remembers previous questions)
- Smart chunk size auto-detection using token statistics
- Duplicate/irrelevant chunk filtering via MMR search

**How it works:**
1. PDFs loaded via `DirectoryLoader` + `PyMuPDFLoader`
2. Text cleaned — page numbers, extra whitespace removed
3. Best chunk size auto-calculated using `tiktoken` token distribution
4. Chunks embedded via `HuggingFace (all-MiniLM-L6-v2)` → stored in `FAISS`
5. `MultiQueryRetriever` generates 3 alternate queries via **Gemini 2.5 Pro**
6. Top-5 diverse chunks fetched via MMR search
7. **Grok-3-fast** generates final answer from context + chat history

**Tech Used:**
| Component | Technology |
|---|---|
| Document Loading | `DirectoryLoader` + `PyMuPDFLoader` |
| Embeddings | `HuggingFace all-MiniLM-L6-v2` |
| Vector Store | `FAISS` (persisted locally) |
| Retriever | `MultiQueryRetriever` (MMR, k=5) |
| Query LLM | `Gemini 2.5 Pro` |
| Answer LLM | `Grok-3-fast` (xAI) |
| Chat History | `HumanMessage` + `AIMessage` (file-persisted) |
| UI | `Streamlit` — `st.chat_message` |

**LCE Chain Flow:**



## 👨‍💻 Author

**Kuntal** — Learning AI one project at a time 🚀

---

⭐ If you found this helpful, give it a star!
