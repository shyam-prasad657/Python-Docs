# ==========================================
# DICTIONARY METHODS IN PYTHON
# ==========================================

# Creating a dictionary
student = {
    "name": "Shyam",
    "age": 24,
    "course": "Python"
}

print("Original Dictionary:")
print(student)
print()

# ------------------------------------------
# 1. get() - Returns the value of a key
# ------------------------------------------
print("1. get()")
print(student.get("name"))          # Existing key
print(student.get("city"))          # Key doesn't exist
print(student.get("city", "Not Found"))  # Default value
print()

# ------------------------------------------
# 2. keys() - Returns all keys
# ------------------------------------------
print("2. keys()")
print(student.keys())
print()

# ------------------------------------------
# 3. values() - Returns all values
# ------------------------------------------
print("3. values()")
print(student.values())
print()

# ------------------------------------------
# 4. items() - Returns key-value pairs
# ------------------------------------------
print("4. items()")
print(student.items())
print()

# ------------------------------------------
# 5. update() - Updates dictionary
# ------------------------------------------
print("5. update()")

student.update({"age": 25, "city": "Chennai"})

print(student)
print()

# ------------------------------------------
# 6. pop() - Removes a specific key
# ------------------------------------------
print("6. pop()")

removed = student.pop("city")

print("Removed Value:", removed)
print(student)
print()

# ------------------------------------------
# 7. popitem() - Removes last inserted item
# ------------------------------------------
print("7. popitem()")

last_item = student.popitem()

print("Removed Item:", last_item)
print(student)
print()

# ------------------------------------------
# 8. setdefault() - Returns value if key exists,
# otherwise inserts key with default value
# ------------------------------------------
print("8. setdefault()")

student.setdefault("country", "India")

print(student)

student.setdefault("country", "USA")  # Won't overwrite

print(student)
print()

# ------------------------------------------
# 9. copy() - Creates a copy
# ------------------------------------------
print("9. copy()")

student_copy = student.copy()

print(student_copy)
print()

# ------------------------------------------
# 10. fromkeys() - Creates a new dictionary
# ------------------------------------------
print("10. fromkeys()")

keys = ["Math", "Science", "English"]

marks = dict.fromkeys(keys, 0)

print(marks)
print()

# ------------------------------------------
# 11. clear() - Removes all items
# ------------------------------------------
print("11. clear()")

marks.clear()

print(marks)
print()

# ------------------------------------------
# 12. len() - Number of key-value pairs
# ------------------------------------------
print("12. len()")

print(len(student))
print()

# ------------------------------------------
# 13. in - Check if key exists
# ------------------------------------------
print("13. in (Membership Operator)")

print("name" in student)
print("salary" in student)
print()

# ------------------------------------------
# 14. del - Delete a key
# ------------------------------------------
print("14. del")

del student["country"]

print(student)
print()

# ------------------------------------------
# 15. Access using []
# ------------------------------------------
print("15. Access using []")

print(student["name"])
print()

# ------------------------------------------
# 16. Modify a value
# ------------------------------------------
print("16. Modify Value")

student["age"] = 30

print(student)
print()

# ------------------------------------------
# 17. Add a new key-value pair
# ------------------------------------------
print("17. Add New Key")

student["salary"] = 50000

print(student)
print()

# ------------------------------------------
# 18. Loop through keys
# ------------------------------------------
print("18. Loop through Keys")

for key in student:
    print(key)

print()

# ------------------------------------------
# 19. Loop through values
# ------------------------------------------
print("19. Loop through Values")

for value in student.values():
    print(value)

print()

# ------------------------------------------
# 20. Loop through items
# ------------------------------------------
print("20. Loop through Items")

for key, value in student.items():
    print(key, ":", value)

print()

print('items()',student.items())