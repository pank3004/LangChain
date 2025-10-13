from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

prompt1=PromptTemplate(
    template="generate a tweet about {topic}", 
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Generate Linkedin post about {topic}", 
    input_variables=['topic']
)

parser=StrOutputParser()

chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1, model,parser), 
    'linkedin':RunnableSequence(prompt2, model, parser)
})

result=chain.invoke({'topic':'AI'})


print(result)

print(result['tweet'])
print(result['linkedin'])