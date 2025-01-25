# Creating a Employee class
# Name should be in Pascal Case
class Employee:
    # Class attribute
    name = "Kumar"
    language = "Python"
    salary = 1200000

# Object initiation
harry = Employee()

# Object attribute
harry.age = 22

# Overwriting Class Attribute with Instance Attribute
harry.name = "Harry"
print(harry.name, harry.salary)
print(harry.age)