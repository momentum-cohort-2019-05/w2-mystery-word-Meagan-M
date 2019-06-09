
word = "bubble"
word_length = len(word)
tries = 8
user_attempts = 1
current_guesses = []
incorrect_letters = []

print("\n\nWelcome to the Mystery Word Game!\n\nYou have 8 tries to guess the letters of the word")
while True:
    game_mode = input("Choose (E)ASY, (R)EGULAR, or (H)ARD mode to begin: ")
    if game_mode.lower() not in ('e', 'r', 'h'):
        print("Please choose again\n'e' for easy mode\n'r' for regular mode\n'h' for hard mode\n\n")
    else:
        break


if game_mode.lower() == "e":
    print("You have chosen easy mode")
if game_mode.lower() == "r":
    print("You have chosen regular mode")
if game_mode.lower() == "h": 
    print("You have chosen hard mode")

# This is from the lists and comprehensions example 49
def print_word(word, guesses):
    ''' 
    this function is from example 49 and is needed along with the code from 48 in order to display the letters and guesses. I tried it without and it didn't work
    '''
    output_letters = [display_letter(letter, guesses)
                      for letter in word]
    print(" ".join(output_letters))

# this is from example 48 on lists and comprehensions. I still don't fully understand why both are needed in order for it to work-- meeting with Andy in the morning and will be sure to ask!

def display_letter(letter, guesses):
    """
    example 48: Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"

[display_letter(letter, current_guesses)
 for letter in word]

print("The word has " + str(word_length) + " letters.")

while user_attempts <= tries:
    letter_guess = input("Guess one letter: ")
    print(letter_guess)
    user_attempts += 1
    if letter_guess in word:
        print(letter_guess + " is in the word! Guess another letter. ")
        current_guesses.append(letter_guess)
        # print(current_guesses)
    else:
        print(letter_guess + " is not in the word, try again. ")
        incorrect_letters.append(letter_guess)
        print(incorrect_letters)
    print_word(word, current_guesses)
