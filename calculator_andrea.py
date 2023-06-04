#This will inherit the calculator functionalities, providing a pathway for enhancements and further improvements.

#Import all required modules
# Import the calculator
from calculator import Calculator
# Import the users interface and ask again
from user_interface import UserInterface, AskAgain
# Import the square root operation from math
from math import sqrt
# Importing tkinter for the upgraded design of the calculator
import tkinter as tk

# Creating the new class Andrea Improved Calculator
class Andrea_Improved_Calculator(Calculator, UserInterface):
    def __init__(self):
        # Initializing parent classes
        Calculator.__init__(self)
        UserInterface.__init__(self, self)

    def create_window(self):
        # Creating and enhancing the calculator window
        self.root = tk.Tk()
        self.root.title("IMPROVED CALCULATOR")

        # Creating an area for the user to enter numbers
        self.num1_label = tk.Label(self.root, text="ENTER THE FIRST NUMBER:")
        self.num1_entry = tk.Entry(self.root)
        self.num2_label = tk.Label(self.root, text="ENTER THE SECOND NUMBER:")
        self.num2_entry = tk.Entry(self.root)
        self.num1_label.grid(row=0, column=0, sticky="e")
        self.num1_entry.grid(row=0, column=1)
        self.num2_label.grid(row=1, column=0, sticky="e")
        self.num2_entry.grid(row=1, column=1)

        # Creating an area for the user to choose an operation
        self.operation_var = tk.StringVar(value="CHOOSE AN OPERATION")
        self.operation_dropdown = tk.OptionMenu(self.root, self.operation_var, "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "SQUARE", "SQUARE ROOT")
        self.operation_dropdown.grid(row=4, column=0, columnspan=2, pady=5)

        # Creating a button to calculate the user's input
        self.calculate_button = tk.Button(self.root, text="CALCULATE THE SUM/ DIFFERENCE/ PRODUCT/ QUOTIENT", command=self.calculate)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Creating an area to show the results
        self.result_label = tk.Label(self.root, text="RESULT:")
        self.result_label.grid(row=8, column=0, columnspan=2)

# Running the program
if __name__ == "__main__":
    calculator_andrea = Andrea_Improved_Calculator()
    calculator_andrea.create_window()