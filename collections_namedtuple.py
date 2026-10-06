#named tuple
from collections import namedtuple
Student=namedtuple("Student", ["name","age","marks"])
name=input("Enter name:")
age=int(input("Enter age:"))
marks=int(input("Enter marks:"))
s=Student(name,age,marks)
print("Student",s)
print("Name:",s.name)
print("Marks:",s.marks)