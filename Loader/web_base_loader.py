import langchain_community
from langchain_community.document_loaders import WebBaseLoader , SeleniumURLLoader
url="https://en.wikipedia.org/wiki/Main_Page"

loader = WebBaseLoader(url)
docs=loader.lazy_load()

for doc in docs:
  print(doc.page_content)