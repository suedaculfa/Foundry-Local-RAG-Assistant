from pathlib import Path
from docx import Document

from config import (
    embedding_model,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

from database import Database


class Ingestor:

    def __init__(self):
        self.db = Database()

    # -----------------------------
    # Read Word documents
    # -----------------------------
    def read_docx(self, file_path):

        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        return "\n".join(paragraphs)

    # -----------------------------
    # Create Chunks
    # -----------------------------
    def create_chunks(self, text):

        chunks = []

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            if chunk.strip():
                chunks.append(chunk)

            start += (CHUNK_SIZE - CHUNK_OVERLAP)

        return chunks

    # -----------------------------
    # Process a single file 
    # -----------------------------
    def process_file(self, file_path):

        print(f"\nPrecessing: {file_path.name}")

        text = self.read_docx(file_path)

        chunks = self.create_chunks(text)

        print(f"{len(chunks)} chunks created.")

        for i, chunk in enumerate(chunks):

            embedding = embedding_model.encode(
            chunk,
            convert_to_numpy=True,
            normalize_embeddings=True
        ).tolist()

            self.db.add_chunk(
                source = file_path.name,
                chunk_id = i+1,
                chunk = chunk,
                embedding = embedding
            )

        print("Saved.")

    # -----------------------------
    # Process the resource folder
    # -----------------------------
    def ingest_all(self):

        self.db.clear_database()

        project_folder = Path(__file__).resolve().parent

        resources_folder = project_folder / "resources"

        if not resources_folder.exists():

            raise Exception(
                f"Resources folder not found:\n{resources_folder}"
            )

        files = list(resources_folder.glob("*.docx"))

        if len(files) == 0:

            raise Exception(
                "No Word documents were found in the resource folder."
            )

        print(f"\nFound {len(files)} Word documents.\n")

        for file in files:

            self.process_file(file)

        print("ALL DOCUMENTS HAVE BEEN PROCESSED.")

    def close(self):

        self.db.close()


if __name__ == "__main__":

    ingestor = Ingestor()

    ingestor.ingest_all()

    ingestor.close()