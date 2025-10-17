

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

prompt1=PromptTemplate(
    template="generate a joke about {topic} in 1 - 2 line", 
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Explain the joke in 3 - 4 lines \n {text}", 
    input_variables=['text']
)

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt1, model, parser)
def word_count(text): 
    text=text.split()
    return len(text)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(), 
    'explanation':RunnableSequence(prompt2, model, parser), 
    'count': RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_gen_chain, parallel_chain)

result=final_chain.invoke({'topic': 'AI'})

print(result)