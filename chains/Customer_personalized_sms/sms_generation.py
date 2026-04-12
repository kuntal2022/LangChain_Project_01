import langchain, langchain_core, pandas as pd, numpy as np, dotenv, streamlit as st 
from dotenv import load_dotenv
from pydantic import Field, BaseModel
from typing import Literal, List, Annotated
import pandas as pd, numpy as np, streamlit as st
from langchain_openai import * 
from langchain_core.prompts import * 
from langchain_core.output_parsers import *  
from langchain_core.runnables import *
from time import sleep 

load_dotenv()
st.title("Personalized SMS Generation ")
st.write("#### Creator - Kuntal", )
# File Upload
uploaded_file=st.file_uploader("Upload CSV", type=['csv'])



# Schema
class CustSegment(BaseModel):
  rfm : Literal["Lost", "Champion", "At_Risk"]=Field(...,description="Customer RFM segment")





#llm creation 
llm=ChatOpenAI(temperature=0.8, model='gpt-4.1')
llm1=ChatOpenAI(temperature=0)
llm_struct = llm1.with_structured_output(schema=CustSegment)



#Lost risk  prompt
prompt_lost_risk = ChatPromptTemplate.from_messages(
  [('system', """You are a Personalized Campgain's SMS creator based on the segment given by the user for   Tufan-X Appral company, Your name is TufBoat.
    You handel customer only at_risk and lost
    -Strict Rule don't ignore 
    - Don't offer more than 60% for specific appral products  lost customers and 50% for at_risk customers
    - Don't offer anyhting unrelastic which is not correct 
    - Strat with some exciting welcome and also say we missed them 
    
    
    """), 
    ('human', 'Create the SMS for the segment {segment} for the RFM {rfm}')]
)



#Champion prompt
prompt_champ = ChatPromptTemplate.from_messages(
  [('system', """You are a Personalized Campgain's SMS creator based on the segment given by the user for Tufan-X Appral company, Your name is TufBoat.
    You handel customer only Champion 
    -Strict Rule don't ignore 
    - offer them 20% if  purchase >=3000/-, 30% if purchase >=5000/-, 50% if purchase >=10,000/- 
    - Don't offer anyhting unrelastic which is not correct 
    
    """), 
    ('human', 'Create the SMS for the segment {segment} for the RFM {rfm}')]
)


# Structural prompt
prompt_struct = ChatPromptTemplate.from_messages(
  [
    ('system', """See the segment given by the user and get the right rfm from"""),
    ('human', '{rfm}')
  ]
)
#parser
parser =StrOutputParser()

#branch
chain_branch = RunnableBranch(
  (lambda x : x['rfm'] in ["Lost", "At_Risk"], prompt_lost_risk | llm | parser)
  ,(lambda x : x['rfm'] =="Champion", prompt_champ | llm | parser)
  ,RunnablePassthrough()
)

button=st.button("GO")

results=[]

if button:
  st.success("✅ File Uplode Successful")
  with st.spinner("Creating SMS"):
    customer = pd.read_csv(uploaded_file)
    customer['National_Vintage_CustomerBucket_RFM']=customer["Nationality"]+", "+customer["Vintage"]+", "+customer['Customer_Bucket']+", "+customer["RFM_Segment"]
    data_for_sms=customer[["National_Vintage_CustomerBucket_RFM", "RFM_Segment"]].drop_duplicates().head(5)

    sms_dict={}
    for i, row in data_for_sms.iterrows():
      sleep(1)
      sms_dict['rfm']=row['RFM_Segment']
      sms_dict['segment']=row['National_Vintage_CustomerBucket_RFM']
      struct_chain = prompt_struct | llm_struct 
      strut_response = struct_chain.invoke(sms_dict['rfm'])

      response = chain_branch.invoke({'rfm':strut_response.rfm,
                                      "segment":sms_dict['segment'] })
      
      results.append({
        "segment":sms_dict['segment'], 
        "rfm":strut_response.rfm,
        "SMS": response
      })
      st.write(f"####✅SMS Creation for {i+1} combination is done")
df=pd.DataFrame(results)
st.dataframe(df)
      

      
      

      
      
      
      
      




      
      


    




