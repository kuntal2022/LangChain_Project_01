from langchain_community.document_loaders import PyPDFLoader
from time import time
loader = PyPDFLoader(file_path=r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\pdfs\Building Machine Learning Systems with Python - Second Edition.pdf")
start=time()
docs=loader.load()
print("----------------Load---------------------")
print(docs[1].metadata)
end=time() 
print(f"Load function took time = {end-start} Sec")
load_ka_time=end-start

print("-----------------Lazy Load--------------------")
start=time()
docs_lazy=loader.lazy_load()
for doc in docs_lazy:
  print(doc.metadata)
end=time() 
print(f"Load function took time = {end-start} Sec")
lazy_load_ka_time=end-start

print()
print(f"Load function took time = {lazy_load_ka_time-load_ka_time} Sec")