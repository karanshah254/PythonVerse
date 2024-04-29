number = int(input("Enter number: "))
fact = 1
for value in range(1, number + 1):
    fact = fact * value

print("Factorial of", number, "is", fact)
