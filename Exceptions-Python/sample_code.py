while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    else:
        break

print(f"Your number is {x}")
