class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and Comapny NAME IS : {self.company}")

    @classmethod
    def changeCompany(cls,name):
        cls.company = name

e1 = Employee()
e1.name = "Kumar"
e1.show()
e1.company = "Tesla"
e1.show()
e1.changeCompany("HP")
e1.show()
Employee.changeCompany("Google")

print(Employee.company)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_full_name(cls, full_name, age):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name, age)

    @classmethod
    def from_dict(cls, data):
        return cls(data['first_name'], data['last_name'], data['age'])

# Creating an instance using the primary constructor
person1 = Person("John", "Doe", 30)

# Creating an instance using the additional constructor from_full_name
person2 = Person.from_full_name("Jane Doe", 25)

# Creating an instance using the additional constructor from_dict
person3 = Person.from_dict({"first_name": "Jim", "last_name": "Beam", "age": 40})

print(person1.first_name, person1.last_name, person1.age)  # Output: John Doe 30
print(person2.first_name, person2.last_name, person2.age)  # Output: Jane Doe 25
print(person3.first_name, person3.last_name, person3.age)  # Output: Jim Beam 40
