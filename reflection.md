# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it? First time I ran, it worked as a basic number guesser where it generated a random secret number and let me pick a difficulty mode and submit guesses
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  Bug 1 “New Game” doesn’t fully reset the game, clicking “New Game” should reset everything (secret number, attempts, score/round state) and start a fresh round immediately, but the button seems to update only the secret number, full game doesn’t reset correctly unless I manually reload the page.
  Bug 2 Hints are backwards (“Go higher” vs “Go lower”), it should have been this way if my guess is lower than the secret number, the hint should say “Go higher.” If my guess is higher, it should say “Go lower." but the game gives the opposite hint (e.g., telling me to go lower when my guess is already too low).
  Bug 3 Attempts / history behave inconsistently (duplicates / extra attempts), in Easy mode, the game should allow the stated number of attempts (e.g., 3) and each guess should appear once in the guess history/debug info, I was able to make more attempts than expected (e.g., I could submit a 4th guess in Easy). Also, the guess history sometimes duplicates entries (e.g., the second guess shows the first guess again), and the developer/debug info doesn’t reliably reflect the guesses.
  Bug 4 Input validation does not enforce the number range, If the game says the guessing range is 1–100, the player should only be able to enter numbers within that range. Inputs like 120 or -5 should be rejected with an error message. But the game allows guesses outside the allowed range. For example, I was able to enter 120 even though the game states the range is 1–100, and the guess was still processed normally.
  Bug 5 Secret number generation ignores the difficulty range, when I choose a difficulty mode, the secret number should be generated within that mode’s allowed range (e.g., Easy: 1–20, Hard: 1–50, etc.). The game should never generate a secret number outside the difficulty range, but in fact even when I selected a mode with a smaller range (like Easy or Hard), the game generated a secret number larger than that range. This makes the round unfair/impossible to play correctly, because the player is told to guess within a limit that the actual secret number can exceed.
  Copilot analysis: I asked Copilot to explain the parse_guess function. It pointed out that the code only checks for None or an empty string, but inputs like spaces (" ") or other non-numeric values can pass through. This may cause incorrect hints or errors later when the game tries to compare the guess to the secret number. My judgment: I agree that the input should be cleaned and validated (e.g., stripping whitespace and converting to an integer) before the game processes the guess.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used GitHub Copilot and ChatGPT. Copilot helped me inside VS Code with explaining functions and suggesting code fixes, while ChatGPT helped me understand bugs conceptually and plan how to fix them step by step.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). Copilot correctly identified that the check_guess function had reversed hint messages, where a guess that was too high told the player to go higher instead of lower. I verified this by reading the code, fixing the messages, and then testing both manually and with pytest to confirm the hints behaved correctly.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).One AI suggestion was to refactor multiple parts of the app at once instead of focusing on specific bugs. This was misleading because it would make debugging harder by mixing many changes together. I verified this by comparing it to my debugging approach and chose to fix one bug at a time instead, which made it easier to test and confirm each fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I considered a bug fixed only when both the code behavior and the game UI matched the expected logic. I tested each fix manually in the Streamlit app to see if the gameplay behaved correctly, and I also checked that the underlying function produced the right output. If both matched, I treated the bug as resolved.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code. I wrote pytest tests for the check_guess function. For example, I tested that when the guess is 60 and the secret is 50, the outcome is "Too High" and the message contains "LOWER". This confirmed that the hint logic was correctly fixed and no longer reversed.
- Did AI help you design or understand any tests? How? Yes, AI helped me generate the initial structure of the pytest tests and suggested what cases to include (win, too high, too low). However, I had to adjust the imports and verify that the tests matched my refactored logic_utils.py. This showed me that AI can help draft tests, but I still need to understand the code to make them run correctly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app. The secret number kept changing because Streamlit reruns the entire script every time the user interacts with the app. If the secret number is not properly stored in st.session_state, it can be regenerated on each rerun, or updated inconsistently when other parts of the code execute.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? I would explain that Streamlit works by re-running the whole Python script every time the user clicks a button or enters input. st.session_state acts like memory that stores values between these reruns, so important data like the secret number or score doesn’t reset every time the app refreshes.
- What change did you make that finally gave the game a stable secret number? I made sure the secret number is stored in st.session_state and only generated when needed, such as at the start of the game, when the user clicks “New Game,” or when the difficulty changes. This prevented the secret from changing unexpectedly during normal gameplay.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? One habit I want to reuse is fixing one bug at a time and testing it immediately before moving on. This helped me clearly connect each change to its effect and avoid breaking other parts of the code. It also made debugging more structured and less overwhelming.
- What is one thing you would do differently next time you work with AI on a coding task? Next time, I would use more focused prompts from the beginning and avoid accepting large refactors early. I learned that smaller, targeted AI suggestions are easier to verify and integrate without introducing new bugs.
- In one or two sentences, describe how this project changed the way you think about AI generated code. This project showed me that AI-generated code can look correct but still contain multiple logical bugs. AI is useful for debugging and generating ideas, but I need to verify every suggestion and understand the code myself before trusting it.
