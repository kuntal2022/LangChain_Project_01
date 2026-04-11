import streamlit as st, os, dotenv
from pydantic import BaseModel, Field
from langchain_core import prompts, output_parsers
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from typing import Optional, Literal, Dict, List
from dotenv import load_dotenv
load_dotenv()

st.title("Structured Output Example")
st.subheader("Author- Kuntal")
input_review=st.text_input("Enter a customer review to analyze", key="input_review")
# base model 
class review(BaseModel):
  Sentiment : Literal[1,0,-1]=Field(..., description="Sentiment of the review")
  Category: Literal["Delivery", "Product Quality", "Customer Service", "Other"] = Field(..., description="Category of the review")
  Key_issue: str = Field(..., description="Key issue mentioned in the review")
  Urgency: Literal["Low", "Medium", "High"] = Field(..., description="Urgency of the issue")
  
llm = ChatOpenAI()
llm_struct= llm.with_structured_output(schema=review)

prompts = ChatPromptTemplate.from_messages(
  [('system', 'You are a helpful assistant for analyzing customer reviews.'),
   ('human', "Analyze the senetence and give the sentiment, category, key issue and urgency of the review. \n Review: {review}")]
)


if input_review:
  st.spinner("Analyzing the review...")
  chain = prompts | llm_struct
  response = chain.invoke(input_review)
  st.write(response)
