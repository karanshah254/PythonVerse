import numpy as np


def genrate_matrix(X, Y):
    array = np.zeros((X, Y), dtype=int)
    for i in range(X):
        for j in range(Y):
            array[i][j] = i * j
    return array


X = int(input("Enter number of rows: "))
Y = int(input("Enter number of columns: "))

result = genrate_matrix(X, Y)
print(result)
