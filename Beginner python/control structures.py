import random

def number_guessing_game():
    # Prompt user for their name
    name = input("Enter your name: ")
    # Generate a random secret number between 1 and 15
    secret_number = random.randint(1, 15)
    # Initialize the number of attempts to 0
    attempts = 0

    # Start the guessing game loop
    while True:
        # Prompt user for their guess and convert to integer
        guess = int(input("Enter your guess: "))
        # Increment the number of attempts
        attempts += 1
        
        # Compare the guess with the secret number and provide feedback
        if secret_number < guess:
            print("Lower")
        elif secret_number > guess:
            print("Higher")
        else:
            # If the guess is correct, congratulate the user and end the game
            print(f"Congratulations {name}! You guessed the number in {attempts} attempts!")
            break

# Call the function to start the number guessing game
number_guessing_game()
