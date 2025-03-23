# Created by: Serge Hamouche
# Created on: march 3rd, 2025
# This program asks the user for a random number from 0-100
import random


def main():
    # Ask user to guess number from 0-100

    SECRET_NUMBER = random.randint(
        0, 100
    )  # Generate a random integer between 0 and 100

    # Get the user's guess
    user_guess = int(input("Enter a number between 0 and 100: "))

    # Check if the guess is correct
    if user_guess == SECRET_NUMBER:
        print("correct!")
    else:
        print("wrong!")


if __name__ == "__main__":
    main()
