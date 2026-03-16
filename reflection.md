# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  When I first ran the game I only noticed that the logic was totally wrong. It says goes lower when I had to go higher so I started looking for bugs from that issue.

- List at least two concrete bugs you noticed at the start  
   (for example: "the secret number kept changing" or "the hints were backwards").
  Here are the list of bugs I discovered (also with the help of Claude)
  1 - When the number is too high, it says go higher instead of go lower and vice-versa.
  2 - Default count of attempts start from 1 instead of 0.
  3 - If the guess is even it is converted to string where "5" will be greater than "15".
  4 - When a new game is reloaded it sets from 1 to 100 irrespective of the difficulty level.
  5 - If the outcome is too high and attempt number is even score is increased which shouldnt.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The 3rd bug in my list is something i discovered with the help of Claude. I then tried it by checking numbers like "4,23; 5:15; 6:34"

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Claude suggested that if difficulty is hard then it shouldnt be in range of 1 to 50 even with 5 attempts as it wouldnt be that hard mathematically compared to normal level. But we are not looking for that type of bugs. We have a specific range and attempts for every level.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  First I ran using self generated test cases and then wrote test_game_logic.py using AI and ran it.

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  One of the bugs which was most confusing to me was the number getting converted to string if its even. I spent some time on that big. And as mentioned in detail with sample testcases in question 2, I manually tested them and also tested using pytest under test_check_guess_no_string_comparison function.

- Did AI help you design or understand any tests? How?
  AI generated the test_game_logic.py as I'm not familiar with writing test files. Other manual work is done by me.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The actual secret number stored in session state never changed, but the variable being passed into check_guess was alternating between an int and a string every attempt.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  reruns - Every button click refreshes the whole page and re-executes every line of code.
  Session state - Imagine playing a board game, but every turn someone flips the table and resets everything. Session state is like writing your score on a sticky note before the table flips, so you can read it back after.

- What change did you make that finally gave the game a stable secret number?
  The secret number was never actually changing — the bug was that every even attempt, the code converted it to a string using str(st.session_state.secret) before passing it to check_guess. This caused wrong comparisons because Python compares strings differently than integers. The fix was removing that conversion and always passing the secret directly as an int.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    Writing pytest tests right after fixing a bug. It forced me to actually prove the fix worked instead of just assuming it did, and it would catch the bug again immediately if something broke it later.

- What is one thing you would do differently next time you work with AI on a coding task?
  would verify AI suggestions before accepting them instead of just copying them. In this project the AI helped catch real bugs, but it also made small mistakes like the wrong expected value in the score test, which I had to correct myself.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI generated code looks clean and confident but can have subtle logical bugs that are easy to miss on a quick read. You still need to understand the code yourself to catch the mistakes the AI doesn't.
