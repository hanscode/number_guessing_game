"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can
totally do that by clicking:
File -> Download Workspace in the file menu after you fork the snapshot
of this workspace.

"""

import random
import math


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player
         "It's lower".
      b. If the guess is less than the solution, display to the player
         "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates
       the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    # Player attempts start at 0
    attempts = 0
    # Store the player scores
    scores = []

    # Display Welcome message to the player
    print("Welcome to the Number Guessing Game!")
    # Store a random as the answer/solution.
    random_number = random.uniform(0, 11)  # Random float:  0.0 <= x <= 11.0
    # Generate a solution number from 0 to 10
    solution_number = math.ceil(random_number - 1)

    while attempts < 6:
        try:
            # Prompt the player for a guess
            guess_number = input("Guess a number from 0 to 10: ")
            # Convert input value to an integer value
            guess_number = int(guess_number)
            if guess_number < 0 or guess_number > 10:
                raise ValueError("The guess must be a number between 0 and 10")
        except ValueError as err:
            # Include the error text to the output
            print(
                ("Oh no, we ran into an issue. {}. "
                 "please try again."
                 .format(err))
            )
            continue

        attempts += 1
        if guess_number > solution_number:
            print("It's lower")
        elif guess_number < solution_number:
            print("It's higher")
        else:
            print("You Got it!")
            print("It took you {} attempts to get the correct number."
                  .format(attempts))
            play_again = input("Would you like to play again? (yes/no): ")
            if play_again.lower() == "yes":
                scores.append(attempts)
                # Using the built-in min function to get the high score
                high_score = min(scores)
                # As a player, at the start of each game, I should be shown the
                # current high score (least amount of guess attempts) so that I
                # know what I am supposed to beat.
                print("The current high score is: {}".format(high_score))
                # Reset the attempts and solution number
                attempts = 0
                solution_number = math.ceil(random.uniform(0, 11) - 1)
                continue
            break
    else:
        print("Sorry, You've reached the maximum attempts.")
        print("The correct number is: {}".format(solution_number))

    # Let the player know the game is ending

    print("The game is ending!")
    print("Thank you for playing the Number Guessing Game!")
    # reset the scores list
    scores = []

# Kick off the program by calling the start_game function.


start_game()
