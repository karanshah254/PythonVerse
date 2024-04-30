def fact(n):
    if n == 0 or n == 1:  # base case
        return 1
    else:
        return n * fact(n - 1)


print("Factorial of 5 is", fact(5))
