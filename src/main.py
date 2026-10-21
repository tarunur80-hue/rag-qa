import sys

from src.loader import load_document
from src.chunker import chunk_text
from src.embedder import embed_texts
from src.vector_store import VectorStore
from src.retriever import retrieve
from src.generator import generate_answer


def main():
    # Use the file given on the command line, or the sample document
    file_path = sys.argv[1] if len(sys.argv) > 1 else "data/company_policy.txt"

    print(f"Loading document: {file_path}")
    text = load_document(file_path)
    chunks = chunk_text(text)
    store = VectorStore(chunks, embed_texts(chunks))
    print(f"Ready! Indexed {len(chunks)} chunks.")
    print("Ask a question about the document (type 'quit' to exit).\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        if not question:
            continue

        try:
            retrieved = retrieve(question, store)
            answer = generate_answer(question, retrieved)
            print(f"\nAnswer: {answer}\n")
        except Exception as error:
            print(f"\nSomething went wrong: {error}\n")


if __name__ == "__main__":
    main()