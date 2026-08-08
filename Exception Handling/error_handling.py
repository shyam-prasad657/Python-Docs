# ============================================
# ERRORS & EXCEPTIONS IN PYTHON
# ============================================

# ============================================
# 1. What is an Error?
# ============================================

print("1. What is an Error?")

print("An error is a problem in a program")
print("that prevents the program from working correctly.")

print()


# ============================================
# 2. Syntax Error
# ============================================

print("2. Syntax Error")

print("Syntax errors happen when Python")
print("cannot understand the structure of your code.")

# Example of Syntax Error:
#
# if 10 > 5
#     print("Hello")

print("The ':' is missing in the example above.")

print()


# ============================================
# 3. Runtime Error
# ============================================

print("3. Runtime Error")

print("A runtime error occurs while the program")
print("is actually running.")

# Example:
#
# number = 10
# print(number / 0)

print("The example above causes ZeroDivisionError.")

print()


# ============================================
# 4. Logical Error
# ============================================

print("4. Logical Error")

print("A logical error does not usually stop the program.")
print("Instead, the program produces the wrong result.")

number1 = 10
number2 = 5

# Wrong calculation:
result = number1 - number2

print("Expected Addition:", number1 + number2)
print("Actual Result:", result)

print()


# ============================================
# 5. What is an Exception?
# ============================================

print("5. What is an Exception?")

print("An exception is an error that occurs")
print("while the program is running.")

print("Python provides exception handling")
print("to prevent the program from crashing.")

print()


# ============================================
# 6. ZeroDivisionError
# ============================================

print("6. ZeroDivisionError")

try:

    result = 10 / 0
    print(result)

except ZeroDivisionError:

    print("You cannot divide a number by zero.")

print()


# ============================================
# 7. ValueError
# ============================================

print("7. ValueError")

try:

    number = int("Hello")
    print(number)

except ValueError:

    print("Invalid value for integer conversion.")

print()


# ============================================
# 8. TypeError
# ============================================

print("8. TypeError")

try:

    result = "10" + 5
    print(result)

except TypeError:

    print("Cannot add a string and an integer.")

print()


# ============================================
# 9. NameError
# ============================================

print("9. NameError")

try:

    print(my_variable)

except NameError:

    print("The variable does not exist.")

print()


# ============================================
# 10. IndexError
# ============================================

print("10. IndexError")

numbers = [10, 20, 30]

try:

    print(numbers[5])

except IndexError:

    print("Index does not exist in the list.")

print()


# ============================================
# 11. KeyError
# ============================================

print("11. KeyError")

student = {
    "name": "Shyam",
    "age": 25
}

try:

    print(student["city"])

except KeyError:

    print("The requested key does not exist.")

print()


# ============================================
# 12. FileNotFoundError
# ============================================

print("12. FileNotFoundError")

try:

    file = open("unknown_file.txt", "r")

except FileNotFoundError:

    print("The file does not exist.")

print()


# ============================================
# 13. Basic try...except
# ============================================

print("13. Basic try...except")

try:

    number = int("100")

    print("Number:", number)

except:

    print("Something went wrong.")

print()


# ============================================
# 14. Multiple except Blocks
# ============================================

print("14. Multiple except Blocks")

try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:

    print("Please enter a valid number.")

except ZeroDivisionError:

    print("Number cannot be zero.")

print()


# ============================================
# 15. Exception with User Input
# ============================================

print("15. Exception with User Input")

try:

    age = int(input("Enter your age: "))

    print("Your age is:", age)

except ValueError:

    print("Please enter numbers only.")

print()


# ============================================
# 16. else with try...except
# ============================================

print("16. else with try...except")

try:

    number = int("50")

except ValueError:

    print("Conversion failed.")

else:

    print("Conversion successful.")
    print("Number:", number)

print()


# ============================================
# 17. finally
# ============================================

print("17. finally")

try:

    number = 10 / 2

    print("Result:", number)

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("This block always executes.")

print()


# ============================================
# 18. try + except + else + finally
# ============================================

print("18. Complete Exception Handling")

try:

    number = int("20")

    result = 100 / number

except ValueError:

    print("Invalid number.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Operation successful.")
    print("Result:", result)

finally:

    print("Program execution completed.")

print()


# ============================================
# 19. Catching the Exception Object
# ============================================

print("19. Exception Object")

try:

    number = 10 / 0

except Exception as error:

    print("Error Type:", type(error).__name__)
    print("Error Message:", error)

print()


# ============================================
# 20. Exception Hierarchy
# ============================================

print("20. Exception Hierarchy")

print("BaseException")
print("    Exception")
print("        ValueError")
print("        TypeError")
print("        KeyError")
print("        IndexError")
print("        ZeroDivisionError")
print("        FileNotFoundError")

print()


# ============================================
# 21. Raising an Exception
# ============================================

print("21. raise")

try:

    age = 15

    if age < 18:
        raise ValueError("Age must be 18 or above.")

except ValueError as error:

    print("Error:", error)

print()


# ============================================
# 22. Custom Exception
# ============================================

print("22. Custom Exception")


class AgeError(Exception):
    pass


try:

    age = 15

    if age < 18:
        raise AgeError("You must be 18 or older.")

except AgeError as error:

    print("Custom Error:", error)

print()


# ============================================
# 23. Using Exception Handling in a Function
# ============================================

print("23. Exception Handling in Function")


def divide(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        return "Cannot divide by zero."


print(divide(10, 2))
print(divide(10, 0))

print()