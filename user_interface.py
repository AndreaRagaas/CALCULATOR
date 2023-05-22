#This User Interface will be the one that accepts the users input. 
#User Interface will also be the one that will execute the design/graphics of the calculator.

#Importing tkinter to design the calculator
import tkinter as tk

#Creating the class
class UserInterface:
    #Defining the User Interface attributions
    def __init__(self, calculator):
        self.calculator = calculator
        self.create_window() 