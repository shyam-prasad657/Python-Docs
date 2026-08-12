# Python Multithreading & Logging — Beginner File

# ============================================
# MULTITHREADING & LOGGING IN PYTHON
# ============================================


# ============================================
# PART 1 - MULTITHREADING
# ============================================

print("========== MULTITHREADING ==========")


# ============================================
# 1. What is a Thread?
# ============================================

print("1. What is a Thread?")

print("A thread is a small unit of work.")
print("It allows multiple tasks to run concurrently.")

print()


# ============================================
# 2. Normal Execution
# ============================================

print("2. Normal Execution")

def task1():
    print("Task 1 started")
    print("Task 1 finished")


def task2():
    print("Task 2 started")
    print("Task 2 finished")


task1()
task2()

print("Both tasks completed.")

print()


# ============================================
# 3. Import threading
# ============================================

print("3. Import threading")

import threading

# ============================================
# 4. Creating a Thread
# ============================================

print("4. Creating a Thread")

def greet():
    print("Hello from a thread!")


thread = threading.Thread(target=greet)

thread.start()

thread.join()

print("Thread completed.")

print()


# ============================================
# 5. Understanding start() and join()
# ============================================

print("5. start() and join()")

def task():
    print("Task is running.")


thread = threading.Thread(target=task)

print("Starting thread...")

thread.start()

print("Waiting for thread to finish...")

thread.join()

print("Thread finished.")

print()


# ============================================
# 6. Running Two Threads
# ============================================

print("6. Two Threads")

def task1():
    for i in range(1, 6):
        print("Task 1:", i)


def task2():
    for i in range(1, 6):
        print("Task 2:", i)


thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads completed.")

print()


# ============================================
# 7. Using sleep()
# ============================================

print("7. Thread with sleep()")

import time


def download():
    for i in range(1, 4):
        print("Downloading...", i)
        time.sleep(1)

    print("Download completed.")


thread = threading.Thread(target=download)

thread.start()
thread.join()

print()


# ============================================
# 8. Two Tasks Running Together
# ============================================

print("8. Two Tasks")

def cooking():
    for i in range(1, 4):
        print("Cooking...", i)
        time.sleep(1)


def cleaning():
    for i in range(1, 4):
        print("Cleaning...", i)
        time.sleep(1)


thread1 = threading.Thread(target=cooking)
thread2 = threading.Thread(target=cleaning)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All tasks completed.")

print()


# ============================================
# 9. Passing Arguments to a Thread
# ============================================

print("9. Passing Arguments")

def greet(name):
    print("Hello", name)


thread = threading.Thread(
    target=greet,
    args=("Shyam",)
)

thread.start()
thread.join()

print()


# ============================================
# 10. Multiple Arguments
# ============================================

print("10. Multiple Arguments")

def add(a, b):
    print("Sum:", a + b)


thread = threading.Thread(
    target=add,
    args=(10, 20)
)

thread.start()
thread.join()

print()


# ============================================
# 11. Checking Thread Name
# ============================================

print("11. Thread Name")

def show_thread():

    current_thread = threading.current_thread()

    print("Thread Name:", current_thread.name)


thread = threading.Thread(
    target=show_thread,
    name="MyThread"
)

thread.start()
thread.join()

print()


# ============================================
# 12. Main Thread
# ============================================

print("12. Main Thread")

print("Current Thread:",
      threading.current_thread().name)

print()


# ============================================
# 13. Checking Whether Thread is Alive
# ============================================

print("13. is_alive()")

def task():
    time.sleep(2)
    print("Task completed.")


thread = threading.Thread(target=task)

print("Before start:", thread.is_alive())

thread.start()

print("After start:", thread.is_alive())

thread.join()

print("After completion:", thread.is_alive())

print()


# ============================================
# 14. Simple Multithreading Example
# ============================================

print("14. Simple Example")

def print_numbers():

    for i in range(1, 6):
        print("Numbers:", i)
        time.sleep(0.5)


def print_letters():

    for letter in ["A", "B", "C", "D", "E"]:
        print("Letters:", letter)
        time.sleep(0.5)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Program completed.")

print()


# ============================================
# PART 2 - LOGGING
# ============================================

print("========== LOGGING ==========")


# ============================================
# 15. What is Logging?
# ============================================

print("15. What is Logging?")

print("Logging is used to record information")
print("about what is happening in a program.")

print()


# ============================================
# 16. Import logging
# ============================================

print("16. Import logging")

import logging

print("logging module imported.")

print()


# ============================================
# 17. Basic Logging
# ============================================

print("17. Basic Logging")

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message.")
logging.info("This is an information message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

print()


# ============================================
# 18. Logging Levels
# ============================================

print("18. Logging Levels")

print("DEBUG     -> Detailed information")
print("INFO      -> General information")
print("WARNING   -> Something may be wrong")
print("ERROR     -> Something went wrong")
print("CRITICAL  -> Serious problem")

print()


# ============================================
# 19. Logging to a File
# ============================================

print("19. Logging to a File")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

print("Logs can be stored in app.log.")

print()


# ============================================
# 20. Logging Messages
# ============================================

print("20. Logging Messages")

logging.info("Application started.")
logging.warning("Low storage.")
logging.error("Unable to open file.")

print("Messages sent to the logger.")

print()


# ============================================
# 21. Logging with Variables
# ============================================

print("21. Logging Variables")

name = "Shyam"
age = 24

logging.info("User name: %s", name)
logging.info("User age: %d", age)

print("Variables logged.")

print()


# ============================================
# 22. Logging an Exception
# ============================================

print("22. Logging an Exception")

try:

    result = 10 / 0

except ZeroDivisionError:

    logging.exception("An error occurred while dividing.")

print("Exception handled.")

print()


# ============================================
# 23. Logging in a Function
# ============================================

print("23. Logging in a Function")

def login(username):

    logging.info("Login attempt by %s", username)

    print("Login function executed.")


login("Shyam")

print()


# ============================================
# 24. Logging + Exception Handling
# ============================================

print("24. Logging + Exception Handling")

def divide(a, b):

    try:

        result = a / b

        logging.info("Division successful.")

        return result

    except ZeroDivisionError:

        logging.error("Cannot divide by zero.")

        return None


print(divide(10, 2))
print(divide(10, 0))

print()


# ============================================
# 25. Simple Real-World Example
# ============================================

print("25. Real-World Example")

def download_file():

    logging.info("Download started.")

    try:

        for i in range(1, 4):

            print("Downloading...", i)
            time.sleep(0.5)

        logging.info("Download completed.")

    except Exception:

        logging.exception("Download failed.")


download_file()

print()


# ============================================
# 26. Multithreading + Logging
# ============================================

print("26. Multithreading + Logging")

def worker(name):

    logging.info("%s started.", name)

    for i in range(3):

        print(name, "-", i)

        time.sleep(0.5)

    logging.info("%s finished.", name)


thread1 = threading.Thread(
    target=worker,
    args=("Worker 1",)
)

thread2 = threading.Thread(
    target=worker,
    args=("Worker 2",)
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All workers completed.")

print()


# ============================================
# 27. Final Summary
# ============================================

print("========== SUMMARY ==========")

print()
print("MULTITHREADING")
print("--------------------------------")
print("threading.Thread() -> Create a thread")
print("start()            -> Start the thread")
print("join()             -> Wait for thread")
print("sleep()            -> Pause execution")
print("is_alive()         -> Check thread status")

print()

print("LOGGING")
print("--------------------------------")
print("logging.debug()    -> Detailed information")
print("logging.info()     -> General information")
print("logging.warning()  -> Warning")
print("logging.error()    -> Error")
print("logging.critical() -> Serious error")
print("logging.exception() -> Log an exception")

print()

print("Program Completed Successfully!")