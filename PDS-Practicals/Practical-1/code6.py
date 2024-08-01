my_dict = {"name": "Karan", "age": 20, "city": "Ahmedabad", "number": "124"}


name = my_dict["name"]
age = my_dict["age"]


keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()


my_dict["age"] = 31
my_dict["email"] = "developer@example.com"


del my_dict["number"]
city = my_dict.pop("city")


print(
    "Original Dictionary: ",
    {"name": "Karan", "age": 20, "city": "Ahmedabad", "number": "124"},
)
print("Name: ", name)
print("Age: ", age)
print("Keys: ", keys)
print("Values: ", values)
print("Items: ", items)
print("Modified Dictionary: ", my_dict)
print("Removed City: ", city)
