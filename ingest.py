from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

CHUNK_SIZE = 150
CHUNK_OVERLAP = 25


def load_text_documents(data_dir: Path) -> List[Dict[str, Any]]:
    """Load all .txt source files from the data directory."""
    text_files = sorted(data_dir.glob("*.txt"))
    documents: List[Dict[str, Any]] = []

    for text_file in text_files:
        text = text_file.read_text(encoding="utf-8")
        documents.append(
            {
                "source": text_file.name,
                "source_path": str(text_file.resolve()),
                "text": normalize_text(text),
            }
        )

    return documents


def normalize_text(text: str) -> str:
    """Normalize whitespace and remove repeated blank lines."""
    return " ".join(text.split())


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    """Split a document into overlapping chunks by approximate tokens.

    This implementation uses whitespace-separated tokens as a practical tokenizer
    for .txt sources. It preserves the requested chunk size and overlap.
    """
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    tokens = text.split()
    if not tokens:
        return []

    chunks: List[str] = []
    start = 0
    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunk = " ".join(tokens[start:end]).strip()
        if chunk:
            chunks.append(chunk)
        if end == len(tokens):
            break
        start += chunk_size - overlap

    return chunks


def build_chunks(data_dir: Path, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[Dict[str, Any]]:
    """Build a list of chunks for every document in the data folder."""
    documents = load_text_documents(data_dir)
    all_chunks: List[Dict[str, Any]] = []

    for document in documents:
        source = document["source"]
        text = document["text"]
        chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

        for index, chunk in enumerate(chunks, start=1):
            all_chunks.append(
                {
                    "id": f"{source}-{index}",
                    "source": source,
                    "chunk_index": index,
                    "chunk_size": len(chunk.split()),
                    "text": chunk,
                }
            )

    return all_chunks


def save_chunks(chunks: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(chunks, indent=2, ensure_ascii=False), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingest text documents and split them into chunks.")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Directory containing the source .txt files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/chunks.json"),
        help="Output path for the chunked JSON file.",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=CHUNK_SIZE,
        help="Chunk size in approximate tokens.",
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=CHUNK_OVERLAP,
        help="Overlap size in approximate tokens.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    chunks = build_chunks(args.data_dir, chunk_size=args.chunk_size, overlap=args.overlap)
    save_chunks(chunks, args.output)
    print(f"Saved {len(chunks)} chunks to {args.output}")


if __name__ == "__main__":
    main()
