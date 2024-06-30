import time
from contextlib import contextmanager
import os

class DatabaseConnection:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        print(f"Connecting to database on {self.host}...")
        time.sleep(5)  # Simulating connection time

    def disconnect(self):
        print("Disconnecting from database...")
        time.sleep(5)

    def __enter__(self):
        self.connect()
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        end_time = time.time()
        print(f"Elapsed time: {end_time - self.start_time:.2f} seconds")

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds")

# Nested context manager combining DatabaseConnection and timer
@contextmanager
def timed_database_connection(host, user, password):
    with DatabaseConnection(host, user, password) as db, timer():
        yield db

@contextmanager
def temp_file(filename):
    try:
        f = open(filename, 'w')
        yield f
    finally:
        f.close()
        os.remove(filename)

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"Elapsed time: {self.duration:.2f} seconds")


host = input("Enter the host:")
user = input("Enter the user:")
password = input("Enter the password:")

with DatabaseConnection(host, user, password) as db:
    time.sleep(2)

# Explanation:
# 1. DatabaseConnection class:
#    - Implements __enter__ and __exit__ methods to make it a context manager.
#    - __enter__ connects to the database and starts timing.
#    - __exit__ disconnects and prints the elapsed time.

# 2. timer function:
#    - A context manager created using @contextmanager decorator.
#    - Measures and prints the execution time of the code inside the with block.

# 3. timed_database_connection function:
#    - A nested context manager that combines DatabaseConnection and timer.
#    - Allows timing of database operations.

# 4. temp_file function:
#    - A context manager for handling temporary file operations.
#    - Opens a file, yields it, then ensures it's closed and removed after use.

# 5. Timer class:
#    - Another implementation of a timer using a class-based context manager.
#    - __enter__ starts the timer, __exit__ calculates and prints the duration.

# 6. Example usage:
#    - Demonstrates how to use the DatabaseConnection context manager.
#    - Prompts the user for host, user, and password.
#    - Uses the DatabaseConnection within a with statement.
#    - Simulates some operation with a 2-second sleep.

# This code provides various ways to manage resources and time operations using context managers,
# showcasing both function-based and class-based implementations. It focuses on database connections
# and timing operations, with additional utilities for temporary file handling.


#-------------------------


# from contextlib import contextmanager
# import os

# @contextmanager
# def temp_file(filename):
#     try:
#         f = open(filename, 'w')
#         yield f
#     finally:
#         f.close()
#         os.remove(filename)

# with temp_file('test.txt') as f:
#     f.write('hello')

# Explanation:
# This code demonstrates the use of a context manager to handle temporary file operations.
# 1. We import 'contextmanager' from 'contextlib' to create a context manager using a generator function.
# 2. We also import 'os' to use file system operations.
# 3. The 'temp_file' function is defined as a context manager using the '@contextmanager' decorator:
#    - It opens a file in write mode and yields the file object.
#    - The 'finally' block ensures that the file is closed and removed, even if an exception occurs.
# 4. We use the 'with' statement to create a temporary file named 'test.txt':
#    - The file is automatically opened when entering the 'with' block.
#    - We write 'hello' to the file.
#    - When exiting the 'with' block, the file is automatically closed and removed.
# This context manager allows for safe and clean handling of temporary files, ensuring they are
# properly cleaned up after use, regardless of whether operations complete successfully or not.

#-------------------------

# import time

# class Timer:
#     def __enter__(self):
#         self.start = time.time()
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.end = time.time()
#         self.duration = self.end - self.start
#         print(f"Elapsed time: {self.duration:.2f} seconds")

# with Timer():
#     time.sleep(2)

# Explanation:
# This code demonstrates the use of a context manager in Python.
# 1. We import the 'time' module to measure elapsed time.
# 2. The 'Timer' class is defined as a context manager:
#    - The '__enter__' method is called when entering the 'with' block. It records the start time and returns the instance.
#    - The '__exit__' method is called when exiting the 'with' block. It calculates and prints the elapsed time.
# 3. We use the 'with' statement to create a Timer context:
#    - The code inside the 'with' block (time.sleep(2)) is timed.
#    - When the block ends, the elapsed time is automatically calculated and printed.
# This context manager allows for easy and clean measurement of code execution time.
