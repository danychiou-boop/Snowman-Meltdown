"""Game logic for Snowman Meltdown."""

import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Select a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display snowman, word progress, and mistakes."""
    print("\n" + "=" * 30)
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:     ", display_word)
    print("Mistakes: ", mistakes)
    print("Guessed:  ", ", ".join(guessed_letters))
    print("=" * 30)


def is_word_guessed(secret_word, guessed_letters):
    """Return True if the whole word has been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False

    return True


def get_valid_guess(guessed_letters):
    """Ask the user for a valid single-letter guess."""
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter exactly one character.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def play_single_game():
    """Run one round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)

    while mistakes < max_mistakes and not is_word_guessed(
        secret_word,
        guessed_letters
    ):
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            mistakes += 1
            print("Wrong guess!")

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman!")
    else:
        print("The snowman melted!")
        print("The secret word was:", secret_word)


def play_game():
    """Run the game and ask whether the user wants to replay."""
    while True:
        play_single_game()

        replay = input("Do you want to play again? (y/n): ").lower()

        if replay != "y":
            print("Thanks for playing Snowman Meltdown!")
            break