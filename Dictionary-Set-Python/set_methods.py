empty_set = set()
print("Before :", empty_set)

# methods
empty_set.add(10)
empty_set.add(12)
empty_set.add(40)
empty_set.remove(12)
empty_set.add("Karan")
empty_set.add("Hello world")
# empty_set.clear()  # clears the set
print("After :", empty_set)


collection = {"Hello", "World", "Learn", "Python", "Coding"}
print("Randomm element poped is", collection.pop())  # removes random element