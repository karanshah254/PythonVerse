# 1. Enter name of 3 movies and adds then to a list
# movie1 = input("Enter movie 1 : ")
# movie2 = input("Enter movie 2 : ")
# movie3 = input("Enter movie 3 : ")

# movieList = []
# movieList.append(movie1)
# movieList.append(movie2)
# movieList.append(movie3)
# print("Movie list is =", movieList)

# 2. check list contais palindrome of elements
list = [1, 2, 3]
print("Original list =", list)
copyList = list.copy()
copyList.reverse()
print("Reverse List =", copyList)
if copyList == list:
    print("List is Palidrome")
else:
    print("List is Not Palidrome")

# 3. Count number of students with grade 'A' in tuple
tuple = ("C", "D", "A", "A", "B")
print("\nNumber of grade 'A' =", tuple.count("A"))
