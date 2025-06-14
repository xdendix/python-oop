class Student:
    def __init__(self, name, age):  # constructor
        self.name = name  # name of the student
        self.age = age  # age of the student

    def __str__(self):  # overloading the str() function
        return f"student name: {self.name}, age: {self.age}"  # this will be called when str() is used on an instance of Student


s1 = Student("Alice", 20)  # creating an instance of Student
print(s1)  # this will call the __str__ method
