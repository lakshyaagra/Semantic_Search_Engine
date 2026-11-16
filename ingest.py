from pathlib import Path

from config import model, collection
from chunking import chunk_text

DATA_DIR = Path("./data")

def ingest_documents():

    all_ids = []
    all_documents = []
    all_embeddings = []
    all_metadatas = []

    for file_path in DATA_DIR.glob("*.txt"):

        text = file_path.read_text(encoding="utf-8")

        chunks = chunk_text(
            text,
            chunk_size=100,
            overlap=20
        )

        embeddings = model.encode(chunks).tolist()

        for i, chunk in enumerate(chunks):

            chunk_id = f"{file_path.stem}_{i}"

            all_ids.append(chunk_id)
            all_documents.append(chunk)
            all_embeddings.append(embeddings[i])

            all_metadatas.append({
                "source": file_path.name,
                "chunk_index": i,
                "file_type": "txt"
            })

    if all_ids:
        collection.upsert(
            ids=all_ids,
            documents=all_documents,
            embeddings=all_embeddings,
            metadatas=all_metadatas
        )

    print("Ingestion completed!")
    print("Total stored chunks:", collection.count())

if __name__ == "__main__":
    ingest_documents()