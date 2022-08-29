"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730560667"

word_input: str = input("Enter a 5-character word: ")
if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter_input: str = input("Enter a single character: ")
if len(letter_input) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter_input + " in " + word_input)

letter_one: str = word_input[0]
letter_two: str = word_input[1]
letter_three: str = word_input[2]
letter_four: str = word_input[3]
letter_five: str = word_input[4]

matching_instances: int = 0
if letter_one == letter_input:
    print(letter_input + " found at index 0")
    matching_instances = matching_instances + 1
if letter_two == letter_input:
    print(letter_input + " found at index 1")
    matching_instances = matching_instances + 1
if letter_three == letter_input:
    print(letter_input + " found at index 2")
    matching_instances = matching_instances + 1
if letter_four == letter_input:
    print(letter_input + " found at index 3")
    matching_instances = matching_instances + 1   
if letter_five == letter_input:
    print(letter_input + " found at index 4")
    matching_instances = matching_instances + 1

if matching_instances > 1:
    print(str(matching_instances) + " instances of " + letter_input + " found in " + word_input)
if matching_instances == 1:
    print(str(matching_instances) + " instance of " + letter_input + " found in " + word_input)
if matching_instances == 0:
    print("No instances of " + letter_input + " found in " + word_input)