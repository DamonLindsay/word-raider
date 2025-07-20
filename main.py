import random
from typing import List


def load_words(filename: str = "words.txt") -> List[str]:
    """
    Load words from a file, one per line, stripping whitespace and ignoring blanks.

    :param filename: Path to the word bank file.
    :return: A list of words.
    """
    with open(filename, "r") as f:
        return [word.strip() for word in f if word.strip()]


def choose_word(words: List[str]) -> str:
    """
    Select a random word from the provided list.

    :param words: List of candidate words.
    :return: A single word as the secret.
    """
    return random.choice(words)


def get_guess(already_guessed: List[str]) -> str:
    """
    Prompt the user for a single-word guess, validate it hasn't been tried before and is alphabetic.

    :param already_guessed: List of previous guesses to prevent repeats.
    :return: The validated guess in lowercase.
    """
    while True:
        guess = input("Enter your guess: ").strip().lower()
        if not guess.isalpha():
            print("Invalid: please enter letters only.")
        elif guess in already_guessed:
            print(f"You already tried '{guess}'.")
        else:
            return guess


def display_progress(secret: str, guesses: List[str]) -> None:
    """
    Show the current state of the word, revealing letters guessed and hiding others as underscores.

    :param secret: The secret word to guess.
    :param guesses: All letters guessed so far.
    """
    display = " ".join([char if char in guesses else "_" for char in secret])
    print(f"Word: {display}")


def is_word_guessed(secret: str, guesses: List[str]) -> bool:
    """
    Check if all letters in the secret have been guessed.

    :param secret: The secret word.
    :param guesses: All letters guessed so far.
    :return: True if fully guessed, else False.
    """
    return all(char in guesses for char in secret)


def main() -> None:
    """
    Run the Word Raider game: load words, choose secret, track guesses, and loop until win/lose.
    """
    words = load_words()
    secret = choose_word(words)
    print("Welcome to Word Raider!\nGuess the secret word, one letter at a time.")
    max_attempts = 6
    attempts = 0
    guesses: List[str] = []

    while attempts < max_attempts and not is_word_guessed(secret, guesses):
        display_progress(secret, guesses)
        guess = get_guess(guesses)
        guesses.append(guess)

        if guess in secret:
            print(f"Good job!  '{guess}' is in the word.")
        else:
            attempts += 1
            print(f"Sorry, '{guess}' is not in the word.  Attempts left: {max_attempts - attempts}")

    if is_word_guessed(secret, guesses):
        print(f"🎉 Congrats!  You guessed '{secret}' correctly!")
    else:
        print(f"😢 Out of attempts!  The word was '{secret}'.  Better luck next time.")


if __name__ == "__main__":
    main()
