# user feedback--> prompt1...........model
#                                classify(pos or neg)
#                                   |
#                                 parser
#                                  .
#                                 .   .
#                               .       .
#                            .            .
#                         .                  .
#                     if positive        if negetive
#                       |                     |       
#                      prompt2             prompt3
#                       |                     |
#                      model                model
#                       |                     |
#                      parser               parser

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from typing import Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-pro')
parser1=StrOutputParser()

class Feedback(BaseModel): 
    sentiment: Literal['Positive', 'Negative'] = Field(description="generate the sentiment ")

parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain= prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback in 1 -2 lines\n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback in 1-2 lines \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser1),
    (lambda x:x.sentiment == 'Negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)


chain = classifier_chain | branch_chain

result=chain.invoke({'feedback': 'the quality of this phone is bad'})
print(result)
#chain.get_graph().print_ascii()