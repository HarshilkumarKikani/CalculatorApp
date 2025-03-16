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

@patch("builtins.input", side_effect=["history", "exit"])
@patch("builtins.print")
@patch("history.history_manager.HistoryManager.display_history", return_value="Operation log")
def test_repl_history(mock_display, mock_print, mock_input):
    main()
    mock_display.assert_called_once()
    mock_print.assert_any_call("Operation log")

@patch("builtins.input", side_effect=["clear", "exit"])
@patch("builtins.print")
@patch("history.history_manager.HistoryManager.clear_history")
def test_repl_clear(mock_clear, mock_print, mock_input):
    main()
    mock_clear.assert_called_once()
    mock_print.assert_any_call("History cleared!")

@patch("builtins.input", side_effect=["save", "exit"])
@patch("builtins.print")
@patch("history.history_manager.HistoryManager.save_history")
def test_repl_save(mock_save, mock_print, mock_input):
    main()
    mock_save.assert_called_once()
    mock_print.assert_any_call("History saved!")

@patch("builtins.input", side_effect=["load", "exit"])
@patch("builtins.print")
@patch("history.history_manager.HistoryManager.load_history")
def test_repl_load(mock_load, mock_print, mock_input):
    main()
    mock_load.assert_called_once()
    mock_print.assert_any_call("History loaded!")