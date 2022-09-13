"""EX03 - Structured Wordle!"""
__author__ = "730560667"


def contains_char(string_input: str, character_input: str) -> bool:
    """Test to see if a single character input is found at any index of a string input."""
    assert len(character_input) == 1
    # Assert that the second argument has a length of 1
    i = 0
    while i < len(string_input):
        if string_input[i] == character_input:
            return True
            # This will correspond to a yellow block later on in the program
        i = i + 1
    return False
    # This will correspond to a white block later on in the program


def emojified(guess: str, secret: str) -> str:
    """Create a string of emojis whose colors signify how similar the guess is to the secret word."""
    assert len(guess) == len(secret)
    # Assert that the guess and secret words are equal in length
    i = 0
    emoji_sequence: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_sequence = emoji_sequence + "\U0001F7E9"
            # Print a green square
        elif contains_char(secret, guess[i]) is True:
            emoji_sequence = emoji_sequence + "\U0001F7E8"
            # Print a yellow square
        else:
            emoji_sequence = emoji_sequence + "\U00002B1C"
            # Print a white square
        i = i + 1
    return emoji_sequence


def input_guess(expected_length: int) -> str:
    """Continue to ask users to enter a word of specified length until a word of correct length is enterred."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """Establish what the secret word is, keep track of how many turns the user has spent, whether the user has won the game, and control the flow of the game."""
    secret = "codes"
    guess = ""
    expected_length = len(secret)
    i = 1
    while i <= 6 and secret != guess:
        # User can play while they have guesses left AND they have not yet won
        print(f"=== Turn {i}/6 ===")
        guess = input_guess(expected_length)
        print(emojified(guess, secret))
        i = i + 1
    if secret == guess:
        print(f"You won in {i-1}/6 turns!")
        # The guess word is the same as the secret word - Yay! Win!
    else:
        print("X/6 - Sorry, try again tomorrow!")
        # The guess word is not the same as the secret word - Boo! Lose!


if __name__ == "__main__":
    # Allows you to run the game as a module
    main()