import langchain_community
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\documnets_folders\customers.csv")

docs = loader.load()


print('each row will be represnted as one documents')
print(len(docs))
print()
for i in range(len(docs)):
  print(docs[i].page_content)
  print()