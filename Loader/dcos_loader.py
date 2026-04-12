from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader(file_path=r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\documnets_folders\cricket_poem.docx")

docs=loader.load()

print(len(docs))


# lazy loader example

docs_lazy=loader.lazy_load()

for i in docs_lazy:
  print(i.metadata)