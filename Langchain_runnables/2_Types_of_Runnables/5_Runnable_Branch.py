
# user topic --> prompt1--> model --> parser --> prompt2--> model--> parser-->result

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

prompt1=PromptTemplate(
    template="generate a detailed report about {topic}", 
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="summarize the text \n {text}", 
    input_variables=['text']
)

parser=StrOutputParser()

# report_gen_chain=RunnableSequence(prompt1,model, parser)
           #or
report_gen_chain= prompt1 | model | parser    # LCEL (Langchain expression language)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)), 
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain, branch_chain)

result=final_chain.invoke({'topic': 'Russia vs Ukrain'})
print(result)