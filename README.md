#Discord Trivia

A discord trivia game that uses old Jeopardy! questions

**Python Version**
This was tested on Python 3.6.0. I think it should run on any Python >= 3.5.x. 

**Gameplay**
To begin the game, type '!Trivia' into the channel you wish to play in. Type '!Kill' to end the game early. Once a game is begun, the bot listens to every message in the chat, and asks a new question when someone gets it right or when time expires (currently after 30 seconds).

**To Do**
At the moment it ends when 25 correct answers are reached. I haven't added any code to keep score yet, although it shouldn't be terribly difficult to do it. It is possible to cheat the answer-checking function. I figured it was better to have that than to require the user's answer and the correct answer to match exactly.

**Questions**
The questions that I used came from this reddit thread: https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/
