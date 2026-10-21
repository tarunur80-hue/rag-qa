import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads GROQ_API_KEY from your .env file

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-20b"

SYSTEM_PROMPT = (
    "You answer questions about a company document. You will be given "
    "excerpts from that document as context. Read ALL the excerpts "
    "carefully, then answer using only facts stated in them. "
    "The wording of the question may differ from the document. For "
    "example, 'leaves' in a question can match 'paid leave' in the text. "
    "Only if the excerpts contain nothing relevant to the question, reply "
    "exactly: 'I could not find the answer in the document.' "
    "Otherwise, answer in one or two clear sentences."
)


def generate_answer(question, retrieved):
    """Ask the LLM to answer using only the retrieved chunks."""
    context = "\n\n".join(
        f"[Chunk {i + 1}]\n{chunk}" for i, (chunk, score) in enumerate(retrieved)
    )

    user_message = f"Context:\n{context}\n\nQuestion: {question}"

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content