from datetime import datetime

from retriever import Retriever
from llm import LLM


retriever = Retriever()
llm = LLM()


# ------------------------------------
# Test Cases
# ------------------------------------
tests = [

    {
        "question": "What is RAG?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "What is Foundry Local?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "What are the key features of SQLite?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "What are the differences between Cloud models and Local models?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "How can we avoid Chunk Overlap?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "Why do we use SQLite in this project?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "What are the best practices with Local LLMs to achieve good performance?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "How does Foundry Local work?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "Why is Prompt Engineering important?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "What are the advantages of Embeddings and Vector Search?",
        "expected": "The assistant should answer using the documents."
    },

    {
        "question": "Why is Cosine Similarity Used?",
        "expected": "The assistant should answer using the documents."
    },
   
    {
        "question": "How much water should an adult consume during a day?",
        "expected": "The assistant should return the fallback message."
    },

    {
        "question": "What are the biggest Tech Companies around the world?",
        "expected": "The assistant should return the fallback message."
    },

    {
        "question": "Who is Barbaros Günay?",
        "expected": "The assistant should return the fallback message."
    },

    {
        "question": "When was the last Championship won by Besiktas?",
        "expected": "The assistant should return the fallback message."
    }

]


# ------------------------------------
# Create Log File
# ------------------------------------
log = open(
    "test_results.txt",
    "w",
    encoding="utf-8"
)

log.write("=" * 60 + "\n")
log.write("RAG TEST RESULTS\n")
log.write("=" * 60 + "\n")
log.write(f"Date: {datetime.now()}\n\n")

print("=" * 60)
print("RAG TESTS")
print("=" * 60)


# ------------------------------------
# Run Tests
# ------------------------------------
for i, test in enumerate(tests, start=1):

    print(f"\nTEST {i}")
    print("Question :", test["question"])

    results = retriever.search(test["question"])

    if len(results) == 0:

        answer = "I couldn't find this information in the provided documents."

    else:

        answer = llm.generate(
            test["question"],
            results
        )

    print("Expected :", test["expected"])
    print("Answer   :", answer)

    print("-" * 60)

    log.write(f"TEST {i}\n")
    log.write(f"Question : {test['question']}\n")
    log.write(f"Expected : {test['expected']}\n")
    log.write(f"Answer   : {answer}\n")
    log.write("-" * 60 + "\n")


log.close()

print("\nAll tests completed.")
print("Results saved to test_results.txt")