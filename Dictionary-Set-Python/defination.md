1. Dictionary in Python:
- >Dictionary are used to store data values in key:value pair. They are unorderes, mutable and don't allow duplicate keys. 
```python
dict = {
    "name": "John",
    "age": 45,
    "marks": [98,96,94]
}
```

2. Nested Dictionary:
```python
school = {
    "name": "Aone School of Science",
    "subject": {"physics": 90, "chemistry": 89, "maths": 96, "computer": 91},
    "location": "Ahmedabad",
}

print(school)
print(school["subject"])
print(school["subject"]["physics"]) # accessing nested values
```

3. Set in Python:
- >Set is collection of unordered items. Each item is unique and immutable.