# ============================================
# Basic String Methods and String Formatting
# ============================================

# Store a string in a variable
name = "Shyam Prasad"

# Original String
print("Original String:")
print(name)

print()

# upper()
# Converts all characters to uppercase
print("Uppercase:")
print(name.upper())

print()

# lower()
# Converts all characters to lowercase
print("Lowercase:")
print(name.lower())

print()

# title()
# Converts the first letter of every word to uppercase
print("Title Case:")
print(name.title())

print()

# capitalize()
# Capitalizes only the first letter of the string
print("Capitalized:")
print(name.capitalize())

print()

# replace()
# Replaces one part of the string with another
print("Replace:")
print(name.replace("Shyam", "Rahul"))

print()

# find()
# Returns the index of the first occurrence
# Returns -1 if not found
print("Find:")
print(name.find("Prasad"))

print()

# count()
# Counts how many times a substring appears
print("Count:")
print(name.count("a"))

print()

# startswith()
# Checks if the string starts with a given value
# Returns True or False
print("Starts With:")
print(name.startswith("Shyam"))

print()

# endswith()
# Checks if the string ends with a given value
# Returns True or False
print("Ends With:")
print(name.endswith("Prasad"))

print()

# strip()
# Removes leading and trailing spaces
text = "   Hello Python   "
print("Strip:")
print(text.strip())

print()

# ============================================
# STRING FORMATTING
# ============================================
first_name = "Shyam"
age = 25
language = "Python"

# Method 1: Using commas in print()
print("Using commas:")
print("Name:", first_name, "Age:", age)

print()

# Method 2: String Concatenation (+)
# Strings only! Numbers must be converted.
print("Using + operator:")
print("Name: " + first_name)

print()

# Method 3: format() method
print("Using format():")
print("My name is {} and I am {} years old.".format(first_name, age))

print()

# Method 4: f-Strings (Recommended)
# Place variables inside {}
print("Using f-Strings:")
print(f"My name is {first_name}.")
print(f"I am {age} years old.")
print(f"I am learning {language}.")

print()

# Formatting Numbers
price = 1499.5678

print("Formatted Price:")
print(f"Price: ₹{price:.2f}")