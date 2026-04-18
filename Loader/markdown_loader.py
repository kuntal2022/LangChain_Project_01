from langchain_community.document_loaders import ToMarkdownLoader
import langchain
from langchain_core.documents  import Document

# neet to convert the pdfto markdown format before loading the document, as the markdown format is more structured and can be easily parsed by the loader. The ToMarkdownLoader will take care of converting the PDF to markdown format and then loading the document into a format that can be used for further processing.

import pymupdf4llm # this library is used to convert the pdf to markdown format, it is a wrapper around the fitz library which is used to extract text from pdfs. The pymupdf4llm library provides a simple interface to convert the pdf to markdown format, which can then be loaded by the ToMarkdownLoader.

# pat var
pdf_path = r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\pdfs\ML CookBook.pdf"


md_text = pymupdf4llm.to_markdown(pdf_path)

docs=[Document(page_content=md_text, metadata={"source": pdf_path})]


print("*************Load**************")
print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)