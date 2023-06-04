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

# Running the program
if __name__ == "__main__":
    calculator_andrea = Andrea_Improved_Calculator()