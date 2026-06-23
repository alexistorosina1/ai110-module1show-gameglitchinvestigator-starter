# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.**
      The game is a number guessing game built with Streamlit. The app picks a secret number within a range set by the chosen difficulty (Easy 1–20, Normal 1–100, Hard 1–50). The player guesses, gets a "higher/lower" hint after each attempt, and earns points for winning within the attempt limit.

- [x] **Detail which bugs you found.**
  1. **Reversed hints** — a guess that was too high told the player to "Go HIGHER!" and a guess that was too low told them to "Go LOWER!".
  2. **Shape-shifting secret** — the secret was cast to a string on every other attempt, so `int` vs `str` comparisons silently broke and the secret appeared to change.
  3. **Wrong attempt count** — `attempts` was seeded at `1`, throwing off the "Attempts left" display and scoring.
  4. **Incomplete "New Game" reset** — clicking "New Game" only reset the secret, leaving stale score, status, and history, and re-drew from a hard-coded 1–100 range instead of the current difficulty.

- [x] **Explain what fixes you applied.**
  - Flipped the hint directions in `check_guess` (too high → "Go LOWER", too low → "Go HIGHER").
  - Always compared the guess against the raw `int` secret, removing the string cast.
  - Seeded `attempts` at `0` so the count and scoring line up.
  - Made "New Game" reset score, status, history, and attempts, and draw the new secret from the selected difficulty's range.
  - Refactored `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` out of `app.py` into `logic_utils.py` so the logic is unit-testable, then added pytest coverage.

## 📸 Demo Walkthrough

A step-by-step playthrough of the fixed game, so a reader can follow along without a video:

1. **Launch the app.** Run `python -m streamlit run app.py` and open the browser tab. The title "🎮 Glitchy Guesser" appears with a difficulty selector.
2. **Pick a difficulty.** Choose "Normal" — the info banner now correctly reads "Guess a number between 1 and 100. Attempts left: 5". (On "Easy" the range is 1–20, on "Hard" it's 1–50.)
3. **Peek at the secret (optional).** Expand "Developer Debug Info" to confirm the secret number, attempts (starts at 0), score (starts at 0), and history are all tracked correctly. The secret no longer changes between guesses.
4. **Make a first guess.** Type `50` and click "Submit". Because 50 is higher than the secret (say, 37), the hint correctly reads "📉 Go LOWER!" — the directions are no longer reversed. "Attempts left" drops to 4 and the guess is added to history.
5. **Make a second guess.** Type `30`. Since 30 is lower than 37, the hint correctly reads "📈 Go HIGHER!". The secret stays fixed at 37 across both submits.
6. **Win the game.** Type `37` and click "Submit". The app shows "🎉 Correct!", awards points based on the attempt number, updates the score, and marks the game as over.
7. **Start a new game.** Click "New Game". Score, status, history, and attempts all reset cleanly, and a fresh secret is drawn from the current difficulty's range (not a hard-coded 1–100).

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest test/
============================= test session starts ==============================
platform darwin -- Python 3.8.13, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/alexistorosina/Desktop/codepath/ai110-module1show-gameglitchinvestigator-starter
collected 2 items

test/test_game_logic.py ..                                               [100%]

============================== 2 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
