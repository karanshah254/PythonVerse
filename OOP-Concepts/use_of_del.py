class Car:
    def __init__(self, name):
        self.name = name


car1 = Car("Rolls Royce")
print("Car 1 is", car1.name)
car2 = Car("Mercedes")
print("Car 2 is", car2.name)
del car2  # deleted object car2
print(car2.name)  # throws error
