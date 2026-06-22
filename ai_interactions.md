# AI Interactions Log

This file documents how AI assistance was used to debug, improve, and verify the game.

---

## Agent Workflow (SF8)

**What task did you give the agent?**
I asked the AI to investigate why the game logic and UI were inconsistent, especially around the secret number, attempts counter, hint messages, and score updates.

**What did the agent do?**
The AI helped trace the Streamlit rerun behavior, identify where session state was being updated too late, suggest fixes for the hint logic, and help move game logic into helper functions.

**What did you have to verify or fix manually?**
I had to check the final app behavior myself, confirm the attempts count was correct, and verify that the UI message and the logic stayed in sync.

---

## Test Generation (SF7)

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Invalid guess input | "Write a test for blank or non-numeric guesses" | Test that parse_guess rejects empty strings and invalid values | Yes | This confirms the app handles bad input safely |
| Difficulty ranges | "Write tests for each difficulty range" | Assertions for Easy/Normal/Hard range mapping | Yes | This ensures the correct bounds are used |
| Attempts cutoff | "Write a test for the last allowed guess" | Test that the game is only lost after the final guess is used | Yes | This checks the off-by-one behavior |
| Hint logic | "Write a test for too high / too low hints" | Assertions for correct hint messages | Yes | This verifies the comparison logic is correct |

---

## Linting & Style (SF9)

**Prompt used:**

```
Help me clean up the code and make the logic easier to understand while keeping the behavior the same.
```

**Linting output before:**

```
No major syntax errors after cleanup, but several logic and UI consistency issues were present.
```

**Changes applied:**
The AI helped separate logic into helper functions and improve readability, while I verified the functionality manually and through pytest.

---

## Model Comparison (SF11)

**Task given to both models:**
Compare how to explain the bug involving reruns, session state, and attempts tracking.

| | Model A | Model B |
|-|---------|---------|
| **Model name** | ChatGPT | Copilot |
| **Response summary** | Explained reruns and state updates clearly and focused on logic fixes | Also explained the issue well and suggested verification steps |
| **More Pythonic?** | Yes | Yes |
| **Clearer explanation?** | Slightly clearer for debugging flow | Slightly clearer for code structure |

**Which did you prefer and why?**
I preferred the explanation that connected the app behavior to the rerun cycle most directly, because that helped me understand why the UI looked one step behind.

