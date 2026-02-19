"""
Unit tests for the ToolRegistry class using google-genai.
"""

import unittest
from unittest.mock import MagicMock, patch
from dynamictooling.registry import ToolRegistry

class TestToolRegistry(unittest.TestCase):
    """
    Test cases for ToolRegistry.
    """

    @patch("google.genai.Client")
    def setUp(self, mock_client_class):
        self.mock_client = MagicMock()
        mock_client_class.return_value = self.mock_client
        self.registry = ToolRegistry(api_key="fake_key")

    def test_register_tool(self):
        """
        Test that a tool can be correctly registered.
        """
        self.registry.register_tool(
            name="test_tool",
            system_instructions="instructions",
            prompt_template="template {input}"
        )
        self.assertIn("test_tool", self.registry.tools)
        self.assertEqual(self.registry.tools["test_tool"]["system_instructions"], "instructions")

    def test_invoke_tool(self):
        """
        Test that a tool can be invoked and returns the expected result.
        """
        # Mocking the Gemini model response
        mock_response = MagicMock()
        mock_response.text = "mocked response"
        self.mock_client.models.generate_content.return_value = mock_response

        self.registry.register_tool(
            name="test_tool",
            system_instructions="instructions",
            prompt_template="template {input}"
        )
        
        result = self.registry.invoke_tool("test_tool", "test input")
        
        self.assertEqual(result, "mocked response")
        self.mock_client.models.generate_content.assert_called_once_with(
            model="gemini-1.5-flash",
            contents="template test input",
            config={'system_instruction': 'instructions'}
        )

if __name__ == "__main__":
    unittest.main()