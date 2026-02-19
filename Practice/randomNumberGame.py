#!/usr/bin/env python3

# Random numbers game that asks the user to 
# guess a number between 1 and 5. You have 10 attempts.
# This will show interaraction with the user via the terminal.  
import random
def main():
    number_to_guess = random.randint(1, 5)
    attempts = 5

    print("Welcome to the Random Numbers Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}: Enter your guess: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < 1 or guess > 100:
            print("Your guess is out of bounds. Please guess a number between 1 and 100.")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Run the game. As long as the user presses 'y' or 'Y', 
# the game will restart.
if __name__ == "__main__":
    while True:
        main()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() not in ['y', 'Y']:
            break