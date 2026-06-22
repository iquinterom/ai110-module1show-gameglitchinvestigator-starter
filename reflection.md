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
--- In one of the test that it did to fix the hint, which was wron it ran the pytest and it said that all the test passed but when i went to test it manually in the local host it was actually not passing. I advised it to checked it again and to redo the test. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- After debuging each bug, I manually went and tested it in the localhost streamlit.
--- The first test that I did manually was the range dynamic that we needed to showcase in the UI, that one i ran it manually and made the changes based on Claude's suggestions
--- Yes it design a series of test, but the issue is that all the test passed in the terminal, but in the localhost sometimes it keeps failing so i had to explain again and send screenshots so Claude can understand the issue. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Strimlit is a local web page that refreshes it self. Every time you update your code strimlit runs it and you can see the changes live. It has a page memory so it can rerun the changes. It is easire for debugging. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- I think that being precise and providing examples to claude it helps fixing the issues. Also, when it comes to testing I need to learn how to test before i can provide claude with examples. The test ran successfully, but some needed to show failed so i can know what part of the code fails, and we can test that code directly. 
--- AI generated code is good as long as you also know the ins and outs of your code. For example, vibe coding is good if you know how to code. It's just a tool that helps you generate code faster and UI, but if you know how the code works or what exacly you are doing if not then you will just follow whatever the AI is doing and thinking that everything is good, but at the end is not. Same here generating pytest is good if you know what exacly what you are testing, and at the beginning testign manually will be necessary. 
