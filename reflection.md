# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game has a sidebar on the laft indicating the diffculty level as well as the rules for that difficulty. The main section of the screen has the game itself which prompts the user to guess the hidden number in a certaina mount of attempts. It looks very basic but straightforward and self explanatory.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The hints always told the user to "go lower" even if the secret number was higher than the guess. The number of attmepts is 1 off and does not accurately indicate how many attempts the user has left.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude Code (Claude Sonnet) as my primary AI tool throughout this project to help identify bugs and understand the Streamlit session state model.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  AI correctly explained that the secret number kept resetting because Streamlit reruns the entire script on every interaction, so any variable not stored in `st.session_state` gets regenerated. I verified this by wrapping the secret assignment in `if "secret" not in st.session_state:` and confirming the number stayed fixed across button clicks in the debug panel.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  AI initially suggested the hints bug might be caused by a comparison using string types rather than integers, implying the fix only required type casting. While type casting was part of the fix, the root cause was actually that the hint messages were mapped to the wrong outcomes ("Too High" was displaying "Go LOWER!" and vice versa), which I confirmed by reading the original `check_guess` function directly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I considered a bug fixed only when both manual testing in the running app and the relevant pytest test passed. For the hints bug, I manually submitted guesses above and below the secret (visible in the debug panel) and confirmed the hint directions matched reality before calling it done.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  Running `pytest tests/test_game_logic.py` showed that `test_guess_too_high` passed after fixing `check_guess` in `logic_utils.py`. Before the fix, the function was returning "Too Low" when the guess was higher than the secret, which caused all direction-based tests to fail.
- Did AI help you design or understand any tests? How?
  AI helped me understand why regression tests for string inputs (like `test_guess_too_high_with_string_secret`) were necessary. It explained that Streamlit could pass the secret as a string in certain edge cases, so testing `check_guess(60, "50")` ensures the function handles type mismatches gracefully rather than producing wrong comparisons.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The original app called `random.randint(low, high)` at the top level of the script every time. Since Streamlit reruns the entire script from top to bottom on every user interaction (button click, input change, etc.), a new random number was generated on each rerun, making it impossible to consistently guess the "same" secret.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Imagine Streamlit as a whiteboard that gets completely erased and redrawn every time you click anything. If you want something to survive the erase — like the secret number — you have to write it in a special notebook called `st.session_state`. Anything only on the whiteboard (a regular Python variable) disappears and gets recreated fresh on every click.
- What change did you make that finally gave the game a stable secret number?
  I wrapped the secret number assignment in a guard: `if "secret" not in st.session_state: st.session_state.secret = random.randint(low, high)`. This ensures the secret is only generated once and stored in session state, so it persists across all subsequent reruns until the player explicitly starts a new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  Writing regression tests immediately after fixing a bug. Once I fixed the hints logic, I added tests for the string-input edge cases right away so that any future change to `check_guess` would instantly catch a regression rather than letting it silently slip through.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would verify AI explanations against the actual source code before accepting them rather than trusting the AI's diagnosis at face value. In this project I initially accepted the "it's just a type casting issue" explanation before actually reading the function and discovering the swapped message mapping.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI-generated code can look clean and complete while hiding subtle logical bugs that only surface during real usage. I now treat AI output as a first draft that needs the same careful review I would give any code written by a junior developer — read it, test it, and don't ship it without verification.
