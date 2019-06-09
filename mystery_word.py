
word = "sun"
tries = 8
user_attempts = 1
current_guesses = []
incorrect_letters = []

def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses) 
                      for letter in word]
    print(" ".join(output_letters))

def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"

[display_letter(letter, current_guesses)
 for letter in word]
    
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













