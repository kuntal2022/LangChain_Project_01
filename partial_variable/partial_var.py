import datetime

import streamlit as st, os, dotenv
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel, Field
from langchain_core import prompts, output_parsers
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from typing import Optional, Literal, Dict, List
import pandas as pd 



llm=ChatOpenAI()


class Person(BaseModel):
    Name: str = Field(..., description="Name of the person")
    Age: int = Field(..., description="Age of the person")
    City: str = Field(..., description="City where the person lives")
    DOB: str = Field(..., description="DOB of the person")
    Job: str = Field(..., description="Job of the person")

    

st.header("Partial Variable Example")
st.subheader("Author- Kuntal")
input_qst = st.chat_input("""Ask me about a person and I will give you the name, age and city, DOB, job !""")


parser = PydanticOutputParser(pydantic_object=Person)

prompt = PromptTemplate(
    template = """Give me the name, age and city, dob and job of a  person {input_qst} \n
{format_instruction}""",
input_variable = ["input_qst"],
partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = prompt | llm | parser


if input_qst:
   response = chain.invoke({'input_qst': input_qst})
   df=pd.DataFrame([response.dict()])


   st.write(df)

   