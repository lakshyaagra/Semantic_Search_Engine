from config import model, collection

def semantic_search(query, top_k=3, source=None):

    if not query.strip():
        return []

    if collection.count() == 0:
        return []

    query_embedding = model.encode([query]).tolist()

    search_args = {
        "query_embeddings": query_embedding,
        "n_results": min(top_k, collection.count()),
        "include": [
            "documents",
            "metadatas",
            "distances"
        ]
    }

    if source and source != "All":  # Streamlit UI mai filters mai default ALL hai na
        search_args["where"] = {
            "source": source
        }

    results = collection.query(**search_args)

    matches = []

    for i in range(len(results["ids"][0])):

        matches.append({
            "id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return matches