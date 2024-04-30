number = int(input("Enter number: "))

def factorial(num):
    fact = 1
    for value in range(1, number + 1):
        fact = fact * value
    return fact

print("Factorial of", number, "is", factorial(number))