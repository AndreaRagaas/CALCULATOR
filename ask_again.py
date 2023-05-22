#This will contain the class where the user will be asked if still wanted to perform another calculation. 

#Importing a messagebox to ask the user
from tkinter import messagebox

#Creating the class
class AskAgain:
    #Defining the ask again's attributions
    def __init__(self, root, result_label, num1_entry, num2_entry):
        self.root = root
        self.result_label = result_label
        self.num1_entry = num1_entry
        self.num2_entry = num2_entry

    #Defining messagebox to ask the user
    def ask(self):
        answer = messagebox.askquestion("ANOTHER CALCULATION", "Do you want to perform another calculation?")     
        #If the user wants to perform another calculation
        if answer == "yes":
                self.result_label.config(text="Result:")
                self.num1_entry.delete(0, "end")
                self.num2_entry.delete(0, "end")