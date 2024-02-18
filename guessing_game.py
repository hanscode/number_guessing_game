"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random, math

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    # Player attempts start at 0
    attempts = 0

    # Display Welcome message to the player
    print("Welcome to the Number Guessing Game!")
    # Store a random as the answer/solution.
    random_number = random.uniform(0, 11) # Random float:  0.0 <= x <= 11.0
    solution_number = math.ceil(random_number - 1) # Generate a solution number from 0 to 10
    
    while attempts < 6:
        attempts += 1
         # Prompt the player for a guess
        guess_number = input("Guess a number from 0 to 10: ")
        # Convert input value to an integer value
        guess_number = int(guess_number)
        
        if guess_number > solution_number:
            print("It's lower")
        elif guess_number < solution_number:
            print("It's higher")
        else:
            print("You Got it!")
            print("It took you {} attempts to get the correct number.".format(attempts))
            break
    else:
        print("Sorry, You've reached the maximum attempts.")
        print("The correct number is: {}".format(solution_number))
        
    
    # Let the player know the game is ending
    print("The game is ending!")


# Kick off the program by calling the start_game function.
start_game()