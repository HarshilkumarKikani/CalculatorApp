import pytest
from unittest.mock import patch, MagicMock
from main import main

@patch("builtins.input", side_effect=["menu", "exit"])
@patch("builtins.print")
def test_repl_menu(mock_print, mock_input):
    main()
    mock_print.assert_any_call("Available commands: add, subtract, multiply, divide, mean, median, mode, history, clear, save, load, exit")

@patch("builtins.input", side_effect=["unknown", "exit"])
@patch("builtins.print")
def test_repl_unknown_command(mock_print, mock_input):
    main()
    mock_print.assert_any_call("Unknown command. Type 'menu' for options.")