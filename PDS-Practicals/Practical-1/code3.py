my_string = "   Hello, World! Welcome to Python programming.   "

upper_string = my_string.upper()
lower_string = my_string.lower()
stripped_string = my_string.strip()
split_string = stripped_string.split()
joined_string = "-".join(split_string)
replaced_string = my_string.replace("World", "Universe")

first_character = my_string[0]
substring = my_string[7:12]


print("Original String: ", my_string)
print("Uppercase: '", upper_string)
print("Lowercase: '", lower_string)
print("Stripped: '", stripped_string)
print("Split: ", split_string)
print("Joined: '", joined_string)
print("Replaced: '", replaced_string)
print("First Character: '", first_character)
print("Substring: '", substring)
