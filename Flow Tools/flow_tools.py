# ============================================
# IF, ELIF, ELSE, BREAK, CONTINUE & PASS
# ============================================

# ============================================
# 1. Simple if Statement
# ============================================

print("1. Simple if Statement")

age = 20

if age >= 18:
    print("You are eligible to vote.")

print("Program continues...\n")


# ============================================
# 2. if...else Statement
# ============================================

print("2. if...else Statement")

marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")

print()


# ============================================
# 3. if...elif...else Statement
# ============================================

print("3. if...elif...else Statement")

score = 82

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Grade D")

print()


# ============================================
# 4. Multiple Conditions using and
# ============================================

print("4. Using 'and'")

age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")

print()


# ============================================
# 5. Multiple Conditions using or
# ============================================

print("5. Using 'or'")

is_student = False
has_coupon = True

if is_student or has_coupon:
    print("Discount Applied")
else:
    print("No Discount")

print()


# ============================================
# 6. Using not
# ============================================

print("6. Using 'not'")

is_logged_in = False

if not is_logged_in:
    print("Please Login")
else:
    print("Welcome!")

print()


# ============================================
# 7. Nested if
# ============================================

print("7. Nested if")

age = 21
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Too Young")

print()


# ============================================
# 8. break Statement
# Stops the loop immediately.
# ============================================

print("8. break Statement")

for i in range(1, 11):

    if i == 6:
        print("Break encountered!")
        break

    print(i)

print("Loop Finished\n")


# ============================================
# 9. continue Statement
# Skips the current iteration.
# ============================================

print("9. continue Statement")

for i in range(1, 11):

    if i == 6:
        continue

    print(i)

print("Loop Finished\n")


# ============================================
# 10. pass Statement
# Does nothing.
# ============================================

print("10. pass Statement")

for i in range(1, 6):

    if i == 3:
        pass

    print(i)

print("pass didn't skip anything.\n")


# ============================================
# 11. pass in if Statement
# ============================================

print("11. pass inside if")

number = 10

if number > 5:
    pass

print("Program continues normally.\n")


# ============================================
# 12. break in while Loop
# ============================================

print("12. break with while")

count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1

print("While Loop Ended\n")


# ============================================
# 13. continue in while Loop
# ============================================

print("13. continue with while")

count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)

print()


# ============================================
# 14. if with User Comparison
# ============================================

print("14. Comparison Operators")

num = 15

if num > 20:
    print("Greater than 20")
elif num == 20:
    print("Equal to 20")
else:
    print("Less than 20")

print()


# ============================================
# 15. Checking Even or Odd
# ============================================

print("15. Even or Odd")

number = 18

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

print()


# ============================================
# 16. Finding Largest Number
# ============================================

print("16. Largest Number")

a = 15
b = 45
c = 30

if a > b and a > c:
    print("Largest:", a)

elif b > a and b > c:
    print("Largest:", b)

else:
    print("Largest:", c)

print()


# ============================================
# 17. break Example (Search)
# ============================================

print("17. Search using break")

numbers = [5, 10, 15, 20, 25]

for num in numbers:

    if num == 15:
        print("Found:", num)
        break

print()


# ============================================
# 18. continue Example (Skip Even Numbers)
# ============================================

print("18. Skip Even Numbers")

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)

print()