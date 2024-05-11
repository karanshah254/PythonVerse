class Car:

    def __init__(self, modelName):
        self.name = modelName

    @staticmethod  # decorator
    def hello():
        print("hello world")


car1 = Car("Rolls Royce")
print(car1.name)
car1.hello()
