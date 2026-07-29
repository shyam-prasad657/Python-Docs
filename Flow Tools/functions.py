# ============================================
# FUNCTIONS IN PYTHON
# ============================================

# ============================================
# 1. Defining a Simple Function
# ============================================

print("1. Simple Function")

def greet():
    print("Hello, Welcome to Python!")

greet()

print()


# ============================================
# 2. Calling a Function Multiple Times
# ============================================

print("2. Calling Function Multiple Times")

def welcome():
    print("Welcome!")

welcome()
welcome()
welcome()

print()


# ============================================
# 3. Function with One Parameter
# ============================================

print("3. Function with One Parameter")

def greet_user(name):
    print("Hello,", name)

greet_user("Shyam")
greet_user("Rahul")

print()


# ============================================
# 4. Function with Multiple Parameters
# ============================================

print("4. Function with Multiple Parameters")

def student(name, age):
    print("Name:", name)
    print("Age :", age)

student("Shyam", 24)

print()


# ============================================
# 5. Function Returning a Value
# ============================================

print("5. Return Statement")

def add(a, b):
    return a + b

result = add(10, 20)

print("Sum =", result)

print()


# ============================================
# 6. Returning Multiple Values
# ============================================

print("6. Returning Multiple Values")

def calculations(a, b):

    return a+b, a-b, a*b

sum1, difference, product = calculations(10, 5)

print("Addition      :", sum1)
print("Subtraction   :", difference)
print("Multiplication:", product)

print()


# ============================================
# 7. Function Without Return
# ============================================

print("7. Function Without Return")

def message():
    print("This function does not return anything.")

value = message()

print("Returned Value:", value)

print()


# ============================================
# 8. Default Arguments
# ============================================

print("8. Default Arguments")

def country(name, nation="India"):
    print(name, "belongs to", nation)

country("Shyam")
country("John", "USA")

print()


# ============================================
# 9. Keyword Arguments
# ============================================

print("9. Keyword Arguments")

def employee(name, salary):
    print("Name  :", name)
    print("Salary:", salary)

employee(salary=50000, name="Rahul")

print()


# ============================================
# 10. Positional Arguments
# ============================================

print("10. Positional Arguments")

employee("Ankit", 45000)

print()


# ============================================
# 11. Arbitrary Arguments (*args)
# ============================================

print("11. *args")

def total(*numbers):

    print("Numbers:", numbers)

    print("Sum =", sum(numbers))

total(10, 20, 30)
total(5, 10, 15, 20)

print()


# ============================================
# 12. Arbitrary Keyword Arguments (**kwargs)
# ============================================

print("12. **kwargs")

def details(**info):

    print(info)

details(name="Shyam", age=24, city="Chennai")

print()


# ============================================
# 13. Local Variable
# ============================================

print("13. Local Variable")

def demo():

    number = 100

    print("Inside Function:", number)

demo()

print()


# ============================================
# 14. Global Variable
# ============================================

print("14. Global Variable")

language = "Python"

def show():

    print("Language:", language)

show()

print()


# ============================================
# 15. Using global Keyword
# ============================================

print("15. global Keyword")

count = 10

def increase():

    global count

    count += 5

increase()

print(count)

print()


# ============================================
# 16. Recursive Function
# ============================================

print("16. Recursion")

def countdown(n):

    if n == 0:
        print("Finished!")
        return

    print(n)

    countdown(n-1)

countdown(5)

print()


# ============================================
# 17. Lambda Function
# ============================================

print("17. Lambda Function")

square = lambda x: x*x

print(square(6))

print()


# ============================================
# 18. Function Inside Function
# ============================================

print("18. Nested Function")

def outer():

    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()

print()


# ============================================
# 19. Docstring
# ============================================

print("19. Docstring")

def multiply(a, b):
    """
    Returns multiplication of two numbers.
    """
    return a * b

print(multiply(5, 4))

print(multiply.__doc__)

print()

# ============================================
# 24. Function Scope Example
# ============================================

print("24. Scope Example")

x = 50

def example():

    x = 100

    print("Inside:", x)

example()

print("Outside:", x)

print()