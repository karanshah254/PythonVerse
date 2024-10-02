# conntrol structures
age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

for i in range(1, 10):
    print(i, end=" ")


def add(a=10, b=5):
    return a + b


# strings in python
str1 = "   kAraN  "
print(str1.upper())
print(str1.lower())
print(str1.strip())
print(str1.replace("r", "V"))
print(str1.split("a"))
print(str1.join("123"))
print(str[0:3])


# tuples in python
tup = (1, 2, 3, 4, 5)
print(tup[0])
print(tup[1:3])


# lists in python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1]
print(list1[0])
print(list1[1:3])
list1.append(6)
list1.insert(2, 7)
list1.remove(3)
list1.pop()
list1.extend([11, 12, 13])
list1.sort()


# dictionaries in python
dictionary = {"name": "Alice", "age": 20, "marks": 90}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
del dictionary["name"]
print(dictionary.pop("age"))


# sets in python
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {1, 2, 3, 4, 5}
print(set1.add(11))
print(set1.remove(1))
print(set1.pop())
print(set1.union(set2))
print(set1.intersection(set2))
