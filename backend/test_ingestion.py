from pprint import pprint
from app.ingestion.repository_fetcher import clone_repository
from app.ingestion.file_discovery import discover_files
from app.ingestion.file_filter import filter_files
from app.ingestion.file_reader import read_file
from app.ingestion.chunker import chunk_file
from app.retrieval.embedding_service import generate_embeddings

# Clone repository
repo = clone_repository(
    "https://github.com/Prajwl-hash/FstAPI.git"
)

# Discover files
files = discover_files(repo)

# Filter useful files
filtered_files = filter_files(files)

# Read files
processed_files = []

for file_path in filtered_files:
    file_data = read_file(file_path, repo)
    processed_files.append(file_data)

# Create chunks
all_chunks = []

for file_data in processed_files:
    chunks = chunk_file(file_data)
    all_chunks.extend(chunks)

print(f"\nTotal chunks created: {len(all_chunks)}")


# -----------------------------------
# EMBEDDINGS START HERE
# -----------------------------------
embedded_chunks = generate_embeddings(all_chunks)

print("\nEmbedding Summary:")

for chunk in embedded_chunks:
    print(
        f'{chunk["metadata"]["file_path"]} | '
        f'Chunk: {chunk["metadata"]["chunk_index"]} | '
        f'Dimensions: {len(chunk["embedding"])}'
    )