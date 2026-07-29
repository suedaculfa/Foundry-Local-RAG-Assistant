import sqlite3
import json
import numpy as np

from config import DATABASE_NAME
from config import DATABASE_FOLDER
from pathlib import Path


class Database:

    def __init__(self):

        

        BASE_DIR = Path(__file__).resolve().parent.parent
        DATABASE_PATH = BASE_DIR / DATABASE_FOLDER / DATABASE_NAME

        self.conn = sqlite3.connect(DATABASE_PATH)

        self.cursor = self.conn.cursor()

        self.create_table()

    # -------------------------
    # Create table
    # -------------------------
    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS documents(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            source TEXT,
                            
            chunk_id INTEGER,
                            
            chunk TEXT,

            embedding TEXT

        )

        """)

        self.conn.commit()

    # -------------------------
    # Clear Database
    # -------------------------
    def clear_database(self):

        self.cursor.execute(

            "DELETE FROM documents"

        )

        self.conn.commit()

    # -------------------------
    # Add Chunk 
    # -------------------------
    def add_chunk(

        self,

        source,

        chunk_id,

        chunk,

        embedding

    ):

        self.cursor.execute(
            """
            INSERT INTO documents
            (source, chunk_id, chunk, embedding)
            VALUES (?, ?, ?, ?)
            """,
            (
                source,
                chunk_id,
                chunk,
                json.dumps(embedding)
            )
        )

        self.conn.commit()

    # -------------------------
    # Retrieve all chunks
    # -------------------------
    def get_all_chunks(self):

        self.cursor.execute(

            """

            SELECT

            source,

            chunk_id,

            chunk,

            embedding

            FROM documents

            """

        )

        rows = self.cursor.fetchall()

        results = []

        for row in rows:

            results.append(

                {

                    "source": row[0],

                    "chunk_id": row[1],

                    "chunk": row[2],

                    "embedding": np.array(

                        json.loads(

                            row[3]

                        )

                    )

                }

            )

        return results

    # -------------------------
    # Record count
    # -------------------------
    def count(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM documents"

        )

        return self.cursor.fetchone()[0]

    # -------------------------
    # Close connection
    # -------------------------
    def close(self):

        self.conn.close()


if __name__ == "__main__":

    db = Database()

    print(

        "Record count:",

        db.count()

    )

    db.close()