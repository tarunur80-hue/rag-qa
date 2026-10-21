def chunk_text(text, chunk_size=200, overlap=40):
    """Split text into chunks of about chunk_size words, with overlap."""
    words = text.split()
    step = chunk_size - overlap
    chunks = []

    for start in range(0, len(words), step):
        chunk = " ".join(words[start:start + chunk_size])
        chunks.append(chunk)

        # Stop once this chunk has reached the end of the document
        if start + chunk_size >= len(words):
            break

    return chunks