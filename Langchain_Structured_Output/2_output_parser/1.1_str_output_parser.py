# text --> model --> output --> model --> summary

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen1.5-1.8B-Chat", 
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()


template1=PromptTemplate(
    template="Explain the concept of {topic} ",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="Summarize the following text 3 to 4 lines: {text}",
    input_variables=["text"]
)

chain=template1 | model | parser | template2 | model | parser

result_summarized=chain.invoke({"topic": "Black Hole"})

print("Summarized Text: ", result_summarized)  # don't need to access .content
