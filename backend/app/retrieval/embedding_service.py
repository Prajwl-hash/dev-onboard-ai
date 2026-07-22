from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text):
    embedding = model.encode(text)
    return embedding


def generate_embeddings(chunks):
    embedded_chunks = []

    for chunk in chunks:
        embedding = generate_embedding(chunk["content"])

        embedded_chunk = {
            "content": chunk["content"],
            "metadata": chunk["metadata"],
            "embedding": embedding
        }

        embedded_chunks.append(embedded_chunk)

    return embedded_chunks