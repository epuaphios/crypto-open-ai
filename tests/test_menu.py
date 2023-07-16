import unittest
from unittest.mock import patch, MagicMock
import datetime
import matplotlib.pyplot as plt
from modules.historical_getter import get_historical_data
from modules.current_price import get_current_price
from rich.console import Console
from modules.option import user_option


class TestMenu(unittest.TestCase):
    def test_menu_exists(self):
        # Assert that the function exists
        self.assertTrue(callable(TestMenu))

    def test_help_menu(self):
        # Mock the input function
        with patch("builtins.input", return_value=""):
            # Call the help_menu function
            TestMenu()

    def test_choice2(self):
        # Mock the Prompt.ask function
        with patch("menu.Prompt.ask", side_effect=["30", "Conservative"]):
            # Call the choice2 function
            TestMenu()

        # No assertion needed as the function runs without errors

    def test_end_program(self):
        # Mock the input function
        with patch("builtins.input", return_value=""):
            # Call the end_programm function
            TestMenu()

    def test_menu_exit(self):
        # Mock the Prompt.ask function
        with patch("menu.Prompt.ask", return_value="5"):
            # Mock the console.print function
            with patch("menu.console.print") as mock_print:
                # Call the menu function
                TestMenu()
    
    def test_choice2_valid_input(self):
    # Mock the Prompt.ask function
      with patch("menu.Prompt.ask", side_effect=["30", "Conservative"]):
        # Call the choice2 function
        TestMenu()

    # # Assert that the user_input function was called with the correct arguments
    # user_input.assert_called_with("30", "conservative")

    # def test_choice2_invalid_input():
    #     # Mock the Prompt.ask function
    #     with patch("my_module.Prompt.ask", side_effect=["100", "Invalid"]):
    #         # Call the choice2 function
    #         with pytest.raises(SystemExit):
    #             TestMenu()

# Menu testing

# @pytest.mark.skip("TODO")
# pass




