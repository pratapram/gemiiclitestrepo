"""
Unit tests for the ToolAgent class using google-genai and Vertex AI.
"""

import unittest
from unittest.mock import MagicMock, patch
from dynamictooling.agent import ToolAgent

class TestToolAgent(unittest.TestCase):
    """
    Test cases for ToolAgent.
    """

    @patch("google.genai.Client")
    def test_process(self, mock_client_class):
        """
        Test that a ToolAgent can correctly process a given prompt.
        """
        # Mocking the Gemini model response
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_response = MagicMock()
        mock_response.text = "mocked agent response"
        mock_client.models.generate_content.return_value = mock_response

        agent = ToolAgent(
            api_key="fake_key",
            name="test_agent",
            system_instructions="system instructions",
            vertexai=True
        )
        
        result = agent.process("test prompt")
        
        self.assertEqual(result, "mocked agent response")
        mock_client.models.generate_content.assert_called_once_with(
            model="gemini-3-flash-preview",
            contents="test prompt",
            config={'system_instruction': 'system instructions'}
        )

if __name__ == "__main__":
    unittest.main()
