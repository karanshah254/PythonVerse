class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # methods/ function of class
    def hello(self):
        print("hello", self.name)

    def getMarks(self):
        return self.marks


s1 = Student("Karan Shah", 98)
# print("Name is", s1.name)
s1.hello()
print(s1.getMarks())
