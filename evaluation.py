from config import collection, model
# print(collection.get()["ids"])

evaluation_data = [
    {
        "query": "What is Python?",
        "relevant_ids": ["python_0"]
    },
    {
        "query": "What is supervised learning?",
        "relevant_ids": ["machine_learning_0"]
    },
    {
        "query": "What is a relational database?",
        "relevant_ids": ["databases_0"]
    }
]

def retrieve_ids(query, top_k=1):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["ids"][0]


def precision_at_k(retrieved_ids, relevant_ids, k):
    if k <= 0:
        raise ValueError("k must be positive")
    
    top_results = retrieved_ids[:k]

    if not top_results:
        return 0.0

    relevant_found = sum(
        doc_id in relevant_ids
        for doc_id in top_results
    )

    return relevant_found / len(top_results)


def recall_at_k(retrieved_ids, relevant_ids, k):
    if not relevant_ids:
        return 0.0

    top_results = retrieved_ids[:k]

    relevant_found = sum(
        doc_id in relevant_ids
        for doc_id in top_results
    )

    return relevant_found / len(relevant_ids)

if __name__ == "__main__":

    for k in [1,2,3]:
        precision_scores = []
        recall_scores = []

        print(f"\n========== TOP {k} EVALUATION ==========")

        for item in evaluation_data:

            query = item["query"]
            relevant_ids = set(item["relevant_ids"])

            retrieved_ids = retrieve_ids(query, top_k=k)

            precision = precision_at_k(
                retrieved_ids,
                relevant_ids,
                k
            )

            recall = recall_at_k(
                retrieved_ids,
                relevant_ids,
                k
            )
            precision_scores.append(precision)
            recall_scores.append(recall)

            avg_precision = sum(precision_scores) / len(precision_scores)
            avg_recall = sum(recall_scores) / len(recall_scores)

            print("\nQuery:", query)
            print("Retrieved IDs:", retrieved_ids)
            print("Expected IDs:", relevant_ids)
            print("Precision@3:", round(precision, 2))
            print("Recall@3:", round(recall, 2))
            print("\n--- Overall Evaluation ---")
        print("Average Precision:", round(avg_precision, 2))
        print("Average Recall:", round(avg_recall, 2))