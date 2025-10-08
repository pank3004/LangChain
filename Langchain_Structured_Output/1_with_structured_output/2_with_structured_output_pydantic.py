from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field


load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)

class Review(BaseModel): 
    key_themes: list[str]=Field(description="The main themes discussed in the review")
    summary: str=Field(description="A brief summary of the review in 1-2 sentences")
    sentiment: Literal['Pos', 'Neg', 'neu']=Field(description="The overall sentiment of the review, either positive, negative, or neutral")
    pros: Optional[list[str]]=Field(default=None, description="A list of positive aspects mentioned in the review")
    cons: Optional[list[str]]=Field(default=None, description="A list of negative aspects mentioned in the review")

  
structured_model=model.with_structured_output(Review)

response=structured_model.invoke('''
                                The new Pixel 9 Pro is an impressive phone. The camera captures stunning photos in any lighting, 
                                 and the performance is buttery smooth. However, the battery drains faster than expected when gaming,
                                  and it heats up a bit. The design looks premium and feels solid in hand. 
                                 Overall, it’s a great choice for photography lovers but not ideal for heavy gamers.
                                ''')

print(response)
print(response.sentiment)
