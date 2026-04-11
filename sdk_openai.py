import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
st.title("OpenAI SDK Example")
st.write("Author : - Kuntal")

question = st.text_input("Ask a question to OpenAI:")

if question:
    client = OpenAI()
    with st.spinner("Generating response..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
                  max_tokens = 100
                  ,temperature=1)
    st.write(response.choices[0].message.content)