import langchain_core, pydantic
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
import streamlit as st
import dotenv, os
from dotenv import load_dotenv
load_dotenv()
from llm_prompt_base.llm_base import azure_open_ai_llm as llm , temp , max_tokens, count_string_llm
from llm_prompt_base.prompt1 import prompt_to_get_topic, count_tokens_prompt
from llm_prompt_base.count_string import TokenCount



st.title("Dynamic Prompt Example")
st.subheader("Author- Kuntal")
explain=st.selectbox("Explanation Type", ["Short Explanation", "Detailed Explanation", "Medium Explanation"])
creative=st.selectbox("How Creative?", ["Not Creative", "Somewhat Creative", "Very Creative"])

if explain == "Short Explanation":
    max_tokens = 100
elif explain == "Detailed Explanation":
    max_tokens = 600
else: 
    max_tokens = 200





if creative == "Not Creative":
    temp = 0.2
elif creative == "Somewhat Creative":
    temp = 0.7
elif creative == "Very Creative":
    temp = 1.0
else:
    temp = 0.5

topic = st.chat_input("Ask me about any topic!")







from llm_prompt_base.prompt1 import prompt_to_get_topic

chain = prompt_to_get_topic | llm | StrOutputParser()


if topic:
    text = chain.invoke({"topic": topic, "explain": explain})
    count_chain = count_tokens_prompt | count_string_llm 
    count = count_chain.invoke({"text": text})
    count = count.output_tokens


    st.write("### Response")
    st.write(text)

    st.write("### Token Count")
    st.write(count)