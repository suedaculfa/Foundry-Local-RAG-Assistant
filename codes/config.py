from sentence_transformers import SentenceTransformer

# -----------------------------
# SQLite
# -----------------------------
DATABASE_NAME = "rag.db"
DATABASE_FOLDER = "db"

# -----------------------------
# Chunk
# -----------------------------
CHUNK_SIZE = 600
CHUNK_OVERLAP = 200
TOP_K = 5


# -----------------------------
# Embedding Model
# -----------------------------
embedding_model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)
# -----------------------------
# Foundry Local
# -----------------------------
FOUNDRY_URL = "http://127.0.0.1:58002/v1"

CHAT_MODEL = "qwen2.5-0.5b-instruct-generic-cpu:4"

SYSTEM_PROMPT = """
You are a Retrieval-Augmented Generation (RAG) assistant.

Rules:
- Answer ONLY using the provided context.
- Never use outside knowledge.
- If the answer cannot be found in the context, reply:
  "I couldn't find this information in the provided documents."
- Keep answers concise.
- Never invent information.
"""