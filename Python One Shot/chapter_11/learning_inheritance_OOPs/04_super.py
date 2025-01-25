class Employee:
    a = 1
    def __init__(self):
        print("I am a constructor of Employee class")

class Programmer(Employee):
    b = 2
    def __init__(self):
        super().__init__()
        print("I am a constructor of Programmer class")

    def greet(self):
        print("Good Morning")

class Manager(Programmer):
    c = 3
    def __init__(self):
        super().__init__()
        super().greet()
        print("I am a constructor of Manager class")

obj = Manager()

print(obj.a)
print(obj.b)
print(obj.c)
