class Car:
    carType = "Luxury"  # class attribute

    def __init__(self, modelName, price):
        # object attribute
        self.name = modelName
        self.price = price
        print("constructor is called")


car1 = Car("Rolls Royce", "10CR")
print("Model name is", car1.name, "and price is", car1.price)

car2 = Car("Mercedes", "1CR")
print("Model name is", car2.name, "and price is", car2.price)
print("Type of Car is", Car.carType)
