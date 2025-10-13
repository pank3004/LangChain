  # user topic -->> prompt ---> model ---> parser --> output

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.5)

prompt=PromptTemplate(
    template="Generate 5 interesting facts about the {topic}", 
    input_variables=["topic"]
)

parser=StrOutputParser()


chain =prompt | model | parser

# without chain: 
# prompt=prompt.format(topic="space")
# response=model.invoke(prompt)                        # response.content==result in this case
# result=parser.parse(response.content)
# print(result)

response = chain.invoke({"topic": "sex"})
print(response)


chain.get_graph().print_ascii()  # visualize the chain