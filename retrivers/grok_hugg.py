from langchain_huggingface import HuggingFaceEmbeddings
import dotenv, os
from dotenv import load_dotenv
from langchain_openai import *
load_dotenv()
from langchain_community.document_loaders import PyMuPDFLoader, ToMarkdownLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter


embed_model = HuggingFaceEmbeddings(
  model_name= "sentence-transformers/all-MiniLM-L6-v2"
)


llm= ChatOpenAI(
  api_key= os.getenv("XAI_API_KEY"),
model='grok-3-mini',
base_url="https://api.x.ai/v1"
)

# load doc

import pymupdf4llm

path = r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\pdfs\ML CookBook.pdf"

md_text= pymupdf4llm.to_markdown(path, page_chunks=True)

from langchain_core.documents import Document
docs = [Document(page_content=page['text'], metadata =page['metadata']) for page in md_text]


spliter = MarkdownHeaderTextSplitter(
  headers_to_split_on = [ ('#', 'Header_1'),
                        ('##', 'Header_2'),
                        ('###', 'Header_3')]
)
all_chunk=[]
for doc in docs:
  chunks= spliter.split_text(doc.page_content)

  for chunk in chunks:
     chunk.metadata.update(doc.metadata)

  all_chunk.extend(chunks)



from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS

vectore_store = Chroma.from_documents(  documents = all_chunk,
  collection_name='chroma_collection',
  embedding=embed_model,
  persist_directory='chorma_db_1'

)

# vectore_store = Chroma(
#   embedding_function=embed_model,
#   collection_name="chroma_collection",
#   persist_directory='chorma_db_1'
# )


retriver = vectore_store.as_retriever(
  search_type='mmr',
  search_kwargs={'k':3, 'lambda_mult':0.5}
)

from langchain_classic.retrievers import MultiQueryRetriever

mutli_q_retriver = MultiQueryRetriever.from_llm(
  retriever=retriver,
  llm =llm 
)


response = mutli_q_retriver.invoke("What is Statistic")
for doc in response:
    print(doc.page_content)
    print("─" * 50)


