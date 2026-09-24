class Student:
def __init__(self, name, grade):
self.name = name
self.grade = grade
def __str__(self):
return f"{self.name} is in grade {self.grade}"
Creating an object from the blueprint
a = Student("Bella", 10)
Printing the object automatically triggers the __str__ method
print(a)