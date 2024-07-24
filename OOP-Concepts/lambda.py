people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

# Sort the list of dictionaries by the value of the key 'name'
people.sort(key=lambda person: person["name"])

# Sort the list of dictionaries by the value of the key 'name'
# people.sort(key=lambda person: person["house"])

print(people)
