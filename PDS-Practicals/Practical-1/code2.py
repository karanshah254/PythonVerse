# 1. Conditional Statements
a = int(input("Enter a number: "))
if a > 0:  # if statement
    print("Positive")

a = int(input("Enter year to check leap year: "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:  # if-else statement
    print("Leap Year")
else:
    print("Not a Leap Year")

# 2. Loops
print("\nFor loop")
for i in range(1, 10):
    print(i, end=" ")

print("\nWhile loop")
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

# 3. Functions
a = 11
b = 22


def add(a, b):
    return a + b


print(f"\nSum of {a} and {b} is {add(a, b)}")
