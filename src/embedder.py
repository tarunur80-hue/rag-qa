from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

# Load the model once, so we don't reload it for every question
model = SentenceTransformer(MODEL_NAME)


def embed_texts(texts):
    """Turn a list of texts into a list of number-vectors (embeddings)."""
    return model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )