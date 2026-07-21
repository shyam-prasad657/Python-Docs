# ============================================
# LISTS IN PYTHON
# ============================================

# A list is an ordered, mutable (changeable)
# collection of items.
# Lists are created using square brackets []

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Original List:")
print(fruits)

print()

# ============================================
# ACCESSING LIST ELEMENTS (INDEXING)
# ============================================

# Positive Indexing
print("Positive Indexing:")
print("fruits[0] =", fruits[0])

print()

# Negative Indexing
print("Negative Indexing:")
print("fruits[-1] =", fruits[-1])

print()

# ============================================
# LIST SLICING
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
# UPDATING LIST ITEMS
# ============================================

print("Updating List:")

fruits[1] = "Pineapple"

print(fruits)

print()

# ============================================
# ADDING ITEMS
# ============================================

# append()
# Adds an item at the end

fruits.append("Watermelon")

print("append():")
print(fruits)

print()

# insert()
# Inserts an item at a specific index

fruits.insert(2, "Kiwi")

print("insert():")
print(fruits)

print()

# extend()
# Adds multiple items

fruits.extend(["Cherry", "Papaya"])

print("extend():")
print(fruits)

print()

# ============================================
# REMOVING ITEMS
# ============================================

# remove()
# Removes by value

fruits.remove("Orange")

print("remove():")
print(fruits)

print()

# pop()
# Removes by index
# Returns the removed item

removed = fruits.pop(2)

print("pop():")
print("Removed:", removed)
print(fruits)

print()

# pop() without index removes the last item

last = fruits.pop()

print("pop() Last Item:")
print("Removed:", last)
print(fruits)

print()

# del
# Deletes using index or slice

del fruits[0]

print("del:")
print(fruits)

print()

# clear()
# Removes all items

temp = ["A", "B", "C"]

temp.clear()

print("clear():")
print(temp)

print()

# ============================================
# SEARCHING
# ============================================

numbers = [10, 20, 30, 20, 40]

print("Searching:")

print("20 in numbers =", 20 in numbers)
print("50 in numbers =", 50 in numbers)

print()

# index()
# Returns the first matching index

print("index():")
print(numbers.index(20))

print()

# count()
# Counts occurrences

print("count():")
print(numbers.count(20))

print()

# ============================================
# SORTING
# ============================================

marks = [65, 92, 45, 81, 76]

print("Original Marks:")
print(marks)

print()

# sort()

marks.sort()

print("sort() Ascending:")
print(marks)

print()

marks.sort(reverse=True)

print("sort() Descending:")
print(marks)

print()

# reverse()

marks.reverse()

print("reverse():")
print(marks)

print()

# ============================================
# COPYING LIST
# ============================================

copy_marks = marks.copy()

print("copy():")
print(copy_marks)
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

values = [12, 45, 3, 28, 10]

print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))

print()

# ============================================
# ITERATING THROUGH A LIST
# ============================================

print("Using for loop:")

for fruit in fruits:
    print(fruit)

print()

# ============================================
# LIST CONCATENATION
# ============================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2

print("Concatenation:")
print(combined)

print()

# ============================================
# LIST REPETITION
# ============================================

repeat = ["Python"] * 3

print("Repetition:")
print(repeat)