import pytesseract
from pdf2image import convert_from_path
from langchain_core.documents import Document

# ─── Direct Paths ─────────────────────────────────────────
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Release-25.12.0-0\poppler-25.12.0\Library\bin"

pdf_path = r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\pdfs\scanned_bill.pdf"

# ─── PDF → Images ─────────────────────────────────────────
pages = convert_from_path(
    pdf_path,
    dpi=300,
    poppler_path=POPPLER_PATH
)

# ─── Images → Text ────────────────────────────────────────
docs = []
for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page, lang="eng")
    docs.append(Document(
        page_content=text,
        metadata={"source": pdf_path, "page": i + 1}
    ))

print(f"Total pages: {len(docs)}")
print(docs[0].page_content[:500])