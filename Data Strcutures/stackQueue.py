# ============================================
# LIST AS STACK, QUEUE & LIST COMPREHENSION
# ============================================

# ============================================
# PART 1 - LIST AS A STACK (LIFO)
# Last In First Out
# ============================================

print("========== STACK ==========")

stack = []

print("Initial Stack:")
print(stack)
print()

# --------------------------------------------
# push() operation using append()
# --------------------------------------------

print("Adding Elements (Push)")

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)
print()

# --------------------------------------------
# Peek (Top Element)
# --------------------------------------------

print("Top Element")

print(stack[-1])

print()

# --------------------------------------------
# Pop Operation
# --------------------------------------------

print("Removing Top Element (Pop)")

removed = stack.pop()

print("Removed:", removed)
print("Stack:", stack)

print()

# --------------------------------------------
# Push More Elements
# --------------------------------------------

stack.append(50)
stack.append(60)

print("After Adding More Elements")
print(stack)

print()

# --------------------------------------------
# Pop Until Empty
# --------------------------------------------

print("Removing All Elements")

while len(stack) > 0:

    print("Removed:", stack.pop())

print("Stack:", stack)

print()

# ============================================
# PART 2 - LIST AS A QUEUE (FIFO)
# First In First Out
# ============================================

print("========== QUEUE ==========")

queue = []

print("Initial Queue")
print(queue)

print()

# --------------------------------------------
# Enqueue Operation
# --------------------------------------------

print("Adding Elements (Enqueue)")

queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")

print(queue)

print()

# --------------------------------------------
# Front Element
# --------------------------------------------

print("Front Element")

print(queue[0])

print()

# --------------------------------------------
# Dequeue Operation
# --------------------------------------------

print("Removing First Element (Dequeue)")

removed = queue.pop(0)

print("Removed:", removed)
print(queue)

print()

# --------------------------------------------
# Add More Elements
# --------------------------------------------

queue.append("E")
queue.append("F")

print("Queue After Adding More Elements")

print(queue)

print()

# --------------------------------------------
# Remove Everything
# --------------------------------------------

print("Removing All Elements")

while len(queue) > 0:

    print("Removed:", queue.pop(0))

print("Queue:", queue)

print()

# ============================================
# PART 3 - LIST COMPREHENSION
# ============================================

print("========== LIST COMPREHENSION ==========")

# --------------------------------------------
# Example 1
# --------------------------------------------

print("1. Squares")

numbers = [1,2,3,4,5]

squares = [x*x for x in numbers]

print(squares)

print()

# --------------------------------------------
# Example 2
# --------------------------------------------

print("2. Even Numbers")

evens = [x for x in range(1,21) if x % 2 == 0]

print(evens)

print()

# --------------------------------------------
# Example 3
# --------------------------------------------

print("3. Odd Numbers")

odds = [x for x in range(1,21) if x % 2 != 0]

print(odds)

print()

# --------------------------------------------
# Example 4
# --------------------------------------------

print("4. Convert to Uppercase")

names = ["vinay", "ravoof", "shyam", "lokesh", "udhay"]

upper_names = [name.upper() for name in names]

print(upper_names)

print()

# --------------------------------------------
# Example 5
# --------------------------------------------

print("5. Length of Each Word")

words = ["Python", "Java", "HTML"]

lengths = [len(word) for word in words]

print(lengths)

print()

# --------------------------------------------
# Example 6
# --------------------------------------------

print("6. Multiplication Table of 5")

table = [5 * x for x in range(1,11)]

print(table)

print()

# --------------------------------------------
# Example 7
# --------------------------------------------

print("7. Filter Numbers Greater Than 50")

numbers = [25,60,80,10,45,100]

greater = [x for x in numbers if x > 50]

print(greater)

print()

# --------------------------------------------
# Example 8
# --------------------------------------------

print("8. Replace Negative Numbers")

numbers = [-5,10,-2,15,-8]

positive = [0 if x < 0 else x for x in numbers]

print(positive)

print()

# --------------------------------------------
# Example 09
# --------------------------------------------

print("09. Nested Loop")

pairs = [(x, y) for x in range(1,4) for y in range(1,3)]

print(pairs)

print()

# ============================================
# Normal Loop vs List Comprehension
# ============================================

print("========== NORMAL LOOP vs LIST COMPREHENSION ==========")

print("Normal Loop")

numbers = []

for i in range(1,6):

    numbers.append(i*i)

print(numbers)

print()

print("List Comprehension")

numbers = [i*i for i in range(1,6)]

print(numbers)

print()

# ============================================
# Summary
# ============================================

print("========== SUMMARY ==========")

print("Stack")
print(" append() -> Push")
print(" pop()    -> Remove Last Element")

print()

print("Queue")
print(" append() -> Enqueue")
print(" pop(0)   -> Dequeue First Element")

print()

print("List Comprehension")
print(" [expression for item in iterable]")
print(" [expression for item in iterable if condition]")

print()

print("Program Completed Successfully!")