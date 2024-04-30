def show(n):  # recurive function
    if n == 0:  # base case
        return
    print(n)
    show(n - 1)  # recursion call


show(5)
