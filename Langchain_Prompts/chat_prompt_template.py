from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert.'),
    ('human', 'explain the concept of {concept} in a simple manner')
])

prompt=chat_template.invoke({'domain':'AI', 'concept':'transformers'})

print(prompt)