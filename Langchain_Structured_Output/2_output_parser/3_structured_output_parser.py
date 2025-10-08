from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen1.5-1.8B-Chat',
    task='text-generation',
)
model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact_1', description='fact_1 about the topic'),
    ResponseSchema(name='fact_2', description='fact_2 about the topic'),
    ResponseSchema(name='fact_3', description='fact_3 about the topic'),
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give me 3 interesting facts about {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt=template.invoke({"topic": "Black Hole"})

result=model.invoke(prompt)
result_parsed=parser.parse(result.content)
print(result_parsed)

