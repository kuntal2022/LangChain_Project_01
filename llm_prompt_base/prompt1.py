import langchain_core
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

prompt_to_get_topic=ChatPromptTemplate.from_messages(
  [('system',"You are a helpful assistant that provides information about various topics.")
    ,('human',"Hi Tell me about {topic} in {explain}")])


count_tokens_prompt=ChatPromptTemplate.from_messages(["human","Count the number of words from the following text {text}"])