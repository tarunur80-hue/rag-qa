from src.embedder import embed_texts


def retrieve(question, store, top_k=3):
    """Find the top_k chunks most relevant to the question."""
    question_embedding = embed_texts([question])
    return store.search(question_embedding, top_k)