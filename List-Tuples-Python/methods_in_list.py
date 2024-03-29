list = [2, 4, 1, 3]

# 1. add element at last
list.append(5)
print("After adding at last", list)

# 2. sort in ascending order
list.sort()
print("Ascending order ", list)

# 3. sorts in descending order
list.sort(reverse=True)
print("Descending order", list)

# 4. reverse a list
list.reverse()
print("After reversing", list)

# 5. insert at specific index
list.insert(2, 10)
print("After insertion at index 0 =", list)

# 6. removes first occurence of element
list.remove(10)
print("After removing value 10 =", list)

# 7. removes element at index
list.pop(2)
print("After removing at index 2 =", list)