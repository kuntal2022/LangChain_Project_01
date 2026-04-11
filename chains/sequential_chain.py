import langchain, langchain_core, pandas as pd, numpy as np, os, pydantic, streamlit as st
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, ChatMessagePromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from dotenv import load_dotenv 
from langchain_openai import *
import time
from time import sleep

#load the keys
load_dotenv()

#mention headers 
st.header("Example of Sequntial Chain")
st.subheader("#### Author : Kuntal")

#get the topic 
topic=st.chat_input("Tell me which Topic?")

#inititate the llm 
llm_explain =ChatOpenAI(model = 'gpt-4o-mini', temperature=0.7, api_key=os.getenv("OPENAI_API_KEY")
                , max_completion_tokens=500)
llm_summary =ChatOpenAI(model = 'gpt-4.1', temperature=0.7, api_key=os.getenv("OPENAI_API_KEY")
                , max_completion_tokens=100)

#prompt to explain the topic 
explain_prompt = ChatPromptTemplate.from_messages(
  [
    ('system', """You are a helpful assistant who explains the topic \n {topic} --rule -[strictly in english -no abusive language]""")
  ]
)

summary_prompt= ChatPromptTemplate.from_messages([
  ('system', """you are the summary writer make the summary of the text \n {text}""" )
])

#parser
parser = StrOutputParser()

# Sequential Chain
chain = explain_prompt | llm_explain | parser | summary_prompt | llm_summary | parser 

invoke_param = {'topic': topic}


if topic:
  with st.spinner("Thinking"):
    response =chain.invoke(invoke_param)
    st.write(response)
    

    









