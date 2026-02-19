# Project: dynamictooling

## Purpose
This project is a Python module designed to let the root agent create tool agents that can help with the given task automtically. This allows the root agent to stay at the higher level without getting lost in the weeds of a particular task.

## Architecture 

## The tool registry

When given a complex task that LLM cannot perform by itself effectively, 
the LLM will first create a new tool_agent (which will also use an LLM), and register with the tool registry.
The new tool can only have a "system_instructions", "prompt", and file attachments (no code).
After the registry confirms the creation of the new tool, it can then be invoked by the LLM for processing.

For example: if an LLM is being tasked to summarize 10 files, the root LLM can create a "summarizer" (that would use another LLM), and would call this "summarizer_tool" 10 times, and finally respond back with the results.



## Technology Stack & Guidelines
*   **Language:** Python 3.10+
*   **Style Guide:** Adhere to [PEP 8](https://www.python.org) style guidelines.
*   **Dependencies:**
    *   [list any specific libraries, e.g., `requests`, `numpy`, etc.]
*   **directory structure:**
    *   The core logic resides in the `dynamictooling/` directory.
    *   Tests must be located in the `tests/` directory. Create unit test cases there.
    *   tests/test_cases_functional.txt describes three important test cases
    *   create a `samples/` directory to include code samples on how to use this library
    *   Documentation follows the [NumPy docstring standard](https://numpydoc.readthedocs.io) for all functions and classes.
*    ** use uv to manage packages

## directory structure

## Coding Preferences
*   Avoid using global variables where possible.
*   Prioritize clear, readable code over overly complex one-liners.
*   Include comprehensive unit tests for all new functionality.
*   Ensure all code is compatible with the latest recommended 


