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
print(harry.name, harry.salary)
print(harry.age)

print(hasattr(harry,'name'))
print(getattr(harry,'name'))
setattr(harry,'name','Pradeep')
print(getattr(harry,'name'))
delattr(harry.salary)
print(getattr(harry,'salary'))