def main():
    x = getInt()
    print(f"Your number is {x}")


def getInt():
    while True:
        try:
            x = int(input("Please enter a number: "))
            return x
        except ValueError:
            print("Oops! That was no valid number. Try again...")
            pass


main()
