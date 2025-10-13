# user topic -->> prompt1 ---> model ---> parser --> prompt2 ---> model ---> parser --> output
# unemployment --> prompt 1 --> report --> parser --> prompt2 ---> summary---> parser --> output
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="generate a detailed report about the {topic}", 
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="summarize the following text in 5 bullet points:\n{text}", 
    input_variables=["text"]
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.3)
parser=StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 
result=chain.invoke({"topic": "cruption in government"})

print(result)

chain.get_graph().print_ascii()  # visualize the chain
