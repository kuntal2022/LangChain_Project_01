from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
import dotenv
import os

dotenv.load_dotenv()

pdf_path = r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\pdfs\pandas_datetime_book.pdf"
CHROMA_DIR = "chroma_db"  # Jahan save hoga

embed_model = OpenAIEmbeddings(model="text-embedding-3-small")

# ─── Check karo — Already exist karta hai? ────────────────
if os.path.exists(CHROMA_DIR):
    print("✅ Vector store already exists — Loading...")
    vectorstore = Chroma(
        collection_name="my_collection",
        embedding_function=embed_model,
        persist_directory=CHROMA_DIR
    )

else:
    print("🔨 First Time Making the Vector Store...")

    # Load
    loader = PyMuPDFLoader(file_path=pdf_path)
    doc_list = []
    x = 0
    for i in loader.lazy_load():
        x += 1
        if 0 <= x <= 43:
            doc_list.append(i)

    # Split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    chunks = splitter.split_documents(doc_list)

    # Save
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embed_model,
        collection_name="my_collection",
        persist_directory=CHROMA_DIR  # ← Save ho jaega!
    )
    print(f"✅ Vector is created and saved! Chunks: {len(chunks)}")

# ─── Retriever ────────────────────────────────────────────
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "What is the strftime function in Python give some examples?"
results = retriever.invoke(query)

print(f"\n{'*' * 50}")
print(results[0].page_content)
print(results[1].page_content)
print(f"{'*' * 50}")