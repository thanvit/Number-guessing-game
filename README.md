# 🎲 Number Guessing Game

A simple Python console-based game where the player tries to guess a secret number within a limited number of attempts. The difficulty level determines how many chances the player gets.

---

## 📖 How It Works
1. The program selects a secret number (currently set to `67`).
2. The player chooses a difficulty level:
   - **Easy** → 10 chances
   - **Medium** → 5 chances
   - **Hard** → 3 chances
3. The player enters guesses until:
   - They guess correctly 🎉
   - Or they run out of attempts ❌

---

## 🕹️ Features
- Multiple difficulty levels
- Tracks remaining attempts
- Ends immediately when the correct guess is made
- Input validation for difficulty selection

---

## 🚀 Getting Started
### Prerequisites
- Python 3.x installed on your system

### Run the Game
```bash
python guessing_game.py
