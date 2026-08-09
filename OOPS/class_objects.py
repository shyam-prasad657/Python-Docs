# ============================================
# CLASSES & OBJECTS IN PYTHON
# ============================================


# ============================================
# 1. What is a Class?
# ============================================

print("1. Creating a Class")

class Student:
    pass

print("Student class created.")

print()


# ============================================
# 2. Creating an Object
# ============================================

print("2. Creating an Object")

class Student:
    pass

student1 = Student()

print("Object created:")
print(student1)

print()


# ============================================
# 3. Adding Attributes to an Object
# ============================================

print("3. Object Attributes")

student1.name = "Shyam"
student1.age = 24
student1.course = "Python"

print("Name  :", student1.name)
print("Age   :", student1.age)
print("Course:", student1.course)

print()


# ============================================
# 4. Creating Multiple Objects
# ============================================

print("4. Multiple Objects")

student1 = Student()
student2 = Student()

student1.name = "Shyam"
student2.name = "Rahul"

student1.age = 24
student2.age = 25

print("Student 1:", student1.name, student1.age)
print("Student 2:", student2.name, student2.age)

print()


# ============================================
# 5. Constructor (__init__)
# ============================================

print("5. Constructor")

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Shyam", 24)

print("Name:", student1.name)
print("Age :", student1.age)

print()


# ============================================
# 6. Understanding self
# ============================================

print("6. self")

class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Student Name:", self.name)

student1 = Student("Shyam")

student1.show_name()

print()


# ============================================
# 7. Creating Methods
# ============================================

print("7. Methods")

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old.")

student1 = Student("Shyam", 24)

student1.introduce()

print()


# ============================================
# 8. Method with Parameters
# ============================================

print("8. Method with Parameters")

class Calculator:

    def add(self, a, b):
        print("Addition:", a + b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

calculator = Calculator()

calculator.add(10, 20)
calculator.multiply(5, 4)

print()


# ============================================
# 9. Method Returning a Value
# ============================================

print("9. Method with return")

class Calculator:

    def add(self, a, b):
        return a + b

calculator = Calculator()

result = calculator.add(10, 30)

print("Result:", result)

print()


# ============================================
# 10. Multiple Objects with Different Data
# ============================================

print("10. Multiple Objects")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name  :", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Shyam", 50000)
employee2 = Employee("Rahul", 60000)

employee1.show_details()

print()

employee2.show_details()

print()


# ============================================
# 11. Modifying Object Attributes
# ============================================

print("11. Modifying Attributes")

employee1 = Employee("Shyam", 50000)

print("Before:")
print(employee1.salary)

employee1.salary = 55000

print("After:")
print(employee1.salary)

print()


# ============================================
# 12. Adding New Attributes
# ============================================

print("12. Adding New Attributes")

employee1.department = "IT"

print("Department:", employee1.department)

print()


# ============================================
# 13. Deleting an Attribute
# ============================================

print("13. Deleting Attribute")

del employee1.department

print("Department attribute deleted.")

print()


# ============================================
# 14. Class Variable
# ============================================

print("14. Class Variable")

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

student1 = Student("Shyam")
student2 = Student("Rahul")

print(student1.name, "-", student1.school)
print(student2.name, "-", student2.school)

print()


# ============================================
# 15. Instance Variable vs Class Variable
# ============================================

print("15. Instance vs Class Variable")

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

student1 = Student("Shyam")
student2 = Student("Rahul")

student1.school = "XYZ School"

print("Student 1:", student1.name, "-", student1.school)
print("Student 2:", student2.name, "-", student2.school)

print()


# ============================================
# 16. Class Method
# ============================================

print("16. Class Method")

class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

print("Before:", Student.school)

Student.change_school("XYZ School")

print("After :", Student.school)

print()


# ============================================
# 17. Static Method
# ============================================

print("17. Static Method")

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

print()


# ============================================
# 18. __str__ Method
# ============================================

print("18. __str__ Method")

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

student1 = Student("Shyam", 24)

print(student1)

print()


# ============================================
# 19. Checking Object Type
# ============================================

print("19. type()")

student1 = Student("Shyam", 24)

print(type(student1))

print()


# ============================================
# 20. isinstance()
# ============================================

print("20. isinstance()")

print(isinstance(student1, Student))

print()


# ============================================
# 21. Inheritance
# ============================================

print("21. Inheritance")

class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.bark()

print()


# ============================================
# 22. Method Overriding
# ============================================

print("22. Method Overriding")

class Animal:

    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def sound(self):
        print("Dog barks.")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()

print()


# ============================================
# 23. Using super()
# ============================================

print("23. super()")

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course


student = Student("Shyam", "Python")

print("Name  :", student.name)
print("Course:", student.course)

print()


# ============================================
# 24. Encapsulation Basics
# ============================================

print("24. Encapsulation")

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(10000)

account.show_balance()

print()


# ============================================
# 27. Important OOP Terms
# ============================================

print("========== IMPORTANT TERMS ==========")

print("Class        -> Blueprint for creating objects")
print("Object       -> Instance of a class")
print("Attribute    -> Data stored inside an object")
print("Method       -> Function defined inside a class")
print("self         -> Refers to the current object")
print("__init__     -> Constructor")
print("Class Var    -> Shared class-level variable")
print("Inheritance  -> Child class gets features from parent")
print("super()      -> Access parent class functionality")
print("Encapsulation -> Bundling/protecting data and methods")
print("Polymorphism -> Same method/interface, different behavior")

print()


# ============================================
# 28. Final Summary
# ============================================

print("========== SUMMARY ==========")

print("1. Create a class using class")
print("2. Create objects from the class")
print("3. Use __init__ to initialize objects")
print("4. Use self to access object data")
print("5. Create methods to perform actions")
print("6. Use class variables for shared data")
print("7. Use inheritance to reuse code")
print("8. Use super() to access parent functionality")

print()

print("Classes & Objects Completed Successfully!")