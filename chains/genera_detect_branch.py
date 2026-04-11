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



st.title("Story Genera Detection 👉 Movies Recomendation ")
st.write("#### Creator : Kuntal")

story=st.chat_input("One Liner Last Story You Read : ")


#base model 
class Genera(BaseModel):
   genera : Literal["Romantic", "Horror", "Comedy", "SciFi", "Action", "Drama", "Thriller", "Animation" ,"Mystery", "Fantasy", "RomCom"] = Field(default='SciFi', description="Genera of the story line given by the user")
   story : str = Field(..., description="The story given by the user")

prompt_story = ChatPromptTemplate([
   ('system', """You are a genera detector from the one line explanation user give"""),
   ('human', "{story}")
])




#branch prompt 



prompt_branch = ChatPromptTemplate.from_messages(
  [
    ('system', """You are a Movie recomender has a vast knowledge of Boolywood and Holywood movies, You should give recomendation based on the genera and story line give by the user 
    
     -strict rule 
     [-Movie recomendation should be ordered by years in desc new movie on top
     - In a table data should come with good visual 
     - Bollywood 5 movies with emojee 
     - Hollywood 5 movies with emojee
     - not more than 50 words 
     
     
     ]
     - format
     [
     -Bolywood
     -bullete points with each 

     -Hollywood
     -bullete points with each 
      ]
     
     
     """),
    ('human', """ the story line is {story} and the genera is {genera} """)

  ]
)





#Structured LLM 
llm=ChatOpenAI(model = 'gpt-5.1')
llm_reco=ChatOpenAI(model = 'gpt-4.1-mini')
llm_struct=llm.with_structured_output(schema=Genera)



#convert to genera dict
convert = RunnableLambda(lambda x: {'genera': x.genera, "story": x.story})


#branch chain 
parser =StrOutputParser()
chain_branch = RunnableBranch(
  (lambda x: x['genera']=="Romantic", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="Horror", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="Comedy", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="SciFi", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="Drama", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="Thriller", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="Animation", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="Mystery", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="Fantasy", prompt_branch | llm_reco | parser ),
  (lambda x: x['genera']=="RomCom", prompt_branch | llm_reco | parser ),
  prompt_branch | llm_reco | parser
)




invoke_param = {'story':story}

chain_struct = prompt_story | llm_struct




if story:
   with st.spinner("Thinking....."):
    genera_result = chain_struct.invoke(invoke_param)
    genera_dict = {"story": genera_result.story, 
                   'genera': genera_result.genera}
    
    
    
    st.write(f"Genera of the Onliner story is : {genera_dict["genera"]}")
    
    response = chain_branch.invoke(genera_dict)
    st.write(f"My recomendation based on your test today ")
    st.write(response)
    



