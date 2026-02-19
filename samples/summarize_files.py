"""
Sample script demonstrating how to use dynamictooling with Vertex AI to summarize text.
"""

import os
from dotenv import load_dotenv
from dynamictooling.registry import ToolRegistry

def main():
    # Load environment variables from .env if present
    load_dotenv()

    # Support multiple API key environment variable names
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or os.getenv("GOOGLE_CLOUD_API_KEY")
    
    if not api_key:
        print("Please set one of GEMINI_API_KEY, GOOGLE_API_KEY, or GOOGLE_CLOUD_API_KEY in your .env file.")
        return

    # Initialize ToolRegistry with vertexai=True as shown in example.py
    registry = ToolRegistry(
        api_key=api_key,
        vertexai=True
    )

    # Register a summarizer tool
    registry.register_tool(
        name="summarizer",
        system_instructions="You are an expert summarizer. Provide concise summaries of the input text.",
        prompt_template="Summarize the following text:\n\n{input}",
        model_name="gemini-3-flash-preview"
    )

    # Invoke the summarizer tool
    texts_to_summarize = [
        "The quick brown fox jumps over the lazy dog. This is a classic pangram used in typography.",
        "Artificial Intelligence is transforming the world. From healthcare to finance, AI is everywhere."
    ]

    for i, text in enumerate(texts_to_summarize):
        print(f"Summarizing text {i+1}...")
        try:
            summary = registry.invoke_tool("summarizer", text)
            print(f"Summary {i+1}:\n{summary}\n")
        except Exception as e:
            print(f"Error summarizing text {i+1}: {e}")

if __name__ == "__main__":
    main()
