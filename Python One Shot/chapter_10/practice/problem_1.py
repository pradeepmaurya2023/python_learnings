# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    compamy = "Microsoft"

    def __init__(self,name):
        self.name = name

    def getInfo(self):
        print(f"Your name is {self.name} and You work at {self.compamy}")

programmer1 = Programmer("Pradeep")
programmer2 = Programmer("Tushar")
programmer3 = Programmer("Rohit")
programmer4 = Programmer("Ravi")

programmer1.getInfo()
