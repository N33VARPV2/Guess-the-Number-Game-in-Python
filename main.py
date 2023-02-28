import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of guesses to 0
num_guesses = 0

# Keep asking the user to guess until they get the correct answer
while True:
    # Ask the user to guess the number
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # Increment the number of guesses
    num_guesses += 1
    
    # Provide feedback to the user
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        # Congratulate the user on guessing the correct number and display the number of guesses
        print(f"Congratulations! You guessed the secret number in {num_guesses} tries!")
        break
