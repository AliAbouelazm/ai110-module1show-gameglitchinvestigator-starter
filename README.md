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
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** A number guessing game where the player tries to guess a hidden number within a limited number of attempts. The difficulty setting controls the number range (Easy: 1–20, Normal: 1–100, Hard: 1–50) and the number of allowed attempts. After each guess the game gives a directional hint and tracks a running score.

- [x] **Bugs found:**
  1. **Secret number kept changing** — `random.randint()` was called at the top level of the script, so Streamlit regenerated a new secret on every rerun (every button click), making it impossible to win.
  2. **Hints were backwards** — `"Too High"` displayed "Go HIGHER!" and `"Too Low"` displayed "Go LOWER!", the opposite of what they should say.
  3. **Attempt counter was off by one** — the attempts display rendered before the increment ran, so it always showed one attempt behind.

- [x] **Fixes applied:**
  1. Wrapped the secret assignment in `if "secret" not in st.session_state:` so it only generates once per game.
  2. Swapped the hint messages so `"Too High"` → "Go LOWER!" and `"Too Low"` → "Go HIGHER!".
  3. Moved `st.session_state.attempts += 1` to before the `st.info` display so the count updates immediately on submit.
  4. Refactored `get_range_for_difficulty`, `parse_guess`, and `update_score` from `app.py` into `logic_utils.py`.

## 📸 Demo

- [x] ![Winning game screenshot](Screenshot%202026-03-11%20at%2012.49.51%20PM.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
