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

        # Creating an entry section for the numbers that the user wanted to get the square or the squareroot 
        self.new_entry_label = tk.Label(self.root, text="ENTER A NUMBER TO GET THE SQUARE/ SQUAREROOT:")
        self.new_entry_entry = tk.Entry(self.root)
        self.new_entry_label.grid(row=2, column=0, sticky="e")
        self.new_entry_entry.grid(row=2, column=1)

        # Creating buttons to perform additional operations
        self.additional_ops_button = tk.Button(self.root, text="CALCULATE FOR THE SQUARE", command=self.additional_operations)
        self.additional_ops_button.grid(row=6, column=0, columnspan=2, pady=5)
        self.additional_ops_button1 = tk.Button(self.root, text="CALCULATE FOR THE SQUAREROOT", command=self.additional_operations)
        self.additional_ops_button1.grid(row=7, column=0, columnspan=2, pady=5)

        # To ask the user
        self.ask_again = AskAgain(self.root, self.result_label, self.num1_entry, self.num2_entry)

        self.root.mainloop()

    #Defining the function buttons to calculate with the choosen operation
    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            num3 = float(self.new_entry_entry.get())
            operation = self.operation_var.get()

            if operation == "ADD":
                result = self.add(num1, num2)
            elif operation == "SUBTRACT":
                result = self.subtract(num1, num2)
            elif operation == "MULTIPLY":
                result = self.multiply(num1, num2)
            elif operation == "DIVIDE":
                result = self.divide(num1, num2)
            elif operation == "SQUARE":
                result = self.square(num3)
            elif operation == "SQUARE ROOT":
                result = self.square_root(num3)

            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Invalid input, please try again")
        except ZeroDivisionError as e:
            self.result_label.config(text=str(e))

        self.ask_again.ask()
        
    # The additional features/operations
    def additional_operations(self):
        try:
            num3 = float(self.new_entry_entry.get())
            operation = self.operation_var.get()

            if operation == "SQUARE":
                result = self.square(num3)
            elif operation == "SQUARE ROOT":
                result = self.square_root(num3)

            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Invalid input, please try again")

    # For the Square Root
    def square_root(self, num3):
        if num3 >= 0:
            return "SQUARE ROOT: " + str(sqrt(num3))
        else:
            return "Invalid input, cannot calculate the square root of a negative number"

    # For the Square
    def square(self, num3):
        return "SQUARE: " + str(num3 * num3)

# Running the program
if __name__ == "__main__":
    calculator_andrea = Andrea_Improved_Calculator()
    calculator_andrea.create_window()