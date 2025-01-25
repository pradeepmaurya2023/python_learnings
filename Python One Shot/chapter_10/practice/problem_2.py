# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    num = 0

    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"Square of {self.num} is {self.num*self.num}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num*self.num*self.num}")
    def square_root(self):
        print(f"Square of {self.num} is {self.num**(1/2)}")

num1 = Calculator(25)

num1.square()
num1.cube()
num1.square_root()
