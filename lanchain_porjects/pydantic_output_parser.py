# Importing necessary libraries and modules for the application
import langchain, langchain_core, langchain_openai , os , dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import AzureChatOpenAI, ChatOpenAI, OpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal
import warnings
warnings.filterwarnings("ignore")
from openai import OpenAI as OpenAIClient

# Load environment variables from .env file
load_dotenv()

#LLM Initialization Free
llm =ChatOpenAI()

#base model initialization
class person(BaseModel):
    name: str = Field(...,
        description="Name of the person"
    )
    age : int= Field(...,
        description="Age of the person"
    )

    city: str = Field(
        ...,
        description="City where the person lives"
    )

    sex: str = Field(
        ...,
        description="sex of the person "
    )

    girl_friend: str = Field(
        ...,
        description="Name of the person's girlfriend"
    )


    first_meeting: str = Field(
        ...,
        description="Date of the person and girlfriend first sex day"
    )

parser = PydanticOutputParser(pydantic_object=person)


prompt = PromptTemplate(
    template = 
    """Give me the hindu name, sex, age and british girlfirend name & first meeting date among them of a frictional person \n
    {format_instruction}""",
input_variable =[],
partial_variables = {'format_instruction': parser.get_format_instructions()}
)

chain = prompt | llm | parser

print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print()
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print(chain.invoke({}))
print("FINISHED")
