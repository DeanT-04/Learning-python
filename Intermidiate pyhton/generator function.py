# Function to generate prime numbers indefinitely
def prime_numbers():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Class that creates an iterator for even numbers up to a specified limit
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 2
        return self.current - 2

# Generator expression for the squares of numbers from 1 to 10
squares = (x**2 for x in range(1, 11))

# Function that takes multiple iterables and yields items from them in a round-robin fashion
def merge_iterables(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        for it in iterators.copy():
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)

# Example usage:
# Print the first 10 prime numbers
primes = prime_numbers()
print("First 10 prime numbers:")
for _ in range(10):
    print(next(primes), end=' ')
print()

# Print even numbers up to 20
print("\nEven numbers up to 20:")
evens = EvenNumbers(20)
for num in evens:
    print(num, end=' ')
print()

# Print the squares
print("\nSquares of numbers from 1 to 10:")
print(list(squares))

# Merge and print items from multiple iterables
print("\nMerged items from multiple iterables:")
numbers = [1, 2, 3, 4]
letters = ['A', 'B', 'C', 'D', 'E']
symbols = ['!', '@', '#']
for item in merge_iterables(numbers, letters, symbols):
    print(item, end=' ')
print()

# Explanation:
# This code demonstrates various concepts related to generators and iterators in Python.

# 1. The 'prime_numbers()' function is a generator that yields prime numbers indefinitely.
#    It uses the 'is_prime()' helper function to check for primality.

# 2. The 'EvenNumbers' class is an iterator that generates even numbers up to a specified limit.
#    It implements the '__iter__()' and '__next__()' methods to make it iterable.
#    The '__iter__()' method returns the object itself, allowing it to be used in for loops.
#    The '__next__()' method is called in each iteration, updating self.current and returning
#    the next even number. It raises StopIteration when self.current exceeds self.limit.
#    self.current starts at 0 and is incremented by 2 in each iteration to generate even numbers.
#    self.limit is set during initialization and determines when to stop generating numbers.

# 3. The 'squares' generator expression creates squares of numbers from 1 to 10 concisely.

# 4. The 'merge_iterables()' function is a generator that takes multiple iterables and yields
#    items from them in a round-robin fashion until all iterables are exhausted.

# Key variables explained:
# 'num': In prime_numbers(), it represents the current number being checked for primality.
# 'self.current': In EvenNumbers, it keeps track of the current even number in the sequence.
# 'self.limit': In EvenNumbers, it sets the upper bound for the even numbers to be generated.
# 'iterators': In merge_iterables(), it's a list of iterator objects created from input iterables.
