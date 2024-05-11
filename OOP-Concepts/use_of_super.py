class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")


class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name


car1 = Toyota("Fortuner", "Diesel")
print(car1.type)
