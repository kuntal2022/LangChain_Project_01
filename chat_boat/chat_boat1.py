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
  



llm=ChatOpenAI()

input_q=""
while input_q !="exit":
  input_q= input("How can I help you today ?")
  chat_history.append({"role": "user", "content": input_q})
  
  prompt=ChatPromptTemplate.from_messages(
  [
    ('system', 'you are an help full assistant you help customer with hisproblem and also refer the chat_history {chat_history}'), 
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', input_q)
  ]
)
  chain = prompt | llm | StrOutputParser()


  invoke_param = {"chat_history": chat_history, "input_q":input_q}
  response = chain.invoke(invoke_param)
  chat_history.append({"role": "assistant", "content": response})
  with open(file_path, 'w') as f:
      f.write("chat_history = " + str(chat_history))
  print(response)



