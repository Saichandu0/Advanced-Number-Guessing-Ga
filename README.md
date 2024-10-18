# Advanced-Number-Guessing-Ga
We are going to design and implement an interactive number guessing game in Python. The game will challenge the player to guess a randomly generated number within a predefined range and limited number of attempts.The complexity of the game will test the player’s ability to make educated guesses while introducing difficulty levels, input validation, and replay functionality.

Requirements:
Game Setup:

The game should randomly generate a secret number between 1 and 100.
The player will have a limited number of attempts to guess the secret number based on the chosen difficulty level:
Easy: 10 attempts
Medium: 7 attempts
Hard: 5 attempts
After each incorrect guess, the game should provide feedback on whether the guess was too high or too low.
Input Validation:

The program should handle invalid inputs (e.g., non-numeric guesses or invalid difficulty levels) by prompting the player to enter valid data without consuming an attempt.
Game Flow:

The player should be prompted to choose the difficulty level at the start of the game. If they enter an invalid difficulty, they should be prompted again until a valid option is selected.
During each round, the player will enter their guess. If the guess is valid (a number within the range), the game will proceed to check it. Invalid guesses should prompt a re-entry without counting as an attempt.
Win/Loss Conditions:

The game ends if the player guesses the secret number within the allowed attempts.
If the player runs out of attempts, the game should reveal the correct number and indicate that the player lost.
Replay Functionality:

After a win or loss, the player should be prompted to play again. If the player chooses to play again, the game should reset and start a new round. If the player declines, the game should terminate.

