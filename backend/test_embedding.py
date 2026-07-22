from app.retrieval.embedding_service import generate_embedding


text = "How do I run this FastAPI application?"

embedding = generate_embedding(text)

# print(embedding)
print("Vector dimensions:", len(embedding))