from openai import OpenAI
from config import SYSTEM_PROMPT
from config import (
    FOUNDRY_URL,
    CHAT_MODEL
)

class LLM:

    def __init__(self):

        self.client = OpenAI(
            base_url=FOUNDRY_URL,
            api_key="unused"
        )

        self.model = CHAT_MODEL

    def generate(self, question, contexts):

        context_text = ""

        for c in contexts:

            context_text += (
                f"""
        Source: {c['source']}
        Chunk: {c['chunk_id']}

        {c['chunk']}

        ----------------------------------------

        """
            )

        prompt = f"""
        {SYSTEM_PROMPT}

        Context:
        {context_text}

        Question:
        {question}

        Remember:
        If the answer is not explicitly contained in the context,
        reply EXACTLY with:

        I couldn't find this information in the provided documents.

        Answer:
        """

        response = self.client.chat.completions.create(
            
            model=self.model,
            
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()