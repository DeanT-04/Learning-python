# Import the time module for measuring execution time
import time

# Define a closure that creates a logger function
def create_logger(prefix):
    # Inner function that forms the closure
    def logger(message):
        # Print the message with the specified prefix
        print(f"{prefix} {message}")
    # Return the inner function, creating a closure
    return logger

# Define a decorator for timing function execution
def timing_decorator(func):
    # Wrapper function that adds timing functionality
    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()
        # Execute the original function
        result = func(*args, **kwargs)
        # Record the end time
        end_time = time.time()
        # Calculate and print the execution time
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        # Return the result of the original function
        return result
    # Return the wrapper function
    return wrapper

# Create two logger functions using the create_logger closure
debug_logger = create_logger("[DEBUG]")
error_logger = create_logger("[ERROR]")

# Define a function that simulates data fetching and decorate it with the timing decorator
@timing_decorator
def fetch_data(id):
    # Simulate a delay in fetching data
    time.sleep(2)
    # Return a string representing the fetched data
    return f"Data for ID {id}"

# Demonstrate the use of loggers and the decorated fetch_data function
debug_logger("Starting data fetch")
result = fetch_data(42)
debug_logger("Data fetch completed")
# Check if data fetching was successful and log accordingly
if result is None:
    error_logger("Failed to fetch data")
else:
    debug_logger(f"Fetched data: {result}")
