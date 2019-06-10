# CURRENTLY WORKING ON THIS: while loop to countdown wrong letter guess attempts

'''turns = 0
while turns <= 7:
    print('That letter is not in the word, try again.\n\nYou have ' + str(turns) + ' guesses left')
    turns = turns + 1 
print("That letter is in the word, choose another!")'''

# ALSO WORKING ON THIS: for loop to display letters and _ in correct sequence after each guess TO REPLACE THE LIST COMPREHENSION (to improve my understanding of how it works)



# BUT TURNING IN THE ASSIGNMENT SO YOU CAN SEE IT :) 

word = "beautiful"
word_length = len(word)
tries = 8
user_attempts = 1
current_guesses = []
incorrect_letters = []

# try using a multi-line string to adjust the spacing. multi line strings preserve the white space (indents and spacing)
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

def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses)
                      for letter in word]
    print(" ".join(output_letters))

# guesses is correct_guesses (assigned to guesses for this function...because python)

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
    # print(letter_guess)
    user_attempts += 1
    if letter_guess in word:
        print(letter_guess + " is in the word! Guess another letter. ")
        current_guesses.append(letter_guess)
        # print(current_guesses)
    else:
        print(letter_guess + " is not in the word, try again. ")
        incorrect_letters.append(letter_guess)
        print(incorrect_letters)
    
    
    # this is where the function print_word is called to print out the correct letters and _ to display the word
    print_word(word, current_guesses)
