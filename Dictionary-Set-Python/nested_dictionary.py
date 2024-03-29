# nested dictionary
school = {
    "name": "Aone",
    "subject": {"physics": 90, "chemistry": 89, "maths": 96, "computer": 91},
    "location": "Ahmedabad",
}

print(school)
print(school["subject"])
print(school["subject"]["physics"]) # accessing nested objects