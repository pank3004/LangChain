from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-pro')


url='https://www.flipkart.com/vivo-t4-5g-emerald-blaze-128-gb/p/itmc2634fd4daeb9'

loader=WebBaseLoader(url)

docs=loader.load()

#print(docs[0].page_content)

parser=StrOutputParser()

prompt=PromptTemplate(
    template="give the answer of the question {question} based on the following text  \n {text}",
    input_variables=['question','text']
)

chain=prompt | model | parser

ans=chain.invoke({'question':'what is the collour of the phone ', 'text':docs[0].page_content})

print(ans)