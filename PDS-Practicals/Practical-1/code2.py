# 1. Conditional Statements in python
# if statement
a = int(input("Enter a number: "))
if a > 0:
    print("Positive")

# if-else statement
a = int(input("Enter year to check leap year: "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# 2. Loops in python
# for loop
print("For loop")
for i in range(1, 10):
    print(i)

# while loop
print("While loop")
i = 0
while i < 10:
    print(i)
    i += 1


# 3. Functions in python
def add(a, b):
    return a + b


print("Using functions sum of two numbers are", add(2, 3))
