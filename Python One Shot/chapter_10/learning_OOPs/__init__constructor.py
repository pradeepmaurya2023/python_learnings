# Creating a Employee class
# Name should be in Pascal Case
class Employee:
    # Class attribute
    language = "Python"
    salary = 1200000

    # constructor called automatically
    # a dunder method which starts with __
    def __init__(self,name,salary):
        self.name = name


# Object initiation
employee1 = Employee("Pradeep",1300000)

print(employee1.name)
print(employee1.salary)
