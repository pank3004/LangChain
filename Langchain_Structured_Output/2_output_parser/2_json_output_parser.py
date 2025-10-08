from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen1.5-1.8B-Chat',
    task='text-generation',
)
model=ChatHuggingFace(llm=llm)
parser=JsonOutputParser()


template=PromptTemplate(
    template="give me the name, age and city of a fictional perison \n {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# prompt=template.format()
# result=model.invoke(prompt)
# result_parsed=parser.parse(result.content)

chain=template | model | parser
result=chain.invoke({})

print(result)