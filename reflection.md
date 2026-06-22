# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Difficulty level    |the range is off for easy is 1 to 20, Normal is 1 to 100, and Hard is 1=50 |Message under Make a guess stays as "Guess number between 1 and 100. Atempts left: #   | Guess a number betwween does't change and in the Attempsts left the number is off by one in all levels   |
|Enter your guess number   |Submit Guess by pressign enter on keyboard   |you need to submit by clicking button Submit Guess | sometimes by pressing the keyboard enter it submits but sometimes it doesn't submit  |
|new game does not clear the enter your guess or refreshes as new game|It should clear the enter your guess/or start as new game |I get a message "Game over. Start a new game to try again." | Should clear game and start new one |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I use Claude.
--- I provided information of one of glitches such as that the difficulty level and attempt number is off in all there levels. Claude responded with why the message is wrong and in what page the UI message was hardcoded.  It provided suggestions on how to correct it. I verify the results by making the changes that it was suggested and once I applied them the UI message was providing the correct information. 
--- 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
