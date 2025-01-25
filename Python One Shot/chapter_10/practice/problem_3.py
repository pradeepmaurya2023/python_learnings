# 3. Create a class with a class attribute a; create an object from it and set ‘a’directly using ‘object.a = 0’. Does this change the class attribute?

class Testing:
    a = 20

newObj = Testing()

newObj.a = 0