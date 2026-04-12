dir_path = r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\pdfs"
import langchain_community
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import pypdf

loader = DirectoryLoader(path=dir_path, 
                         glob="*.pdf",
                         loader_cls = PyPDFLoader)
docs=loader.lazy_load()

for i in docs:
  print(i.metadata)