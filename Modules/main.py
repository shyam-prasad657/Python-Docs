# ============================================
# MODULES IN PYTHON
# ============================================

# ============================================
# 1. Importing a Module
# ============================================

print("1. Import Module")

import math

print(math.sqrt(25))
print(math.pi)

print()


# ============================================
# 2. Import Specific Functions
# ============================================

print("2. Import Specific Function")

from math import sqrt, factorial

print(sqrt(64))
print(factorial(5))

print()


# ============================================
# 3. Import with Alias
# ============================================

print("3. Alias")

import math as m

print(m.pow(2, 5))
print(m.floor(5.9))
print(m.ceil(5.1))

print()


# ============================================
# 4. Import Everything (Not Recommended)
# ============================================

print("4. Import *")

from math import *

print(sin(0))
print(cos(0))

print()


# ============================================
# 5. Random Module
# ============================================

print("5. Random Module")

import random

print(random.randint(1, 10))
print(random.choice(["Apple", "Banana", "Orange"]))

print()


# ============================================
# 6. Datetime Module
# ============================================

print("6. Datetime Module")

import datetime

today = datetime.datetime.now()

print(today)

print()


# ============================================
# 7. OS Module
# ============================================

print("7. OS Module")

import os

print("Current Folder:")
print(os.getcwd())

print()


# ============================================
# 8. Platform Module
# ============================================

print("8. Platform Module")

import platform

print(platform.system())
print(platform.python_version())

print()


# ============================================
# 9. Using a Custom Module
# ============================================

print("9. Custom Module")

import mymodule

mymodule.greet()

print(mymodule.name)

print(mymodule.add(10, 20))

print(mymodule.multiply(5, 4))

print()


# ============================================
# 10. Import Specific Function from Custom Module
# ============================================

print("10. Import Specific Function")

from mymodule import greet, add

greet()

print(add(50, 60))

print()


# ============================================
# 11. Alias for Custom Module
# ============================================

print("11. Alias for Custom Module")

import mymodule as mm

mm.greet()

print(mm.add(5, 15))

print()


# ============================================
# 12. dir() Function
# Lists all functions and variables
# ============================================

print("12. dir()")

print(dir(math))

print()


# ============================================
# 13. __name__ Variable
# ============================================

print("13. __name__")

print(__name__)

print()


# ============================================
# 14. Calling Functions Multiple Times
# ============================================

print("14. Reusing Functions")

print(mymodule.add(100, 200))

print(mymodule.multiply(8, 9))

print()


# ============================================
# 15. Using Constants from Modules
# ============================================

print("15. Constants")

print(math.pi)

print(math.e)

print()


# ============================================
# 16. More Useful Math Functions
# ============================================

print("16. Math Functions")

print(math.sqrt(81))

print(math.factorial(6))

print(math.gcd(18, 24))

print(math.fabs(-25))

print()


# ============================================
# 17. Random Choices
# ============================================

print("17. Random Examples")

colors = ["Red", "Green", "Blue", "Black"]

print(random.choice(colors))

print(random.sample(colors, 2))

print()


# ============================================
# 18. Datetime Formatting
# ============================================

print("18. Date Formatting")

print(today.strftime("%d-%m-%Y"))

print(today.strftime("%I:%M %p"))

print()


# # ============================================
# # 19. Help Function
# # ============================================

# print("19. help()")

# print(help(math.sqrt))

# print()


# ============================================
# 20. Summary
# ============================================

print("========== SUMMARY ==========")

print("import module")
print("from module import function")
print("import module as alias")
print("dir(module)")
print("__name__")
print("Creating Your Own Modules")

print()

print("Program Completed Successfully!")