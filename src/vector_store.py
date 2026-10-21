import faiss


class VectorStore:
    def __init__(self, chunks, embeddings):
        """Build a FAISS index from chunks and their embeddings."""
        self.chunks = chunks
        dimension = embeddings.shape[1]  # 384 for our model
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

    def search(self, query_embedding, top_k=3):
        """Return the top_k closest chunks as (chunk_text, score) pairs."""
        scores, ids = self.index.search(query_embedding, top_k)
        results = []
        for score, i in zip(scores[0], ids[0]):
            if i != -1:  # -1 means "no result found"
                results.append((self.chunks[i], float(score)))
        return results