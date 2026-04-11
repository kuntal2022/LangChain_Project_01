import dotenv
import ast 
import os, langchain, langchain_core 
from langchain_core.prompts import * 
from langchain_openai import * 
from dotenv import load_dotenv
from langchain_core.output_parsers import *
load_dotenv()

file_path =r"C:\Users\Neel\Desktop\Azure_open_ai\chat_boat\chat_history.txt"
chat_history=[]

with open(file_path, 'r') as f:
  data = f.read()
  data=data.replace("chat_history = ","" )
  chat_history.extend(ast.literal_eval(data))
  
input_q= input("How can I help you today ?")

prompt=ChatPromptTemplate.from_messages(
  [
    ('system', 'you are an help full assistant'), 
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', input_q)
  ]
)
chat_history.extend(prompt)
llm=ChatOpenAI()

chain = prompt | llm | StrOutputParser()

invoke_param = {"chat_history": chat_history, "input_q":input_q}
response = chain.invoke(invoke_param)
chat_history.extend([{"role": "assistant", "content":response}])
print(response)