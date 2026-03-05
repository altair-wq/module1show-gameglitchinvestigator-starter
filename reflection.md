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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
