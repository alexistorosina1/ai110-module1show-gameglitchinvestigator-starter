# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input    | Expected Behavior    | Actual Behavior    | Console Output / Error |
| -------- | -------------------- | ------------------ | ---------------------- |
| guess:50 | hint: go lower       | hint: go higher    | none                   |
| guess    | add guess to history | misses some inputs | none                   |
| new game | reset all values     | resets secret only | none                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

* I used Claude for this project

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

* Claude's suggestion for the comparison from the guess and the secret was correct because the previous glitched game was silently breaking. It was comparing a string to an int.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

* One example of misleading was when I told Claude that the guess logic is wrong, Claude got rid of the input box for the guessing.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

* after running tests and double checked if the errors were fixed i closed the terminal and restarted the game to double check if it is good.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - one test i ran manual was the attempts. I had to be sure the attempts weren't off by 1 or not reading the attempts
- Did AI help you design or understand any tests? How?

* I asked AI to create tests for me

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

* One thing I would do better is git commit my changes more often, so I can continue to actually realize what I am doing and not just vibe code.
