from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Create Gemini embedding instance
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", dimensions=32)

# Example query
text = "Delhi is the capital of India"
result = embeddings.embed_query(text)

print(result)
