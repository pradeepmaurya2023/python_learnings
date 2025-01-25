class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

obj = Manager()

print(obj.a)
print(obj.b)
print(obj.c)
