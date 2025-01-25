class Employee:
    a = 25

    @classmethod
    def show(cls):
        print(f"The value of class attribute a is {cls.a}")

    
obj = Employee()
obj.a = 100

obj.show()