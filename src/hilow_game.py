"""Play a higher/lower guessing game with user-defined bounds.

Inputs:
- lower_bound (int) from user input
- upper_bound (int) from user input
- user_guess (int) from user input

Processing:
- Validate bounds so lower < upper
- Generate a random number in the range
- Compare guesses until the random number is guessed

Outputs:
- Prompts, hints (too low/high), and success message printed to the console.

Typical usage example:
    Enter the lower bound: 1
    Enter the upper bound: 10
    Great, now guess a number between 1 and 10: 5
    Nope, too low.
    Guess another number: 7
    You got it!
"""

# === Imports ===
from random import randint


# === Main Function ===
def main() -> None:
    """Run the higher/lower guessing game."""

    # Display welcome message to Bella.
    # TODO: Add code to display a welcome message to Bella, the user.

    # Get and validate lower and upper bounds of the guessing range.
    # TODO: Add code to get and validate lower and upper bounds from user input
    # using a post-condition loop.

    # Generate a random number between lower and upper bounds, inclusive.
    # TODO: Add code to generate a random number between lower_bound and
    # upper_bound, inclusive.

    # Prompt player for first guess.
    # TODO: Add code to prompt the player for their first guess.


    # Repeat guessing until the user guesses correctly.
    # TODO: Add code for a loop that repeats until the user guesses correctly.

    # Display correct guess message.
    # TODO: Add code to display a message indicating the user guessed correctly.


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Add references to any resources used to complete this assignment.
