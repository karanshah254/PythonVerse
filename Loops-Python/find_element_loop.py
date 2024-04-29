number = [1, 2, 3, 4, 5]
search = 3
i = 0

while i < len(number):
    if number[i] == search:
        print("found at index", search)
        break
    else:
        print("finding")
    i += 1