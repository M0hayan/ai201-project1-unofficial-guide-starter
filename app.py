from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from dotenv import load_dotenv
import gradio as gr
from groq import Groq
from vector_store import query_vector_store, CHROMA_DIR

MODEL_NAME = "llama-3.3-70b-versatile"
GROUNDING_INSTRUCTION = (
    "Answer the question using only the information in the provided documents. "
    "If the documents don't contain enough information to answer, say 'I don't have enough information on that.' "
    "Ensure the answers are from received text only and with source attribution. "
    "Return the result using the exact format:\nAnswer: <your answer>\nSources: <source1>, <source2>, ..."
)


@dataclass
class RetrievedChunk:
    source: str
    chunk_index: int
    text: str


def load_api_key_from_env() -> str:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment. Please add it to .env or export it.")
    return api_key


def format_retrieved_context(results: dict) -> list[RetrievedChunk]:
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    chunks: list[RetrievedChunk] = []

    for document, metadata in zip(documents, metadatas):
        chunks.append(
            RetrievedChunk(
                source=metadata.get("source", "unknown"),
                chunk_index=int(metadata.get("chunk_index", 0)),
                text=document.strip(),
            )
        )

    return chunks


def build_prompt(question: str, retrieved_chunks: list[RetrievedChunk]) -> str:
    context_blocks = []
    for chunk in retrieved_chunks:
        context_blocks.append(
            f"Source: {chunk.source}\nChunk: {chunk.chunk_index}\nText: {chunk.text}"
        )

    context = "\n\n".join(context_blocks)
    return (
        f"{GROUNDING_INSTRUCTION}\n\n"
        "Context:\n"
        f"{context}\n\n"
        f"Question: {question}\n"
        "Answer in the requested format."
    )


def generate_answer(question: str, top_k: int = 5) -> str:
    api_key = load_api_key_from_env()
    client = Groq(api_key=api_key)

    retrieval = query_vector_store(query=question, top_k=top_k, persist_directory=CHROMA_DIR)
    retrieved_chunks = format_retrieved_context(retrieval)

    if not retrieved_chunks:
        return "Answer: I don't have enough information on that.\nSources: none"

    messages = [
        {"role": "system", "content": GROUNDING_INSTRUCTION},
        {"role": "user", "content": build_prompt(question, retrieved_chunks)},
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.0,
        max_completion_tokens=512,
    )

    if not response.choices:
        raise RuntimeError("Groq returned no completion choices.")

    return response.choices[0].message.content or ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query the ISU housing QA system with grounded generation.")
    parser.add_argument("--query", type=str, default=None, help="Question to ask the system.")
    parser.add_argument("--top-k", type=int, default=5, help="Number of retrieved chunks to include as context.")
    return parser.parse_args()


def build_gradio_interface() -> None:
    def respond(question: str, top_k: int = 5) -> str:
        if not question or not question.strip():
            return "Answer: Please enter a question.\nSources: none"
        return generate_answer(question, top_k=top_k)

    with gr.Blocks() as demo:
        gr.Markdown("# ISU Housing QA")
        gr.Markdown(
            "Ask a question about ISU housing and get a grounded answer with source attribution."
        )
        question_input = gr.Textbox(
            lines=4,
            label="Question",
            placeholder="What do I need to know about ISU housing policies?",
        )
        top_k_slider = gr.Slider(
            minimum=1,
            maximum=10,
            step=1,
            value=5,
            label="Top K retrieved chunks",
        )
        answer_output = gr.Textbox(lines=12, label="Answer")
        submit_button = gr.Button("Submit")

        submit_button.click(
            respond,
            inputs=[question_input, top_k_slider],
            outputs=[answer_output],
        )
        question_input.submit(
            respond,
            inputs=[question_input, top_k_slider],
            outputs=[answer_output],
        )

    demo.launch(server_name="0.0.0.0", server_port=7860)


def main() -> None:
    args = parse_args()
    if args.query:
        answer = generate_answer(args.query, top_k=args.top_k)
        print(answer)
    else:
        build_gradio_interface()


if __name__ == "__main__":
    main()
