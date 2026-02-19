"""
Sample script demonstrating how to use dynamictooling to summarize text.
"""

import os
from dynamictooling.registry import ToolRegistry

def main():
    # Ensure you have set the GOOGLE_API_KEY environment variable.
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Please set the GOOGLE_API_KEY environment variable.")
        return

    registry = ToolRegistry(api_key=api_key)

    # Register a summarizer tool
    registry.register_tool(
        name="summarizer",
        system_instructions="You are an expert summarizer. Provide concise summaries of the input text.",
        prompt_template="Summarize the following text:

{input}"
    )

    # Invoke the summarizer tool
    texts_to_summarize = [
        "The quick brown fox jumps over the lazy dog. This is a classic pangram used in typography.",
        "Artificial Intelligence is transforming the world. From healthcare to finance, AI is everywhere."
    ]

    for i, text in enumerate(texts_to_summarize):
        print(f"Summarizing text {i+1}...")
        summary = registry.invoke_tool("summarizer", text)
        print(f"Summary {i+1}:
{summary}
")

if __name__ == "__main__":
    main()
