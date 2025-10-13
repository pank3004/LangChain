

#
#                             create quiz
#                      ----------model 2 ------------------
#   user long document                                           model 3
#       of a topic                                          combine both result ----------------output
#                       ------model1----------------------
#                            generate summary of 
#                            of the document
#                                                  
# 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.schema.runnable import RunnableParallel

from dotenv import load_dotenv
load_dotenv()

model1=ChatGoogleGenerativeAI(model="gemini-2.5-pro")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen1.5-1.8B-Chat", 
    task="text-generation"
)

model2=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="generate a notes of the given text \n {text}", 
    input_variables=['text']
)

prompt2=PromptTemplate(
    template="Generate 5 quizs with answer from the given text \n {text}", 
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="Merge the provided notes and the quizs in a single document \n notes-> {notes} and quiz-> {quiz}", 
    input_variables=['notes','quiz']
)

parallel_chain=RunnableParallel({
    'notes': prompt1 | model1 | parser, 
    'quiz': prompt2 | model2 | parser
}
)

merge_chain =  prompt3 | model1 | parser

chain=parallel_chain | merge_chain

with open('logistic_reg.txt', 'r', encoding='utf-8') as f:
    text = f.read()

result=chain.invoke({'text':text})
print(result)


