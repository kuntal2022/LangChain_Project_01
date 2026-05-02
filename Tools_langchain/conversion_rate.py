#streamlit start
import streamlit as st
from currencyList import cur_list

st.set_page_config(
    page_title="AI Model Currency Conversion-App/Kuntal",
    page_icon="💰",
    layout="wide"
)




st.header("Currency Conversion-App")
st.write(f"### Author - Kuntal")
base_currency = st.selectbox("From which Currency You Wish to Convert", cur_list)
target_currency = st.selectbox("To which Currency You Wish to Convert", cur_list)
base_currency_value=float(st.number_input("How much you to Convert ?"))





# Import Libraries 
from langchain_community.tools import tool , BaseTool
from pydantic import BaseModel, Field
from typing import Type, Annotated
import requests, os, io , json

from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.prompts import *
from langchain_core.messages import *
from langchain_openai import ChatOpenAI
load_dotenv()


llm = ChatGroq(model="llama-3.3-70b-versatile")

# InjectedToolArg
from langchain_core.tools import InjectedToolArg

CURRENCY_API='3f3c11c5b652bf8a1a695a2c'


#with @ method tool conversion rate
@tool 

def get_conversion_factor(base_currency: str = base_currency, target_currency: str = target_currency, api_key: str = CURRENCY_API) ->  float:

  """
  This function fetch the currency conversion factor b/w a given base currency and target currency
  """
  url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_API}/pair/{base_currency}/{target_currency}"

  response=requests.get(url)

  return response.json()



#2nd tool multiplication with InjectedGetArg

@tool
def multiply_tool(conversion_rate : Annotated[float, InjectedToolArg], base_currency_value : float = base_currency_value) -> float:
  
  """ 
  This function returns the value by multiplying the conversion rate with base currency value 
  """

  return base_currency_value * conversion_rate


# tool binding 
llm_with_tool=llm.bind_tools([multiply_tool, get_conversion_factor])

if base_currency_value and base_currency and target_currency:
  with st.spinner("Working......!"):

    #Get the query 
    query = f"""What is the conversion rate between {base_currency} and {target_currency}, 
    and what is the value of {base_currency_value} to the {target_currency}
    """

    
    msg_list=[HumanMessage(query)]

    #First tool call 
    ai_msg=llm_with_tool.invoke(msg_list)
    msg_list.append(ai_msg)
    tool_calls=ai_msg.tool_calls
    #first tool execution 

    for tool_call in tool_calls:
      if tool_call['name']=="get_conversion_factor":
        tool_msg1= get_conversion_factor.invoke(tool_call)
        conversion_rate = json.loads(tool_msg1.content)['conversion_rate']
        msg_list.append(tool_msg1)

      if tool_call['name']=="multiply_tool":
        tool_call['args']["conversion_rate"]=conversion_rate
        tool_msg2=multiply_tool.invoke(tool_call)
        msg_list.append(tool_msg2)

    final_cal = llm_with_tool.invoke(msg_list)
    final_ans = final_cal.content

    st.markdown(
    f"""
    <div style="
        padding: 20px;
        border-radius: 10px;
        background-color: #0b3d91;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #ffd700;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    ">
        {final_ans}
    </div>
    """,
    unsafe_allow_html=True
)


