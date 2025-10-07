from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.5)

#chat_history=[]

# while True:
#     user_input=input("You: ")
#     chat_history.append({"role":"user", "content":user_input})
#     if user_input=="exit":
#         break   
#     response=model.invoke(chat_history)
#     chat_history.append({"role":"assistant", "content":response.content})
#     print("AI:", response.content)

chat_history=[
    SystemMessage(content="You are a helpful assistant")
]
while True:
    user_input=input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break   
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI:", response.content)

print("chat_history:", chat_history)