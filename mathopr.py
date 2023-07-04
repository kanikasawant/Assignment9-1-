import math 
class MathOperations:
    def __init__(self,num1=0,num2=0):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return(self.num1 + self.num2)
        
    def subtract(self):
        return(self.num1 - self.num2)
        
    def multiply(self):
        return(self.num1 * self.num2)
        
    def divide(self):
        if self.num2 != 0:
            return (self.num1 // self.num2)
        else:
            raise ZeroDivisionError("Cannot divide by zero!")
    def square_root(self):
        if self.num1 >= 0:
            return( math.sqrt(self.num1))
        else:
            raise ValueError("Cannot calculate square root of a negative number!")
    
    def sincalculate(self):
        return math.sin(self.num1) , math.sin(self.num2)