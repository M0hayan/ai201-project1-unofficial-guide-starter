from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import chromadb
from sentence_transformers import SentenceTransformer

CHUNK_FILE = Path("data/chunks.json")
CHROMA_DIR = Path("data/chroma_store")
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "isu_housing_chunks"


def load_chunks(chunk_file: Path = CHUNK_FILE) -> List[Dict[str, Any]]:
    """Load chunk metadata and text from the ingestion output file."""
    if not chunk_file.exists():
        raise FileNotFoundError(f"Chunk file not found: {chunk_file}")

    with chunk_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_embedding_model(model_name: str = EMBED_MODEL_NAME) -> SentenceTransformer:
    """Load the sentence-transformers embedding model."""
    return SentenceTransformer(model_name)


def create_chroma_client(persist_directory: Path = CHROMA_DIR):
    """Create or load a Chroma client for persistent storage."""
    persist_directory.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(persist_directory))


def get_collection(client: chromadb.api.Client, name: str = COLLECTION_NAME):
    """Get or create the Chroma collection for chunk embeddings."""
    return client.get_or_create_collection(
        name=name,
        metadata={"description": "ISU housing text chunks for retrieval"},
    )


def embed_texts(model: SentenceTransformer, texts: List[str]) -> List[List[float]]:
    """Embed a list of text strings using the embedding model."""
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True, normalize_embeddings=True)
    return embeddings.tolist()


def build_vector_store(
    chunk_file: Path = CHUNK_FILE,
    persist_directory: Path = CHROMA_DIR,
    model_name: str = EMBED_MODEL_NAME,
) -> None:
    """Load chunks, embed them, and persist them into ChromaDB."""
    chunks = load_chunks(chunk_file)
    model = load_embedding_model(model_name)
    texts = [chunk["text"] for chunk in chunks]
    ids = [chunk["id"] for chunk in chunks]
    metadatas = [
        {
            "source": chunk["source"],
            "chunk_index": chunk["chunk_index"],
            "chunk_size": chunk["chunk_size"],
        }
        for chunk in chunks
    ]

    embeddings = embed_texts(model, texts)
    client = create_chroma_client(persist_directory)
    collection = get_collection(client)

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
    )
    print(f"Stored {len(ids)} chunk embeddings in ChromaDB at {persist_directory}")


def query_vector_store(
    query: str,
    top_k: int = 5,
    persist_directory: Path = CHROMA_DIR,
    model_name: str = EMBED_MODEL_NAME,
) -> Dict[str, Any]:
    """Run a similarity search over stored chunk embeddings."""
    model = load_embedding_model(model_name)
    client = create_chroma_client(persist_directory)
    collection = get_collection(client)

    query_embedding = model.encode([query], show_progress_bar=False, convert_to_numpy=True, normalize_embeddings=True)
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and query a Chroma vector store from chunked text.")
    parser.add_argument(
        "action",
        choices=["embed", "query"],
        help="Action to perform: embed chunk data or query the vector store.",
    )
    parser.add_argument(
        "--query",
        type=str,
        default=None,
        help="Query text to run against the stored embeddings. Required for the query action.",
    )
    parser.add_argument(
        "--chunk-file",
        type=Path,
        default=CHUNK_FILE,
        help="Path to the JSON file containing ingested chunks.",
    )
    parser.add_argument(
        "--persist-dir",
        type=Path,
        default=CHROMA_DIR,
        help="Directory to persist the Chroma vector store.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of nearest neighbors to return for query retrieval.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.action == "embed":
        build_vector_store(
            chunk_file=args.chunk_file,
            persist_directory=args.persist_dir,
        )
    elif args.action == "query":
        if not args.query:
            raise ValueError("--query is required when action=query")

        results = query_vector_store(
            query=args.query,
            top_k=args.top_k,
            persist_directory=args.persist_dir,
        )
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
