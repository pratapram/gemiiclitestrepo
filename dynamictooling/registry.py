"""
Tool Registry module for managing dynamic tool agents using google-genai.
"""

from google import genai
from typing import Dict, List, Optional, Any

class ToolRegistry:
    """
    Registry for managing and invoking dynamic tool agents.
    """

    def __init__(self, api_key: str, vertexai: bool = True):
        """
        Initialize the ToolRegistry with a Google GenAI client.

        Parameters
        ----------
        api_key : str
            The API key or Access Token for Google Generative AI.
        vertexai : bool, optional
            Whether to use Vertex AI, by default True.
        """
        # Based on example.py, vertexai=True with api_key works.
        self.client = genai.Client(
            api_key=api_key,
            vertexai=vertexai
        )
        self.tools: Dict[str, Any] = {}

    def register_tool(
        self, 
        name: str, 
        system_instructions: str, 
        prompt_template: str,
        model_name: str = "gemini-3-flash-preview"
    ):
        """
        Register a new tool agent.

        Parameters
        ----------
        name : str
            Unique name for the tool.
        system_instructions : str
            System instructions for the tool agent.
        prompt_template : str
            The prompt template to be used when the tool is invoked.
        model_name : str, optional
            The name of the Gemini model to use, by default "gemini-3-flash-preview".
        """
        self.tools[name] = {
            "system_instructions": system_instructions,
            "prompt_template": prompt_template,
            "model_name": model_name
        }

    def invoke_tool(self, name: str, input_data: str, attachments: Optional[List[Any]] = None) -> str:
        """
        Invoke a registered tool agent.

        Parameters
        ----------
        name : str
            The name of the tool to invoke.
        input_data : str
            The data to pass to the tool agent.
        attachments : Optional[List[Any]], optional
            Optional file attachments for the tool, by default None.

        Returns
        -------
        str
            The response from the tool agent.
        """
        if name not in self.tools:
            raise ValueError(f"Tool '{name}' not found in registry.")

        tool_config = self.tools[name]
        
        prompt = tool_config["prompt_template"].format(input=input_data)
        
        response = self.client.models.generate_content(
            model=tool_config["model_name"],
            contents=prompt,
            config={
                'system_instruction': tool_config["system_instructions"]
            }
        )
        return response.text