from langchain_community.retrievers import WikipediaRetriever
from langchain_core import documents 
import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import dotenv 
dotenv.load_dotenv()

parser = StrOutputParser()
retriever = WikipediaRetriever(lang='en', top_k=1)
prompt= ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant 
     that answers questions based on the retrieved Wikipedia content.
     - Rule
      1. Always use the retrieved content to answer the question.
      2. If the retrieved content does not contain the answer, say "I don't know."
      3. Be concise and accurate in your answers.
      4. Do not include any information that is not present in the retrieved content.
      5. Always give less than 100 words in your answer.
      6. If document is empty, say "I don't know."
      7. Summarize the document if it is bigger than 100 words.
     """),
    ("human", "{query}\n\nBased on the following retrieved content, provide a concise and accurate answer:\n{text}")
])

llm =ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0, max_tokens=100)

st.header("Wikipedia Retriever")
query = st.text_input("Enter your query:")

if query:
    try:
      results = retriever.invoke(query)
      st.write("##Answer:")
      text = results[0].page_content
      chain = prompt | llm | parser
      res=chain.invoke({"query": query, "text": text})
      st.write(res)
    except:
      text = "No content retrieved."
      

    
