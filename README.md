# DynamicTooling

DynamicTooling is a Python module designed to allow root agents to dynamically create and manage specialized tool agents. This abstraction enables higher-level agents to delegate complex tasks to specialized "micro-agents" powered by Google's Gemini models via Vertex AI.

## Features

- **Dynamic Tool Registration**: Register specialized agents with unique system instructions and prompt templates.
- **Vertex AI Integration**: Built on top of the `google-genai` library, optimized for Vertex AI.
- **Flexible Invocation**: Invoke tools with dynamic inputs and receive structured responses.
- **Environment Management**: Seamlessly manages dependencies and environment variables using `uv` and `python-dotenv`.

## Installation

This project uses `uv` for package management.

```bash
# Clone the repository
git clone https://github.com/pratapram/gemiiclitestrepo.git
cd gemiiclitestrepo

# Install dependencies
uv sync
```

## Configuration

Create a `.env` file in the root directory with your Google Cloud credentials:

```env
GOOGLE_CLOUD_API_KEY="your-vertex-ai-access-token"
PROJECT_ID="your-google-cloud-project-id"
LOCATION="us-central1"
```

## Usage

### Tool Registry

The `ToolRegistry` is the primary interface for managing agents.

```python
import os
from dynamictooling.registry import ToolRegistry

# Initialize the registry
registry = ToolRegistry(api_key=os.getenv("GOOGLE_CLOUD_API_KEY"))

# Register a tool
registry.register_tool(
    name="summarizer",
    system_instructions="You are an expert summarizer.",
    prompt_template="Summarize this: {input}"
)

# Invoke the tool
result = registry.invoke_tool("summarizer", "Long text to summarize...")
print(result)
```

### Running Samples

You can run the provided summarization sample:

```bash
PYTHONPATH=. uv run python samples/summarize_files.py
```

## Testing

Run the unit tests to verify the installation:

```bash
uv run python -m unittest discover tests
```

## License

MIT
