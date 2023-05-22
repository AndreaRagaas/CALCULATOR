#The Calculator will be the one that will run the calculator.

#Importing the two classes
from calculator import Calculator
from user_interface import UserInterface

#Run the program
if __name__ == "__main__":
    calculator_gui = UserInterface(Calculator())