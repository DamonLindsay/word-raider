import random


def load_words(filename="words.txt"):
    with open(filename, "r") as f:
        return [word.strip() for word in f if word.strip()]


def choose_word(words):
    return random.choice(words)


def main():
    words = load_words()
    secret = choose_word(words)
    print("Welcome to Word Raider!")
    # TODO: game loop goes here


if __name__ == "__main__":
    main()
