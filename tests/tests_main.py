import pytest
from unittest.mock import patch, MagicMock
from main import main

@patch("builtins.input", side_effect=["menu", "exit"])
@patch("builtins.print")
def test_repl_menu(mock_print, mock_input):
    # Run the REPL for two commands: "menu" and "exit"
    main()
    
    # Verify the menu options were printed
    mock_print.assert_any_call("Available commands: add, subtract, multiply, divide, history, clear, save, load, exit")
    mock_print.assert_any_call("Goodbye!")

@patch("builtins.input", side_effect=["add 2 3", "exit"])
@patch("builtins.print")
@patch("plugins.basic_operations.execute", return_value=5)
def test_repl_add(mock_execute, mock_print, mock_input):
    # Mock HistoryManager
    with patch("main.HistoryManager") as MockHistoryManager:
        MockHistoryManager.return_value = MagicMock()
        
        # Run the REPL for the "add 2 3" command
        main()
        
        # Verify the addition plugin was called
        mock_execute.assert_called_with("add 2 3", MockHistoryManager.return_value)
        
        # Check the result was printed
        mock_print.assert_any_call("Result: 5")

@patch("builtins.input", side_effect=["unknown_command", "exit"])
@patch("builtins.print")
def test_repl_unknown_command(mock_print, mock_input):
    # Run the REPL for an invalid command
    main()
    
    # Verify the error message was printed
    mock_print.assert_any_call("Unknown command. Type 'menu' for options.")