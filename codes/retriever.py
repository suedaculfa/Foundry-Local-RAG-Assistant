import numpy as np

from config import embedding_model, TOP_K
from database import Database


class Retriever:

    def __init__(self):
        self.db = Database()

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, question):

        question_embedding = embedding_model.encode(
            question,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        documents = self.db.get_all_chunks()

        results = []

        for doc in documents:

            score = self.cosine_similarity(
                question_embedding,
                doc["embedding"]
            )

            results.append(
            {
                "source": doc["source"],
                "chunk_id": doc["chunk_id"],
                "chunk": doc["chunk"],
                "score": float(score)
            }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        if not results:
                    return []
        
        if results[0]["score"] < 0.83:
            return []
        
        return results[:TOP_K]


if __name__ == "__main__":

    retriever = Retriever()

    while True:

        question = input("\nQuestion : ")

        if question.lower() == "exit":
            break

        answers = retriever.search(question)

        for item in answers:

            print("=" * 60)
            print("Source:", item["source"])
            print("Score :", round(item["score"], 3))
            print()
            print(item["chunk"])