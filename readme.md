# Semantic Search Engine

A semantic search engine built using Python, Sentence Transformers, ChromaDB and Streamlit. It allows users to search through text documents based on meaning rather than just keyword matching by converting text into embeddings and retrieving semantically relevant chunks.

## Features

- **Semantic Search:** Finds relevant content based on the meaning of a query rather than exact keyword matches.
- **Document Chunking:** Splits large documents into smaller chunks with configurable chunk size and overlap.
- **Vector Embeddings:** Generates embeddings using `all-MiniLM-L6-v2` from Sentence Transformers.
- **Vector Database:** Stores embeddings, document chunks and metadata using ChromaDB.
- **Top-K Retrieval:** Retrieves the most relevant chunks for a given query.
- **Source Filtering:** Filter search results by document source.
- **Persistent Storage:** Stores embeddings in a persistent ChromaDB database.
- **Search Evaluation:** Evaluates retrieval performance using Precision@K and Recall@K.

## Tech Stack

- Python
- Sentence Transformers
- ChromaDB
- Streamlit

## How It Works

1. Text documents are loaded from the data directory.
2. Documents are split into smaller chunks using a custom chunking function.
3. Each chunk is converted into a numerical embedding using Sentence Transformers.
4. Embeddings, text chunks and metadata are stored in ChromaDB.
5. The user's query is converted into an embedding using the same model.
6. ChromaDB retrieves the most semantically similar chunks.
7. Retrieved results, including source information and similarity distances, are displayed through the Streamlit interface.

## Project Structure

```text
Semantic_Search_Engine/
├── app.py
├── config.py
├── chunking.py
├── ingest.py
├── search.py
├── evaluation.py
├── data/
├── chroma_db/
└── requirements.txt
```

## Installation & Usage

Ingest the documents:

```bash
python ingest.py
```

Run the application:

```bash
streamlit run app.py
```

## Evaluation

Retrieval performance is evaluated using:

- **Precision@K:** Measures how many retrieved results are relevant within the top-K results.
- **Recall@K:** Measures how many of the relevant documents are retrieved within the top-K results.