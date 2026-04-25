#make the header and get the query
import streamlit as st
st.header("Multi Books : Question Ans Rag")
st.subheader("Author - Kuntal")
st.write("""Sourcse are :                                               
         1.Building Machine Learning Systems with Python - Second Edition        
         2.Deep Learning from Scratch     
         3.Machine Learning for Mathematics     
         4.ML CookBook     
         5.Must-Read on AI Agents     
         6.pandas_datetime_book     
         7.Practical Statistics for Data Scientists     
         """)
#get the query
query=st.chat_input()


# Import Libraries

import dotenv, os, pandas as pd, numpy as np, warnings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.retrievers import MultiQueryRetriever
import langchain_chroma, langchain_classic, langchain_community, langchain_google_genai
from langchain_openai import *
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import * 
from langchain_community.document_loaders import * 
from langchain_core.documents import Document 
from langchain_classic.vectorstores import FAISS 
from langchain_text_splitters import *
import re , tiktoken



warnings.filterwarnings('ignore')

#env steup 
dotenv.load_dotenv()

file_path = directory_path =r"C:\Users\Neel\Desktop\Azure_open_ai\Data\pdfs"




# Make function to clean the text 

def clean_text(text):
    # 1. Page numbers remover
    text = re.sub(r'^\d+$', '', text, flags=re.MULTILINE)
    
    # 2. Image placeholders remover
    text = re.sub(r'==>.*?<==', '', text)
    
    # 3. Extra whitespace remover
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 4. Extra spaces remover
    text = re.sub(r' {2,}', ' ', text)
    
    return text.strip()


#directory loader 
dir_loader = DirectoryLoader(directory_path, 
                             glob="**/*.pdf",  # Only pdf files
                             loader_cls=PyMuPDFLoader # Using pymupdf 
                             )

# Cleaing function
lazy_docs = dir_loader.lazy_load()

# getting best chunk size 

#tiktoken token count
enc = tiktoken.encoding_for_model('gpt-3.5-turbo')

row=[]
doc_list =[]
for  doc in lazy_docs:
  chunk_doc=([Document(page_content=clean_text(doc.page_content).strip(), 
                    metadata=doc.metadata)] )
  row.append({
        'text': doc.page_content,   
    })

  doc_list.extend(chunk_doc)



stats_df = pd.DataFrame(row)
stats_df['token_count']= stats_df['text'].apply(lambda x: len(enc.encode(x)))


def Best_token(df, thresold=0.55):
    q=df['token_count'].quantile(thresold)
    return min(max(q, 300),800)

chunk_size = Best_token(stats_df)


# Spliter 
recuresive_spliter = RecursiveCharacterTextSplitter(
                                                    chunk_size = chunk_size, 
                                                    chunk_overlap=chunk_size//10
                                                    )

chunks = recuresive_spliter.split_documents(doc_list)



# Vectore Base Creation
dir_path =r"C:\Users\Neel\Desktop\Azure_open_ai\Data\VectStore\Faiss_folder_1"

# Hugging face embedding
embed = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")
if os.path.exists(dir_path):
  print("The Vectore base is Present Loading.........")

  vectore_base = FAISS.load_local(dir_path, allow_dangerous_deserialization=True, embeddings=embed)
  print("Loading Successful..")

    
else:
  # Vectore base creation ussing Faiss
  print(f"Vectore base creating at the path {dir_path}")
  vectore_base = FAISS.from_documents(
    documents=chunks,
      embedding=embed
  )
  vectore_base.save_local(dir_path)

#ret_llm
ret_llm = ChatGoogleGenerativeAI(
  #  api_key=os.getenv('GOOGLE_API_KEY'),
model ='gemini-2.5-pro')

# make the retriever

base_ret= vectore_base.as_retriever(search_type='mmr',
                                    search_kwargs={'k':5, 'lambda_mult':0.5})

#multi retriever
multi_q_ret= MultiQueryRetriever.from_llm(
   retriever=base_ret,
   llm=ret_llm
)


# rag prompt 

rag_prompt = ChatPromptTemplate.from_messages([
   ('system', """You are a question answer boat 
    give answer strictly from the given context :
    context: {context}

    rule: if you don't find user query ralated answer from the context say you don't know
   """),

   ('human', "{input}")
])

#llm
grok_llm = ChatOpenAI(
   api_key=os.getenv('XAI_API_KEY'),
   model='grok-3-fast',
   base_url="https://api.x.ai/v1"

)

#document chain
combine_chain = create_stuff_documents_chain(llm=grok_llm, prompt=rag_prompt)

#rag_chain 
rag_chain = create_retrieval_chain(multi_q_ret, combine_chain)

#getting the ans
if query:
   st.spinner("Getting the Answer")
   final_response = rag_chain.invoke({'input': query})
   st.write(final_response['answer'])
