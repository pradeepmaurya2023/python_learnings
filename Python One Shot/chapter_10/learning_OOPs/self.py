# Creating a Employee class
# Name should be in Pascal Case
class Employee:
    # Class attribute
    name = "Kumar"
    language = "Python"
    salary = 1200000

    # Self  in Class
    def getInfo(self):
        print(f"Your name is {self.name} and You Code in {self.language} Language and Your salary is {self.salary}")

    def greet(self):
        print("Good Night")


# Object initiation
harry = Employee()

harry.getInfo()
# Employee.getInfo(harry)  it's same as above

harry.greet()