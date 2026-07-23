# ============================================
# TUPLES IN PYTHON
# ============================================

# A tuple is an ordered, immutable (cannot be changed)
# collection of items.
# Tuples are created using parentheses ()

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Original Tuple:")
print(fruits)

print()

# ============================================
# ACCESSING TUPLE ELEMENTS (INDEXING)
# ============================================

# Positive Indexing

print("Positive Indexing:")

print("fruits[0] =", fruits[0])
print("fruits[1] =", fruits[1])
print("fruits[4] =", fruits[4])

print()

# Negative Indexing

print("Negative Indexing:")

print("fruits[-1] =", fruits[-1])
print("fruits[-2] =", fruits[-2])
print("fruits[-5] =", fruits[-5])

print()

# ============================================
# TUPLE SLICING
# ============================================

print("Basic Slicing:")

print("fruits[0:2] =", fruits[0:2])
print("fruits[1:4] =", fruits[1:4])
print("fruits[:3] =", fruits[:3])
print("fruits[2:] =", fruits[2:])
print("fruits[:] =", fruits[:])

print()

# Step Value

print("Using Step:")

print("fruits[::2] =", fruits[::2])
print("fruits[::-1] =", fruits[::-1])

print()

# ============================================
# TUPLES ARE IMMUTABLE
# ============================================

print("Tuples are Immutable")

# The following statement will produce an error
# because tuple elements cannot be modified.

# fruits[1] = "Pineapple"

print("Tuple elements cannot be changed after creation.")

print()

# ============================================
# SEARCHING
# ============================================

numbers = (10, 20, 30, 20, 40)

print("Searching:")

print("20 in numbers =", 20 in numbers)
print("50 in numbers =", 50 in numbers)

print()

# ============================================
# index()
# Returns the first occurrence
# ============================================

print("index():")

print(numbers.index(20))

print()

# ============================================
# count()
# Counts occurrences
# ============================================

print("count():")

print(numbers.count(20))

print()

# ============================================
# LENGTH
# ============================================

print("Length:")

print(len(fruits))

print()

# ============================================
# MINIMUM, MAXIMUM AND SUM
# ============================================

values = (12, 45, 3, 28, 10)

print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))

print()

# ============================================
# ITERATING THROUGH A TUPLE
# ============================================

print("Using for loop:")

for fruit in fruits:
    print(fruit)

print()

# ============================================
# TUPLE CONCATENATION
# ============================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print("Concatenation:")

print(combined)

print()

# ============================================
# TUPLE REPETITION
# ============================================

repeat = ("Python",) * 3

print("Repetition:")

print(repeat)

print()

# ============================================
# SINGLE ELEMENT TUPLE
# ============================================

single = ("Apple",)

print("Single Element Tuple:")

print(single)

print(type(single))

print()

# Without comma, it is NOT a tuple

not_tuple = ("Apple")

print("Without Comma:")

print(not_tuple)

print(type(not_tuple))

print()

# ============================================
# TUPLE UNPACKING
# ============================================

student = ("Shyam", 24, "Python")

name, age, course = student

print("Tuple Unpacking:")

print(name)
print(age)
print(course)

print()

# ============================================
# NESTED TUPLES
# ============================================

nested = (
    ("Apple", "Banana"),
    ("Mango", "Orange")
)

print("Nested Tuple:")

print(nested)

print("Access Nested Element: ", nested[1][0])

print()

# ============================================
# CONVERT TUPLE TO LIST
# ============================================

tuple_data = (10, 20, 30)

list_data = list(tuple_data)

print("Tuple to List:")

print(list_data)

print(type(list_data))

print()

# ============================================
# CONVERT LIST TO TUPLE
# ============================================

list_numbers = [100, 200, 300]

tuple_numbers = tuple(list_numbers)

print("List to Tuple:")

print(tuple_numbers)

print(type(tuple_numbers))