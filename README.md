#Discord Trivia

A discord trivia game that uses old Jeopardy! questions

**Python Version**
This was tested on Python 3.6.0. I think it should run on any Python >= 3.5.x. 

**Gameplay**
To begin the game, type '!Trivia' into the channel you wish to play in. Type '!Kill' to end the game early. Once a game is begun, the bot listens to every message in the chat, and asks a new question when someone gets it right or when time expires (currently after 30 seconds).

The number of questions that a player must answer defaults to 25. That number can be overridden when you begin the game by including a number when starting the game (e.g., "!Trivia 50").

Typing "!Trivia" while in game will tell you the score of the current leader. If a player has not set a nickname, he will be referred to by the bot as "None."

**Questions**
The questions that I used came from this reddit thread: https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/
