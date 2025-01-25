# 4. Add a static method in problem 2, to greet the user with hello.
import math

class Calculator:
    num = 0

    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"Square of {self.num} is {self.num*self.num}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num*self.num*self.num}")
    def square_root(self):
        print(f"Square of {self.num} is {math.sqrt(self.num)}")

    @staticmethod
    def greet():
        print("Hello ")

num1 = Calculator(25)

num1.greet()
num1.square()
num1.cube()
num1.square_root()

