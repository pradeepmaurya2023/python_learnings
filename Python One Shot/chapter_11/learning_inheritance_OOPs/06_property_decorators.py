class Employee:
    a = 25

    @classmethod
    def show(cls):
        print(f"The value of class attribute a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split( " ")[0]
        self.lname = value.split( " ")[1]
    
obj = Employee()

obj.name = "Pradeep Kumar"

print(obj.name)