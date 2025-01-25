class Employee:
    company = "ITC"
    name = "Harry"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"

    def showLanguage(self):
        print(f"You code in {self.language} language")
        return


# Inheriting Employee class in Programmer class
class Programmer(Employee,Coder):

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
        return


a = Employee()
b = Programmer()

print(b.name)
print(b.showLanguage())