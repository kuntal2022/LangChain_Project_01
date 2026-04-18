import fitz, langchain, langchain_core, langchain_community
from langchain_community.document_loaders import PyMuPDFLoader


pdf_path = r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\pdfs\ML CookBook.pdf"

loader = PyMuPDFLoader(file_path=pdf_path)

docs = loader.load()

print(len(docs))

print(docs[0].metadata)
print(docs[125].page_content)
