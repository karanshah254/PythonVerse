import math


def is_prime(n):
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(5))
