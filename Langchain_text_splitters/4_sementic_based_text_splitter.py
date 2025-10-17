from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

# Initialize free local embeddings model
# You can use "all-MiniLM-L6-v2" for small + fast performance
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create the semantic chunker using Hugging Face embeddings
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",  # or "percentile"
    breakpoint_threshold_amount=2
)

# Sample text
sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. 
The sun was bright, and the air smelled of earth and fresh grass. 
The Indian Premier League (IPL) is the biggest cricket league in the world. 
People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. 
It causes harm to people and creates fear in cities and villages. 
When such attacks happen, they leave behind pain and sadness. 
To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

# Split semantically
docs = text_splitter.create_documents([sample])

# Print results
print(f"Number of Chunks: {len(docs)}\n")
for i, doc in enumerate(docs, start=1):
    print(f"Chunk {i}:")
    print(doc.page_content)
    print("-" * 50)


# Embeddings are Key: 
    # It uses an embedding model (like one from OpenAI or a local one) to convert each sentence into a list of numbers called a vector or an "embedding." This vector represents the sentence's meaning.

# Measuring Similarity: 
    # It then compares the vector of one sentence to the vector of the next sentence. If the vectors are very similar, it means the sentences are talking about the same thing. It calculates a "similarity score" (often using cosine similarity) between them.

# Finding the Breakpoint: 
    # When it finds two adjacent sentences that have a low similarity score, it sees this as a "semantic breakpoint"—a place where the topic has likely changed. It then creates a split at that point.