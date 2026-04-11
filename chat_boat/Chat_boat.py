import ast
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
import streamlit as st, warnings
warnings.filterwarnings("ignore")

load_dotenv()

FILE_PATH = r"C:\Users\Neel\Desktop\Azure_open_ai\chat_boat\chat_history.txt"




if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
file_path = r"C:\Users\Neel\Desktop\Azure_open_ai\chat_boat\chat_history.txt"

with open(file_path, "r") as f:
    data = f.read()
    chat_history_1= ast.literal_eval(data.replace("chat_history = ", "").strip())
    st.session_state.chat_history.extend(chat_history_1)


# display the old chat
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.write(message['content'])


input_qst = st.chat_input("How can I help Today!")

prompt =ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant.'),
     MessagesPlaceholder(variable_name="chat_history"),
     ('human', "{input_qst}")])

llm=ChatOpenAI()

def save_history(history):
    with open(FILE_PATH, "w") as f:
        f.write("chat_history = " + str(history))

save_history(st.session_state.chat_history)


if input_qst:
    chain = prompt | llm | StrOutputParser()
    st.session_state.chat_history.append(
    {"role": "user", "content": input_qst}
)
    response = chain.invoke({"input_qst": input_qst, "chat_history": st.session_state.chat_history})

    st.session_state.chat_history.append(
    {"role": "assistant", "content": response}
)
    save_history(st.session_state.chat_history)
    print(response)
    
    
     

    