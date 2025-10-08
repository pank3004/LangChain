from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field   

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen1.5-1.8B-Chat", 
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

class Person(BaseModel): 
    name: str =Field(description="name of the person")
    age: int = Field(gt=18, descriction="age of the person")
    city: str = Field(description="city of the person lives in" )


parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="give me the name, age and city of a fictional person who live in {place} \n {format_instructions}", 
    input_variables=["place"],
    partial_variables= {'format_instructions': parser.get_format_instructions()}
)

# prompt = template.invoke({"place": "India"})
# result = model.invoke(prompt)
# result_parsed=parser.parse(result.content)

chain = template | model | parser
final_result = chain.invoke({"place": "India"})
print(final_result)

# print(result_parsed)