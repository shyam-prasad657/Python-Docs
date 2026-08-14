# ============================================
# STRUCT MODULE IN PYTHON
# pack() and unpack()
# ============================================


# ============================================
# 1. What is the struct module?
# ============================================

print("1. What is struct?")

print("The struct module is used to")
print("convert Python values into binary data")
print("and binary data back into Python values.")

print()

import struct

print("struct module imported successfully.")

print()


# ============================================
# 2. What is Binary Data?
# ============================================

print("2. Binary Data")

print("Computers store data as bytes.")
print("struct helps us work with binary data.")

number = 10

print("Normal Python number:", number)

print()


# ============================================
# 3. pack()
# ============================================

print("3. pack()")

print("pack() converts Python values into bytes.")

data = struct.pack("i", 10)

print("Original value:", 10)
print("Packed value  :", data)
print("Data type     :", type(data))

print()


# ============================================
# 4. Understanding the Format Code
# ============================================

print("4. Format Code")

print("The 'i' means integer.")

data = struct.pack("i", 100)

print("Value :", 100)
print("Bytes :", data)

print()


# ============================================
# 5. Different Format Codes
# ============================================

print("5. Common Format Codes")

print("i -> Integer")
print("f -> Float")
print("d -> Double")
print("c -> Character")
print("? -> Boolean")
print("h -> Short integer")
print("q -> Long integer")

print()


# ============================================
# 6. Packing an Integer
# ============================================

print("6. Packing Integer")

data = struct.pack("i", 25)

print("Original:", 25)
print("Packed  :", data)

print()


# ============================================
# 7. Packing a Float
# ============================================

print("7. Packing Float")

data = struct.pack("f", 25.5)

print("Original:", 25.5)
print("Packed  :", data)

print()


# ============================================
# 8. Packing a Boolean
# ============================================

print("8. Packing Boolean")

data = struct.pack("?", True)

print("Original:", True)
print("Packed  :", data)

print()


# ============================================
# 9. Packing a Character
# ============================================

print("9. Packing Character")

data = struct.pack("c", b"A")

print("Original:", b"A")
print("Packed  :", data)

print()


# ============================================
# 10. Packing Multiple Values
# ============================================

print("10. Packing Multiple Values")

data = struct.pack("if", 10, 25.5)

print("Integer:", 10)
print("Float  :", 25.5)
print("Packed :", data)

print()


# ============================================
# 11. pack() with Multiple Integers
# ============================================

print("11. Multiple Integers")

data = struct.pack("iii", 10, 20, 30)

print("Original values:", 10, 20, 30)
print("Packed values  :", data)

print()


# ============================================
# 12. unpack()
# ============================================

print("12. unpack()")

print("unpack() converts bytes back")
print("into Python values.")

data = struct.pack("i", 100)

value = struct.unpack("i", data)

print("Packed data :", data)
print("Unpacked    :", value)

print()


# ============================================
# 13. unpack() Returns a Tuple
# ============================================

print("13. unpack() returns a tuple")

data = struct.pack("i", 100)

value = struct.unpack("i", data)

print("Value:", value)
print("Type :", type(value))

print()


# ============================================
# 14. Getting the Actual Value
# ============================================

print("14. Getting Actual Value")

data = struct.pack("i", 100)

value = struct.unpack("i", data)

print("Tuple:", value)
print("Actual number:", value[0])

print()


# ============================================
# 15. Packing and Unpacking Multiple Values
# ============================================

print("15. Multiple Values")

data = struct.pack("if", 10, 25.5)

print("Packed:", data)

values = struct.unpack("if", data)

print("Unpacked:", values)

print("Integer:", values[0])
print("Float  :", values[1])

print()

# ============================================
# 17. Packing Different Data Types
# ============================================

print("17. Different Data Types")

age = 24
height = 171.5
is_student = True

data = struct.pack("if?", age, height, is_student)

print("Original values:")
print(age)
print(height)
print(is_student)

print()

print("Packed:", data)

print()


# ============================================
# 18. Unpacking Different Data Types
# ============================================

print("18. Unpacking Different Data Types")

values = struct.unpack("if?", data)

print("Unpacked values:", values)

print("Age       :", values[0])
print("Height    :", values[1])
print("Is Student:", values[2])

print()