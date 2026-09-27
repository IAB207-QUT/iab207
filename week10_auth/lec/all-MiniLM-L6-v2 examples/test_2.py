# pip install sentence-transformers

from sentence_transformers import SentenceTransformer
# API key not needed as we are running the model locally

# Function to calculate cosine similarity
import numpy as np
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Load embedding model (runs locally)
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# User query
query = "I want something that helps me commute to work"

# Candidate descriptions
items = [
    "Wireless noise-cancelling headphones with long battery life",
    "Compact coffee machine for making espresso at home",
    "Road bicycle for getting around the city"
]

# Embed query
query_embedding = model.encode(query)

# Compare each item's embedding to the query embedding and store the similarity score

results = []

for item in items:
    item_embedding = model.encode(item)

    similarity = cosine_similarity(
        query_embedding,
        item_embedding
    )

    results.append({
        "item": item,
        "similarity": similarity
    })
    
# Rank by similarity (highest first)
results.sort(
    key=lambda x: x["similarity"],
    reverse=True
)

# Display ranked results
print(f"Query: {query}\n")

for rank, result in enumerate(results, start=1):
    print(
        f"{rank}. {result['item']} "
        f"(Similarity: {result['similarity']:.4f})"
    )



