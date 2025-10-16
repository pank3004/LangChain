from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-pro')

loader=TextLoader("cricket.txt", encoding='utf-8')
docs=loader.load()


print(docs)

print(docs[0])  # document
print(docs[0].page_content)  # actual text
print(docs[0].metadata)


print(type(docs))  # list
print(type(docs[0]))  # langchain document
print(type(docs[0].page_content))   # str
print(type(docs[0].metadata))  # dict


parser=StrOutputParser()

prompt=PromptTemplate(
    template="Summarize the poem \n {text}",
    input_variables=['text']
)

chain= prompt | model | parser

result=chain.invoke({'text': docs[0].page_content})

print(result)

