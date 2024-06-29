def number_values():
    # Prompt user for two numbers and convert them to integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform arithmetic operations and print the results
    print(f"Addition: {num1 + num2}")  # Addition of the two numbers
    print(f"Subtraction: {num1 - num2}")  # Subtraction of the two numbers
    print(f"Multiplication: {num1 * num2}")  # Multiplication of the two numbers
    print(f"Division: {num1 / num2}")  # Division of the two numbers
    print(f"Modulus: {num1 % num2}")  # Modulus (remainder) of the two numbers
    print(f"Exponentiation: {num1 ** num2}")  # Exponentiation of the two numbers
    print(f"Floor Division: {num1 // num2}")  # Floor division of the two numbers

number_values()
