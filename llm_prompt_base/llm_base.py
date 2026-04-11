
import langchain, langchain_core, langchain_openai , os , dotenv
from langchain_openai import AzureChatOpenAI, ChatOpenAI, OpenAI

from dotenv import load_dotenv
from  llm_prompt_base import count_string
load_dotenv()
max_tokens=100
temp = 0

azure_open_ai_llm=AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    temperature=temp,
    max_completion_tokens=max_tokens)



count_string_llm = ChatOpenAI()
count_string_llm=count_string_llm.with_structured_output(schema=count_string.TokenCount)


