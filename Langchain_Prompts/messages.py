from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.5)

messages=[
    SystemMessage(content="You are a helpful assistant that translates English to hindi."),
    HumanMessage(content="Translate the following English text to Hindi: 'Hello, how are you?'")
]
response=model.invoke(messages)
messages.append(AIMessage(content=response.content))

print(messages)