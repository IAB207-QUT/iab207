# pip install sentence-transformers

from sentence_transformers import SentenceTransformer
# API key not needed as we are running the model locally

# Load embedding model (runs locally)
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Embed a string as a vector
embedding = model.encode(
    "I want something that helps me listen to music on my daily commute to work"
)

# Print the vector to see if it worked
print(embedding)
print(f"Vector size: {len(embedding)}")

