import dotenv, os
dotenv.load_dotenv()

from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

parser1=StrOutputParser()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    temperature=0.7,
    max_completion_tokens=100
)


# llm= ChatOpenAI()

prompt = ChatPromptTemplate(['human',"Hi Tell me about {topic}"])


chain = prompt | llm | parser1

print(chain.invoke({"topic":"Azure OpenAI"}))

