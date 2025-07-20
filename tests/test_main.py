import sys, os

# Add project root (one level up from tests/) into sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import io
import random
import tempfile
import pytest
from main import load_words, choose_word, is_word_guessed, display_progress, check_word_guess, parse_args


def test_load_words(tmp_path):
    # Create a temp file with some words and blank lines.
    content = "apple\n\nBanana\nCarrot   \n"
    file = tmp_path / "words.txt"
    file.write_text(content)

    words = load_words(str(file))
    assert words == ["apple", "Banana", "Carrot"]


def choose_word_with_seed():
    # Fix the random seed for predictability
    words = ["one", "two", "three"]
    random.seed(0)
    picked = choose_word(words)
    assert picked in words


def test_is_word_guessed_true():
    secret = "aba"
    guesses = ["a", "b"]
    assert is_word_guessed(secret, guesses) is True


def test_is_word_guessed_false():
    secret = "abc"
    guesses = ["a", "b"]
    assert is_word_guessed(secret, guesses) is False


def test_display_progress(capsys):
    secret = "dog"
    guesses = ["d", "g"]
    display_progress(secret, guesses)
    captured = capsys.readouterr()
    # Expect underscores for missing letters
    assert "d _ g" in captured.out


def test_check_word_guess_true():
    assert check_word_guess("raider", "raider")


def test_check_word_guess_false():
    assert not check_word_guess("puzzle", "raider")


def test_parse_args_defaults(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["word-raider"])
    args = parse_args()
    assert args.word_file == "words.txt"
    assert args.max_attempts == 6


def test_parse_args_custom(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["word-raider", "-f", "custom.txt", "-a", "8"])
    args = parse_args()
    assert args.word_file == "custom.txt"
    assert args.max_attempts == 8
