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
