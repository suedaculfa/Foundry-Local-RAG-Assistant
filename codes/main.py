import time
from retriever import Retriever
from llm import LLM

def main():
    retriever = Retriever()
    llm = LLM()

    print("=" * 60)
    print(" " * 20 + "Local RAG Assistant")
    print("=" * 60)
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYour Question: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue
        
        total_start = time.time()

        retrieval_start = time.time()
        
        results = retriever.search(question)
        
        retrieval_end = time.time()
        retrieval_time = retrieval_end - retrieval_start

        if len(results) == 0:
            print("\nI couldn't find this information in the provided documents.")
            continue

        contexts = []
        for item in results:
            contexts.append(item)

        
        generation_start = time.time()
        
        answer = llm.generate(question, contexts)
        
        generation_end = time.time()
        generation_time = generation_end - generation_start
        total_time = time.time() - total_start

        print("\n" + "=" * 60)
        print("Answer")
        print("=" * 60)
        print("\n" + answer + "\n")

        print("=" * 60)
        print("Retrieved Chunks")
        print("=" * 60)
        for item in results:
            print(f"Chunk: {item['chunk_id']}   Score: {item['score']:.4f}  Source: {item['source']}")

        print("\n" + "=" * 60)
        print("Sources")
        print("=" * 60)
        shown_sources = set()
        for item in results:
            if item["source"] not in shown_sources:
                print(f"• {item['source']}")
                shown_sources.add(item["source"])
                
        print("\n" + "-" * 20)
        print(f"Retrieval  : {retrieval_time:.2f} s")
        print(f"Generation : {generation_time:.2f} s")
        print(f"Total      : {total_time:.2f} s")
        print("=" * 60)

if __name__ == "__main__":
    main()