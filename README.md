# Dev Onboard AI

Dev Onboard AI is an AI-powered developer onboarding assistant designed to help developers understand unfamiliar codebases faster.

The system processes software repositories by discovering relevant files, filtering unnecessary content, reading source code, splitting it into meaningful chunks, and generating vector embeddings for semantic retrieval.

> 🚧 This project is currently under active development.

## 🎯 Problem

Developers joining an existing project often spend significant time understanding:

- Project structure
- Important files and modules
- Existing architecture
- Relationships between different parts of the codebase
- Where specific functionality is implemented

Dev Onboard AI aims to reduce this onboarding time by creating an intelligent knowledge layer over a software repository.

## ⚙️ Current Pipeline

Repository
↓
File Discovery
↓
File Filtering
↓
File Reading
↓
Code Chunking
↓
Embedding Generation
↓
Semantic Retrieval

## 📁 Current Project Structure

backend/
├── app/
│   ├── ingestion/
│   │   ├── chunker.py
│   │   ├── file_discovery.py
│   │   ├── file_filter.py
│   │   ├── file_reader.py
│   │   └── repository_fetcher.py
│   │
│   ├── retrieval/
│   │   └── embedding_service.py
│   │
│   ├── test_embedding.py
│   └── test_ingestion.py
│
└── .gitignore

## ✅ Currently Implemented

- Repository/file discovery
- File filtering
- Source file reading
- Content chunking
- Embedding generation
- Initial ingestion testing
- Embedding testing

## 🚀 Planned Features

- Vector storage
- Semantic code search
- Retrieval pipeline
- Question answering over repository context
- Backend API
- Improved automated tests
- Developer-friendly interface

## 🛠️ Tech Stack

- Python
- Vector Embeddings
- Git & GitHub

Additional technologies will be documented as they are integrated.

## 🧪 Development Status

The project is currently in active development.

The ingestion and embedding layers are being built first, followed by retrieval and API capabilities.

## 🎯 Project Goal

The long-term goal is to allow a developer to provide a repository and ask questions such as:

- "Where is authentication implemented?"
- "How does this project connect to the database?"
- "Which files handle API requests?"
- "Explain the architecture of this repository."

The system should retrieve relevant code context and provide grounded answers based on the repository.
