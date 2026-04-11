import langchain, langchain_core, os, io, streamlit as st, pandas as pd, numpy as np 
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate, PromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnableBranch, RunnablePassthrough, RunnableParallel
from langchain_openai import * 
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import *
from pydantic import BaseModel, Field 
from typing import List, Literal, Optional, Annotated, TypedDict


# Project Idea 
# We will analyse a the mood of the person and based on that we will give response 

st.title("Mood Dectector Through Emojee")
st.write("Creator : Kuntal")

mood=st.chat_input("Give The Mood Emojee :")

# Pydantic class 
class Mood(BaseModel):
  mood_decode: Literal["Happy", "Sad", "Angry", "Other"]= Field(default="Other",description= """The mood of the user""") 



# mood may be happy, sad, angry 
# Prompt
#mood detection
prompt_mood_detection = ChatPromptTemplate.from_messages([
    ('system', """You are a mood detector.
     Analyze the user message and detect the mood.
     Reply with ONLY one word from these options: Happy, Sad, Angry, Other
     Do not say anything else. Just one word."""),
    ('human', '{mood}')
])


#Angry Prompt 
prompt_angry = ChatPromptTemplate.from_messages(
  [
    ('system', """You are the assitant who reponses the user who has angry mood /n
      to cool down"""),
      ('human', "{mood_decode}")
  ]
)

#Happy Prompt 
prompt_happy = ChatPromptTemplate.from_messages(
  [
    ('system', """You are the assitant who response the user who has happy mood
     """),
     ('human', "{mood_decode}")
  ]
)

#Sad Prompt 
prompt_sad = ChatPromptTemplate.from_messages(
  [
    ('system', """You are the assitant who response the user who has sad mood to console them"""),
    ('human', "{mood_decode}")
  ]
)

#llms
llm_mood_detector = ChatOpenAI(model = 'gpt-3.5-turbo')
llm_mood_detector_struct=llm_mood_detector.with_structured_output(schema=Mood)
llm_reply=ChatOpenAI(model = 'gpt-4.1-mini')

#covert 
convert= RunnableLambda(lambda x : {"mood_decode": x.mood_decode})



#parser
parser =StrOutputParser()

chain_branch = RunnableBranch(
  (lambda x : x['mood_decode']=="Happy", prompt_happy | llm_reply | parser
   ),
   (lambda x : x['mood_decode']=="Angry", prompt_angry | llm_reply | parser
   ),
    (lambda x : x['mood_decode']=="Sad", prompt_sad | llm_reply | parser
   ),
   RunnablePassthrough()
)


expression_chain = prompt_mood_detection | llm_mood_detector_struct



if mood:
  with st.spinner("Thinking"):
  # mood_detection_chain
    chain_mood_detection = prompt_mood_detection | llm_mood_detector_struct | convert | chain_branch

    invoke_param = {"mood": mood}
    expresion = expression_chain.invoke(invoke_param)


    response=chain_mood_detection.invoke(invoke_param)
    st.write(f"The User is in {expresion.mood_decode}")
    st.write(response)



