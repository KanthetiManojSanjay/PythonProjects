class Student:
    major="CSE"
    def __init__(self,name, rollno):
        self.name = name
        self.rollno = rollno

s1=Student("John", 1)
s2=Student("Bill", 2)

print(s1.major) #Static variable can be accessed using object as well
print(s2.major)

print(s1.name)
print(s2.name)

print(Student.major) #Static variable can be accessed using className
