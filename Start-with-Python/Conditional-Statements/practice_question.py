# 1. check even odd number
number = int(input("Enter a number : "))
if number % 2 == 0:
    print("even")
else:
    print("odd")


# 2. find greatest of 3 numbers
number1 = int(input("\nEnter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if number1 > number2 and number1 > number3:
    print("number1 is greatest", number1)
elif number2 > number3:
    print("number2 is greatest", number2)
else:
    print("number3 is greatest", number3)


# 3. Check year is leap year or not
year = int(input("\nEnter year : "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
