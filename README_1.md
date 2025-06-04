# Personal Finance Tracker

This is a simple console-based Python application designed to help you track and summarize your personal expenses. You can add new expenses, categorize them, and then view a detailed list of all expenses or a summary by category.

---

## How to Run the Script

1.  **Save the code:** Save the provided Python code into a file named `finance_tracker.py` (or any other `.py` extension).
2.  **Open a terminal or command prompt:** Navigate to the directory where you saved the file.
3.  **Run the script:** Execute the script using the Python interpreter:
    ```bash
    python finance_tracker.py
    ```
4.  **Follow the prompts:** The program will present a menu. Enter the corresponding number for the action you'd like to perform (Add expense, View All Expenses, View Summary, or Exit).

---

## Python Concepts Used

This project utilizes several fundamental Python programming concepts:

* **Variables and Data Types:**
    * `str`: For text inputs like expense descriptions and category names.
    * `float`: For numerical expense amounts.
    * `int`: For menu choices.
    * `tuple`: Used to store `(expense_description, expense_amount)` as a single value associated with a category key.
    * `dict` (Dictionary): The core data structure (`expenseDict`) used to store expenses, mapping a `categoryName` (key) to an `expense` tuple (value).
* **Functions:**
    * `addExpense()`: Handles user input for adding new expenses and storing them.
    * `view_expenses()`: Displays all recorded expenses by category.
    * `view_summary()`: Provides a summary of expenses, showing total amount per category.
    * `menuLogic()`: Manages the main program flow and user interaction menu.
* **Input/Output:**
    * `input()`: To receive user input from the console.
    * `print()`: To display information and prompts to the user.
* **Control Flow:**
    * `while` loops: For repetitive actions like adding multiple expenses or keeping the main menu running until the user exits.
    * `if`/`elif`/`else` statements: For conditional logic, such as checking user menu choices, validating inputs, and determining whether to display an empty report message.
* **Error Handling:**
    * `try`/`except` blocks: To gracefully handle potential errors (exceptions) like `ValueError` (e.g., when a non-numeric value is entered where a number is expected) and other `Exception` types.
    * `continue` statement: Used within loops and `except` blocks to skip the rest of the current iteration and re-prompt the user for valid input.
* **String Methods:**
    * `.strip()`: Used to remove leading/trailing whitespace from user inputs to ensure accurate validation (e.g., preventing a space from being considered a valid non-empty input).
