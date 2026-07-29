# Local RAG Assistant

This project is a simple Retrieval-Augmented Generation (RAG) assistant developed during the Microsoft Summer School.

The assistant reads Word documents, stores them in a local SQLite database using embeddings, retrieves the most relevant information with cosine similarity, and generates answers using a local Large Language Model (LLM) running through Microsoft Foundry Local.

---

## Features

- Reads Word (.docx) documents
- Splits documents into chunks
- Creates embeddings using Sentence Transformers
- Stores data in SQLite
- Retrieves relevant chunks with cosine similarity
- Generates answers with a local LLM
- Returns a fallback message when the answer cannot be found

---

## Technologies Used

- Python 3.14
- Microsoft Foundry Local
- Sentence Transformers
- SQLite
- NumPy
- python-docx

---

## Project Structure

```
YerelRAGAsistani/
├── codes/
│   ├── main.py
│   ├── config.py
│   ├── llm.py
│   ├── retriever.py
│   ├── database.py
│   ├── ingestion.py
│   └── test.py
|
│
├── db/
│   └── rag.db
|
├── resources/
│   ├── document1.docx
│   ├── document2.docx
│   └── ...
|
├── reports/
│   ├── Project_Report.docx
│   ├── Evaluation_Report.docx
│   └── System_Test_Report.docx
|
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

1. Documents are loaded from the **resources** folder.
2. Documents are divided into chunks.
3. Embeddings are generated for each chunk.
4. Embeddings are stored in SQLite.
5. The user's question is converted into an embedding.
6. The most relevant chunks are retrieved.
7. The retrieved context is sent to the local LLM.
8. The assistant generates an answer based only on the retrieved documents.

---

## Running the Project

### 1. Process the documents

```bash
python ingest.py
```

### 2. Start the assistant

```bash
python main.py
```

### 3. Run the test cases

```bash
python tests.py
```

---

## Configuration

Current project settings:

- Chunk Size: 600
- Chunk Overlap: 200
- Top-K: 5
- Embedding Model: intfloat/multilingual-e5-base
- Chat Model: qwen2.5-0.5b-instruct-generic-cpu:4

---

## Future Improvements

- Support PDF and TXT files
- Use a vector database instead of SQLite
- Add a graphical user interface
- Improve retrieval accuracy

---

## Notes

This project was developed for educational purposes as part of the Microsoft Summer School program.