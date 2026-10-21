# Mini Q&A System (RAG)

A command-line Retrieval-Augmented Generation (RAG) app. You give it a TXT or PDF document, ask questions, and it answers **only from the document**. If the answer is not in the document, it says so instead of guessing.

## How it works

1. **Load**: read text from a `.txt` or `.pdf` file (`src/loader.py`)
2. **Chunk**: split the text into ~200-word chunks with 40-word overlap (`src/chunker.py`)
3. **Embed**: convert chunks to vectors with Sentence Transformers, model `all-MiniLM-L6-v2` (`src/embedder.py`)
4. **Store**: index the vectors in FAISS (`src/vector_store.py`)
5. **Retrieve**: find the top 3 chunks closest to the question (`src/retriever.py`)
6. **Generate**: send the chunks and question to an LLM on Groq with a strict "answer only from context" prompt (`src/generator.py`)

## Setup

1. Clone the repo and open the folder:
```bash
   git clone https://github.com/tarunur80-hue/rag-qa.git
   cd rag-qa
```
2. Create and activate a virtual environment:
```bash
   python -m venv venv
   source venv/Scripts/activate    # Windows (Git Bash)
   # source venv/bin/activate      # Mac / Linux
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Get a free API key from https://console.groq.com, then copy `.env.example` to `.env` and put your key in it:
```
   GROQ_API_KEY=your_key_here
```

## Usage

Run with the sample document:
```bash
python -m src.main
```

Or with your own file:
```bash
python -m src.main path/to/your_document.pdf
```

Type a question at the `You:` prompt, and type `quit` to exit.

## Example

```
You: How many leaves are allowed?
Answer: Employees are allowed 20 days of paid leave annually.

You: Who won the cricket world cup?
Answer: I could not find the answer in the document.
```

## Test queries

See [`tests/test_queries.md`](tests/test_queries.md) for sample questions and expected answers.

## Project structure

```
data/company_policy.txt   sample document
src/                      pipeline code
tests/test_queries.md     test questions
requirements.txt          dependencies
```

## Avoiding hallucination

- The prompt tells the model to use only the retrieved context.
- If the context has no answer, the model must reply "I could not find the answer in the document."
- Temperature is set to 0 for consistent, factual output.

## Possible improvements

- Chunk by section or paragraph instead