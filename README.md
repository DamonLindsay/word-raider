# Word Raider 🎮
![CI](https://github.com/DamonLindsay/word-raider/actions/workflows/python-app.yml/badge.svg)

## 📋 Overview

Word Raider is an interactive, command-line word-guessing game written in Python. Players try to uncover a secret word one letter at a time (or by guessing the full word) before running out of attempts. This project demonstrates core Python concepts such as file handling, loops, conditionals, CLI parsing, and unit testing.

## ⚙️ Features
- Load a customizable word bank from a text file.
- Guess single letters or attempt the full word.
- Configurable maximum number of incorrect guesses.
- Clear progress display and feedback after each guess.
- Comprehensive unit tests for core logic.
- Continuous Integration (CI) suite running tests across Python versions 3.8-3.11

## 🚀 Installation
`1.` **Clone the repository**
```bash
git clone https://github.com/DamonLindsay/word-raider.git
cd word-raider
```
`2.` **Create and activate a virtual environment**
```
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell   
.\.venv\Scripts\activate    

```
`3.` **Install dependencies**
```
pip install -r requirements.txt     # if additional dependencies exist
pip install pytest                  # for running tests
```

## 🏃‍♂️ Usage
Run the game with default settings:
```bash
python main.py
```
Specify a custom Word file and/or maximum attempts:
```
python main.py --word-file custom_words.txt --max-attempts 8
```

## 🧪 Testing
Unit tests are written with pytest.  To run them:
```
pytest -q
```
Make sure your virtual environment is active so it uses the correct Python interpreter.

## 🤝 Contributing
`1.` Fork the repo and create a feature branch:
```
git checkout -b feature/YourFeature git add . git commit -m "feat: add My New Feature"
```
`2.` Push your branch and open a Pull Request on GitHub.
`3.` CI will run automatically; ensure all tests pass before requesting a review.

## 📄 License
This project is licensed under the [MIT License](LICENSE)

---
*Happy raiding!* 🚀