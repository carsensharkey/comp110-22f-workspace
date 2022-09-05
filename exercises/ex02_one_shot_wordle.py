"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730560667"

secret_word: str = "python"
player_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(player_guess) != len(secret_word):
    player_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    """Ensure that the player's guess word has 6 characters"""

word_index: int = 0
emoji_result: str = ""

while word_index < len(secret_word):
    if player_guess[word_index] == secret_word[word_index]:
        emoji_result = emoji_result + "\U0001F7E9"
        """If the letters in the same position of the guess word and secret word match, add a green square to that position in the emoji sequence"""
    else:
        right_letter_wrong_spot: bool = False
        alternate_index: int = 0
        while right_letter_wrong_spot is False and alternate_index < len(secret_word):
            if player_guess[word_index] == secret_word[alternate_index]:
                """Check to see if the guessed character exists anywhere else in the word"""
                right_letter_wrong_spot = True
            else:
                alternate_index = alternate_index + 1
        if right_letter_wrong_spot is True:
            emoji_result = emoji_result + "\U0001F7E8"
            """Guessed character exists elsewhere, return a yellow square"""
        else:
            emoji_result = emoji_result + "\U00002B1C"
            """Guessed character does not exist in the word at all, return a white square"""
    word_index = word_index + 1
print(emoji_result)
"""Return the sequence of emoji squares to help player narrow down the possibilities for their next guess"""

if player_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
"""Tells the player whether or not they have guessed the word exactly correct"""