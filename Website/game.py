import random
import requests

def choose_word():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    word = response.json()[0]
    return word

def display_word(word, guessed_letters, revealed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters or letter in revealed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
def randomly_reveal_letters(word):
    num_to_reveal = random.randint(1, len(word)//2)  # You can adjust the number of letters to reveal
    revealed_letters = random.sample(word, num_to_reveal)
    return revealed_letters
def draw_hangman(attempts):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]

    return stages[6 - attempts]

def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    revealed_letters = randomly_reveal_letters(word_to_guess)
    print(display_word(word_to_guess, guessed_letters, revealed_letters))
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(draw_hangman(attempts))  # Draw the hangman

            print(f"Wrong guess! Attempts remaining: {attempts}")
        
        current_display = display_word(word_to_guess, guessed_letters, revealed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break

    if "_" in current_display:
        print(f"Sorry, you've run out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()