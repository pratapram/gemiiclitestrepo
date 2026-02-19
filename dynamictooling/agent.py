"""
Tool Agent module for representing individual tool agents using google-genai.
"""

from google import genai
from typing import List, Optional, Any

class ToolAgent:
    """
    Represents an individual tool agent that can process specific tasks.
    """

    def __init__(self, api_key: str, name: str, system_instructions: str, model_name: str = "gemini-1.5-flash"):
        """
        Initialize the ToolAgent.

        Parameters
        ----------
        api_key : str
            The API key for Google Generative AI.
        name : str
            Unique name for the agent.
        system_instructions : str
            System instructions for the agent.
        model_name : str, optional
            The name of the Gemini model to use, by default "gemini-1.5-flash".
        """
        self.name = name
        self.system_instructions = system_instructions
        self.model_name = model_name
        self.client = genai.Client(api_key=api_key)

    def process(self, prompt: str, attachments: Optional[List[Any]] = None) -> str:
        """
        Process a given prompt using the agent's instructions.

        Parameters
        ----------
        prompt : str
            The prompt to process.
        attachments : Optional[List[Any]], optional
            Optional file attachments for the tool, by default None.

        Returns
        -------
        str
            The processed response.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config={
                'system_instruction': self.system_instructions
            }
        )
        return response.text