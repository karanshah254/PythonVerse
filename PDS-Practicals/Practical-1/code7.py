my_set = {1, 2, 3, 4, 5}


my_set.add(6)
my_set.add(3)
my_set.remove(2)
popped_element = my_set.pop()


another_set = {4, 5, 6, 7, 8}


union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)


print("Original Set: ", {1, 2, 3, 4, 5})
print("Modified Set: ", my_set)
print("Popped Element: ", popped_element)
print("Another Set: ", another_set)
print("Union of Sets: ", union_set)
print("Intersection of Sets: ", intersection_set)
