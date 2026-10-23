# Approach 1 using __
"""
class Student:
    def __init__(self):
        self.__id = 123  # Here __ will make the field as private
        self.__name = "John"

    def display(self):
        print(self.__id)
        print(self.__name)


s = Student()
s.display()

print(s._Student__id)  # Name mangling to access private field
"""


# Approach 2 using getter & setter
class Student:
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


s = Student()
s.setId(123)
s.setName("John")
print(s.getId())
print(s.getName())
