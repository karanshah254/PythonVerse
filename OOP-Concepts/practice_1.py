# Create a student class that takes name and marks of 3 students and write a method to print average


class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def find_average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3


student1 = Student("John", 98, 95, 96)
print("Average marks of", student1.name, "is", student1.find_average())
