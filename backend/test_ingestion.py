from pprint import pprint
from app.ingestion.repository_fetcher import clone_repository
from app.ingestion.file_discovery import discover_files
from app.ingestion.file_filter import filter_files
from app.ingestion.file_reader import read_file
from app.ingestion.chunker import chunk_file

repo = clone_repository(
    "https://github.com/Prajwl-hash/FstAPI.git"
)
# discover
files = discover_files(repo)

# filter 
filtered_files = filter_files(files)

# read
processed_file =[]

for file in filtered_files:
    file_data =read_file(file,repo)
    processed_file.append(file_data)
    
for file_data in processed_file:
    pprint({
        "file_path": file_data["file_path"],
        "extension": file_data["extension"],
        "content_preview": file_data["content"][:100]
    })
    
all_chunks = []

for file_data in processed_file:
    chunks = chunk_file(file_data)
    all_chunks.extend(chunks)

print(f"\nTotal chunks created: {len(all_chunks)}")

for chunk in all_chunks:
    pprint(chunk)