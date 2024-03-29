school = {
    "name": "Aone",
    "subject": {"physics": 90, "chemistry": 89, "maths": 96, "computer": 91},
    "location": "Ahmedabad",
}

print("Keys are:", list(school.keys()))  # returns all keys
print("Value are:", list(school.values()))  # return values
print("(Key,value) pair:", list(school.items()))  # return (key,value) pair as tuples
print(
    "Value at key is", school.get("location")
)  # return value at specified key else None
print(
    "Updated Dictionary is", school.update({"Field": ["Science", "Commerce"]})
)  # Updated original dictionary with new key:value pair
print(school)
