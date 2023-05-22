#This Calculator file will contain the function of each operation buttons

#Creating the class
class Calculator:
    #Defining the function of each operations
    #To Add
    def add(self, num1, num2):
        return ("SUM: " + str(num1 + num2))
    
    #To Subtract
    def subtract(self, num1, num2):
        return ("DIFFERENCE: " + str(num1 - num2))
    
    #To Multiply
    def multiply(self, num1, num2):
        return ("PRODUCT: " + str(num1 * num2))
    
    #To Divide
    def divide(self, num1, num2):
        if num2 != 0:
            return ("QUOTIENT: " + str(num1 / num2))
        else:
            raise ZeroDivisionError("Cannot divide by zero")