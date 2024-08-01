my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


first_element = my_list[0]
last_element = my_list[-1]
third_element = my_list[2]


first_three_elements = my_list[0:3]
middle_elements = my_list[3:7]
last_three_elements = my_list[-3:]


my_list.append(110)
my_list.insert(3, 35)
my_list.remove(70)
popped_element = my_list.pop()
my_list.extend([120, 130, 140])
my_list.sort()


print("Original List: ", [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("First Element: ", first_element)
print("Last Element: ", last_element)
print("Third Element: ", third_element)
print("First Three Elements: ", first_three_elements)
print("Middle Elements: ", middle_elements)
print("Last Three Elements: ", last_three_elements)
print("Modified List: ", my_list)
print("Popped Element: ", popped_element)
