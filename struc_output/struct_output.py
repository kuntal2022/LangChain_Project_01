
from urllib import response

from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import AzureChatOpenAI, ChatOpenAI, OpenAI
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
import streamlit as st
import dotenv, os
from dotenv import load_dotenv
import pydantic
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, Literal
from openai import OpenAI as OpenAIClient
import base64
from io import BytesIO
from PIL import Image

load_dotenv()
from pydantic import BaseModel, Field
from typing import Optional, Literal

class review(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        ..., description="Sentiment of the review"
    )

    category: str = Field(
        default="Not mentioned",
        description="Category of the review"
    )

    key_issue: str = Field(
        default="Not mentioned",
        description="Key issue mentioned in the review"
    )

    urgency: Literal["low", "medium", "high", "None"] | None = Field(
        default="None",
        description="Urgency of the issue"
    )

    recommendation: str = Field(
        default="No recommendation",
        description="Recommended action"
    )

    product_name: str = Field(
        default="Not mentioned",
        description="Product name"
    )

    name: str = Field(
        default="Not mentioned",
        description="Reviewer name"
    )

    good_points: str = Field(
        default="Not mentioned",
        description="Good points"
    )

    bad_points: str = Field(
        default="Not mentioned",
        description="Bad points"
    )


llm =ChatOpenAI(model = 'gpt-4.1')
structured_llm = llm.with_structured_output(schema=review)



st.title("Structured Output Example")
st.subheader("Author- Kuntal")
review_input = st.chat_input("Enter a customer review to analyze:")
st.write("#### Customer Review")
st.write(review_input)

prompt= ChatPromptTemplate.from_messages(
    [('system',"""You are a helpful hotel assistant that analyzes customer reviews and provides insights on sentiment, category, key issues, urgency, and recommendations. recomendation is must no exception. If there is no recommendation, write 'No recommendation'. If any of the other fields are not mentioned in the review, write 'Not mentioned' for that field.\n
    
    strict rule:
      Most Important if any one ask apart from the hotel and resturannt related issue then only provide the response and do not mention about the hotel or restaurant in that case, don't provide any response if the issue is not related to hotel or restaurant. If any one ask abouth other thing say you can't help on that matter strictly.
    """)
     ,('human',"{input}")])

if review_input:
  with st.spinner("Analyzing review..."):
  
    result = structured_llm.invoke( review_input)
    if result.name is None:
      result.name = "Not mentioned"


  st.write("### Analysis Result")
  st.write("**Name:**", result.name)
  st.write("**Sentiment:**", result.sentiment)
  st.write("**Category:**", result.category)
  st.write("**Key Issue:**", result.key_issue)
  st.write("**Urgency:**", result.urgency)
  st.write("**Recommendation:**", result.recommendation)



  if result.sentiment == "negative" and result.urgency in ["high", "medium"]:
    prompt_for_response = ChatPromptTemplate.from_messages(
      [('system',"""You are a hotel customer support agent Mr Benx. A customer has left a review with negative sentiment and medium or high urgency. Please draft a response to address the customer's concerns and offer a solution. The review details are as follows: Sentiment: {sentiment}, Category: {category}, Key Issue: {key_issue}, Urgency: {urgency}, Recommendation: {recommendation}., customer name : Customer
        
      - Rules for drafting response:
      1. Start the response by addressing the customer by their name if mentioned in the review, otherwise start with a general greeting.
      2. Acknowledge the customer's concerns and express empathy for their experience.
      3. Provide a solution or offer assistance based on the key issue and recommendation mentioned in the review.
      4. Keep the response concise and professional.
      5. Most Important if any one ask apart from the hotel and resturannt related issue then only provide the response and do not mention about the hotel or restaurant in that case, don't provide any response if the issue is not related to hotel or restaurant. If any one ask abouth other thing say you can't help on that matter strictly.
        
        """)])


    st.write("### Drafted Response to Customer")
    with st.spinner("Drafting response to customer..."):

      response_chain = prompt_for_response | llm | StrOutputParser()
      st.write(response_chain.invoke({"sentiment": result.sentiment, "category": result.category, "key_issue": result.key_issue, "urgency": result.urgency, "recommendation": result.recommendation}))
      
  else:
    st.write("🥰 Thank you")



   

    
  

