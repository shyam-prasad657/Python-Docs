# ============================================
# FILE HANDLING IN PYTHON
# Reading & Writing Files
# ============================================

# ============================================
# 1. Creating and Writing to a File (write)
# ============================================

print("1. Writing to a File")

file = open("sample.txt", "w")

file.write("Hello, Welcome to Python!\n")
file.write("This is the second line.\n")

file.close()

print("Data written successfully.\n")


# ============================================
# 2. Reading an Entire File (read)
# ============================================

print("2. Reading Entire File")

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

print()


# ============================================
# 3. Reading One Line (readline)
# ============================================

print("3. Reading One Line")

file = open("sample.txt", "r")

print(file.readline())
print(file.readline())

file.close()

print()


# ============================================
# 4. Reading All Lines (readlines)
# ============================================

print("4. Reading All Lines")

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()

print()


# ============================================
# 5. Loop Through a File
# ============================================

print("5. Loop Through File")

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()

print()


# ============================================
# 6. Appending Data (append)
# ============================================

print("6. Appending Data")

file = open("sample.txt", "a")

file.write("This line was appended.\n")

file.close()

print("New data added.\n")


# ============================================
# 7. Reading After Append
# ============================================

print("7. Reading Updated File")

file = open("sample.txt", "r")

print(file.read())

file.close()

print()


# ============================================
# 8. Using with Statement (Recommended)
# Automatically closes the file
# ============================================

print("8. Using with")

with open("sample.txt", "r") as file:
    print(file.read())

print()


# ============================================
# 9. Writing Multiple Lines (writelines)
# ============================================

print("9. writelines()")

lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("languages.txt", "w") as file:
    file.writelines(lines)

print("languages.txt created.\n")


# ============================================
# 10. Reading languages.txt
# ============================================

print("10. Reading languages.txt")

with open("languages.txt", "r") as file:
    print(file.read())

print()


# ============================================
# 11. File Modes
# ============================================

print("11. File Modes")

print("r  -> Read")
print("w  -> Write (Overwrites file)")
print("a  -> Append")
print("x  -> Create new file")
print("r+ -> Read and Write")
print("w+ -> Write and Read")
print("a+ -> Append and Read")

print()


# ============================================
# 12. Checking File Position
# ============================================

print("12. tell()")

with open("sample.txt", "r") as file:

    print(file.tell())

    file.read(10)

    print(file.tell())

print()


# ============================================
# 13. Moving File Pointer
# ============================================

print("13. seek()")

with open("sample.txt", "r") as file:

    file.seek(6)

    print(file.read())

print()


# ============================================
# 14. Reading Specific Characters
# ============================================

print("14. Reading Specific Characters")

with open("sample.txt", "r") as file:

    print(file.read(5))

print()


# ============================================
# 15. Checking File Properties
# ============================================

print("15. File Properties")

with open("sample.txt", "r") as file:

    print("Name     :", file.name)
    print("Mode     :", file.mode)
    print("Readable :", file.readable())
    print("Writable :", file.writable())
    print("Closed   :", file.closed)

print()


# ============================================
# 16. File Closed?
# ============================================

print("16. Checking Closed")

file = open("sample.txt", "r")

print(file.closed)

file.close()

print(file.closed)

print()


# ============================================
# 17. Creating a File (x Mode)
# ============================================

print("17. Create New File")

try:

    file = open("newfile.txt", "x")

    file.write("New file created successfully.")

    file.close()

    print("File Created.")

except FileExistsError:

    print("File already exists.")

print()


# ============================================
# 18. Handling Missing File
# ============================================

print("18. File Not Found")

try:

    file = open("abc.txt", "r")

except FileNotFoundError:

    print("File does not exist.")

print()


# ============================================
# 19. Copy File Content
# ============================================

print("19. Copy File")

with open("sample.txt", "r") as source:

    data = source.read()

with open("copy.txt", "w") as destination:

    destination.write(data)

print("File copied successfully.")

print()


# ============================================
# 20. Summary
# ============================================

print("========== SUMMARY ==========")

print("open()       -> Open a file")
print("read()       -> Read complete file")
print("readline()   -> Read one line")
print("readlines()  -> Read all lines")
print("write()      -> Write text")
print("writelines() -> Write multiple lines")
print("close()      -> Close file")
print("with         -> Automatically closes file")
print("tell()       -> Current file position")
print("seek()       -> Move file pointer")

print()

print("Program Completed Successfully!")