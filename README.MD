# Calculator Program

This program is a simple calculator that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. It provides a user-friendly graphical user interface (GUI) using the Tkinter library.

## Usage

To use the calculator program, follow these steps:

1. Make sure you have Python installed on your system.
2. Install the required dependencies by running the following command:

   ```shell
   pip install tkinter
   ```

3. Create a new Python file and import the necessary classes:

   ```python
   from calculator import Calculator
   from user_interface import UserInterface
   ```

4. Instantiate the `UserInterface` class and run the program:

   ```python
   if __name__ == "__main__":
       calculator_gui = UserInterface(Calculator())
   ```

5. The calculator GUI will appear, allowing you to enter two numbers and choose an operation.
6. Click the "Calculate" button to perform the selected operation.
7. The result will be displayed in the GUI.
8. After viewing the result, a message box will ask if you want to perform another calculation.
9. If you choose "Yes," the GUI will be reset, and you can enter new numbers and choose another operation.
10. If you choose "No," a message box will display a thank-you message, and the program will exit.

## Program Structure

The program consists of the following files:

- `calculator.py`: Contains the `Calculator` class that performs arithmetic operations.
- `user_interface.py`: Contains the `UserInterface` class that creates the calculator GUI and handles user interactions.
- `ask_again.py`: Contains the `AskAgain` class that prompts the user if they want to perform another calculation.
- `main.py`: The main entry point of the program. It imports the necessary classes and runs the calculator GUI.

### Classes

#### Calculator

The `Calculator` class provides methods to perform arithmetic calculations. It supports basic operations such as addition, subtraction, multiplication, and division.

#### UserInterface

The `UserInterface` class is responsible for providing an interactive user interface for the calculator. It utilizes the Tkinter library to create a graphical interface where users can enter numbers, choose an operation, and calculate the result.

#### AskAgain

The `AskAgain` class displays a message box to ask the user if they want to perform another calculation. If the user chooses to continue, the input fields are cleared, and the result label is reset. If the user decides to stop, a message box is shown to thank them for using the calculator, and the program is closed.