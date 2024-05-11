class Person:
    name = "abcd"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person("Karan Shah")
print(p1.name)
print(Person.name)
