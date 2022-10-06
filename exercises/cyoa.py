"""Choose Your Own Adventure Project!"""
__author__ = "730560667"


points: int
player: str
HAPPY_FACE: str = "\U0001F601"
SAD_FACE: str = "\U0001F641"


def greet() -> None:
    """Welcomes the player and asks for their name."""
    print("Welcome to my guessing game! The point of the game is to predict which number will appear next in a given range. Your score will increase with each correct guess, until you guess incorrectly, upon which you will be brought back to the home screen with the ability to play again or exit the game.")
    global player
    player = input("Please enter your first name to begin: ")


def long_version(points: int) -> int:
    """Function for the hard mode of the game with 4 number choices."""
    print("Predict whether the next number is 1, 2, 3, or 4.")
    from random import randint
    i: int = 1
    while i > 0: 
        result: int = randint(1, 4)
        guess: int = int(input(f"Make your guess, {player}: "))
        if result == guess:
            print(f"Correct {HAPPY_FACE}")
            points += 1
        else:
            print(f"Incorrect {SAD_FACE}")
            return points
    

def main() -> None:
    """The entrypoint of the program."""
    greet()
    global points
    points = 0
    global player
    game_mode: str = ""
    while game_mode != "c":
        game_mode = input(f"{player}, you now have three different options for proceeding in the game. Please type the single, lower-case letter a, b, or c corresponding to your desired path.\na) Easy mode with only two options\nb) Hard mode with four options \nc) Exit the game.\nYour choice: ")
        if game_mode == "a":
            print("Predict whether the next number is 1 or 2.")
            from random import randint
            i: int = 1
            while i > 0: 
                result: int = randint(1, 2)
                guess: int = int(input(f"Make your guess, {player}: "))
                if result == guess:
                    print(f"Correct {HAPPY_FACE}")
                    points += 1
                else:
                    print(f"Incorrect {SAD_FACE}")
                    i = 0
            print(f"Total adventure points obtained: {points}")
        elif game_mode == "b":
            points = long_version(points)
            print(f"Total adventure points obtained: {points}")
        elif game_mode == "c":
            print(f"Thank you for playing, {player}! You have accumulated {points} adventure points this time around. I hope you enjoyed and that you will play again soon!")
            quit()
        else:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()