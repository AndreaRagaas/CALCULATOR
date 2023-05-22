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

    #Designing the calculators interface
    def create_window(self):
        self.root = tk.Tk()
        self.root.title("SIMPLE CALCULATOR")
    
    #Creating an area for the users input
        self.num1_label = tk.Label(self.root, text="ENTER THE FIRST NUMBER: ")
        self.num1_entry = tk.Entry(self.root)
        self.num2_label = tk.Label(self.root, text="ENTER THE SECOND NUMBER: ")
        self.num2_entry = tk.Entry(self.root) 
        self.num1_label.grid(row=0, column=0, sticky="e")
        self.num1_entry.grid(row=0, column=1)
        self.num2_label.grid(row=1, column=0, sticky="e")
        self.num2_entry.grid(row=1, column=1)

    #Creating an area for the user to choose an operation
        self.operation_var = tk.StringVar(value="CHOOSE AN OPERATION")
        self.operation_dropdown = tk.OptionMenu(self.root, self.operation_var, "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE")
        self.operation_dropdown.grid(row=2, column=0, columnspan=2, pady=5)

    #Creating a button to calculate the users input
        self.calculate_button = tk.Button(self.root, text="CALCULATE", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=5)

    #Creating an area to show the results
        self.result_label = tk.Label(self.root, text="RESULT:")
        self.result_label.grid(row=4, column=0, columnspan=2)