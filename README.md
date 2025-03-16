# **Advanced Calculator Application**

![Welcome to the Advanced Calculator App](https://wallpapersok.com/images/hd/cool-calculator-with-formulas-gy7fwb9k68gum8hc.jpg)

## **Overview**
This Advanced Calculator Application is a Python-based command-line tool designed to demonstrate professional software development practices. It emphasizes clean, maintainable code, dynamic configuration, robust exception handling, logging, and testing, while integrating advanced features like a plugin system, Pandas-based history management, and design patterns.

## Demonstration Videos

- [**Video 1: CalculatorApp Demo**](https://screenrec.com/share/6S0LXhb5pv)
- [**Video 2: PyTest Coverage**](https://screenrec.com/share/fryN3WZRPG)

---

## **Key Features**
1. **Command-Line Interface (REPL):**
   - A user-friendly interface to perform operations interactively.
   - Supports arithmetic and statistical operations.
   - Includes history management commands.

2. **Plugin System:**
   - Dynamically loads new commands or features without modifying core code.
   - `menu` command lists all available plugin commands.

3. **Calculation History Management:**
   - Built with Pandas for efficient history tracking.
   - Save, load, clear, and display history records.

4. **Logging Practices:**
   - Logs INFO, WARNING, and ERROR messages to track application behavior.
   - Configurable via environment variables for flexible output destinations.

5. **Dynamic Configuration:**
   - Environment variables allow customization of the history file, log file, and log level.

6. **Design Patterns:**
   - **Facade Pattern** for simplifying Pandas operations.
   - **Command Pattern** for structuring REPL commands.
   - **Strategy and Factory Patterns** for flexible plugin integration.

---

## **Setup Instructions**
### **Prerequisites**
- Install dependencies with pip:
  ```bash
  pip install -r requirements.txt
  ```

### **Configuration**
1. Create a `.env` file for environment variables:
   ```plaintext
   HISTORY_FILE=history.csv
   LOG_LEVEL=INFO
   LOG_FILE=app.log
   ```
2. Customize these values as needed:
   - `HISTORY_FILE`: Path to save/load calculation history.
   - `LOG_LEVEL`: Logging level (`INFO`, `WARNING`, `ERROR`).
   - `LOG_FILE`: File to write logs. Leave empty to disable file logging.

---

## **Usage**
### **Running the Application**
To start the calculator application:
```bash
python main.py
```

### **Available Commands**
- **Arithmetic Operations:**
  ```plaintext
  add <num1> <num2>
  subtract <num1> <num2>
  multiply <num1> <num2>
  divide <num1> <num2>
  ```
- **Statistical Operations:**
  ```plaintext
  mean <num1> <num2> ...
  median <num1> <num2> ...
  mode <num1> <num2> ...
  ```
- **History Management:**
  ```plaintext
  history               # Display calculation history
  save                  # Save history to file
  load                  # Load history from file
  clear                 # Clear the history
  ```

### **Extending Functionality**
- Add plugins by placing Python files in the `plugins/` directory.
- Plugins are automatically loaded at runtime and displayed in the `menu` command.

---

## **Testing**
- Run tests with Pytest:
  ```bash
  pytest --cov=. --cov-report=term-missing
  ```
- Coverage is maintained at **90%+**.

---

## **Exception Handling**
This project applies both LBYL (*Look Before You Leap*) and EAFP (*Easier to Ask for Forgiveness than Permission*) principles:
- Example of **LBYL**: Checking if a file exists before attempting to load it in `load_history()`.
- Example of **EAFP**: Handling `ZeroDivisionError` in division operations and `StatisticsError` in mode operations.

---

## **Logging**
- Logging is configured dynamically based on environment variables.
- Key locations of logging:
  - `HistoryManager`: Logs all file operations and history events.
  - REPL: Logs user commands and any exceptions raised.

---

## **Design Patterns**
- **Command Pattern**: Simplifies how commands are handled in the REPL.
- **Facade Pattern**: Provides an interface for managing calculation history (e.g., `save_history`, `load_history`).
- **Strategy and Factory Patterns**: Enable seamless plugin integration.

---

## **Commit History**
Logical and descriptive commits showcase incremental development:
- **Improved test coverage for `statistics_operations`.**
- **Added REPL tests for unknown commands and history.**
- **Refactored logging for history management.**

---