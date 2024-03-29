studentInfo = {
    "name": "Karan",
    "age": 20,
    "learning": ["Python", "C", "Java", "JavaScript"],
    "marks": 96,
    "topic_covered": ("Dictionary", "Set"),
}

print("Total info:", studentInfo)
print("Age is", studentInfo["age"])
print("Student is learning", studentInfo["learning"])
print("Student name is", studentInfo["name"])
print("Student marks is", studentInfo["marks"])
print("Todays topic is:", studentInfo["topic_covered"])
print(type(studentInfo)) # dictionary