# text --> model --> output --> model --> summary

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen1.5-1.8B-Chat", 
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template="Explain the concept of {topic} ",
    input_variables=["topic"]
)
prompt1=template1.invoke({"topic": "Black Hole"})
result = model.invoke(prompt1)


template2=PromptTemplate(
    template="Summarize the following text 3 to 4 lines: {text}",
    input_variables=["text"]
)
prompt2=template2.invoke({"text": result.content})
result_summarized = model.invoke(prompt2)

print("Original Text: ", result.content)
print("--------------------------------------------------")
print("Summarized Text: ", result_summarized.content)
