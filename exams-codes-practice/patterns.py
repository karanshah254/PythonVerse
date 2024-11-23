# 1
# *
# * *
# * * *
# * * * *
for rows in range(5):
    for colums in range(rows):
        print("*", end=" ")
    print()


# 2
# $ $ $ $
# $ $ $
# $ $
# $
print()
for rows in range(4):
    for colums in range(4 - rows):
        print("$", end=" ")
    print()


# 3
# # # # #
# # #
#
# # #
# # # # #
print()
for i in range(5):
    if i <= 5 // 2:
        print("# " * (5 - 2 * i))
    else:
        print("# " * (2 * i - 3))


# 4
# 0 0 0 0 0
#   0 0 0
#     0
#   0 0 0
# 0 0 0 0 0
print()
n = 5  # only works for odd number of rows
k = n
for row in range(n, 0, -1):
    if row >= 3:
        print(" " * (n - row), end="")
    else:
        print(" " * (row - 1), end="")
    print("0" * k)

    if row <= 3:
        k += 2
    else:
        k -= 2
