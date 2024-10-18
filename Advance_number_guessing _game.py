import random

def play_game():
    print("Welcome to the advanced number guessing game!")

    difficulty_levels = {"easy": 10, "medium": 7, "hard": 5}
    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty in difficulty_levels:
            attempts = difficulty_levels[difficulty]
            break
        else:
            print("Invalid input. Please choose again from the above options.")

    secret_number = random.randint(1, 100)
    print(f"You have {attempts} attempts to guess a number between 1 and 100.")

    for attempt in range(1, attempts + 1):
        guess = get_valid_input(f"Attempt {attempt}/{attempts}. Enter your guess: ", range(1, 100))
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempt} attempts!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        if attempt == attempts:
            print(f"Sorry, you're out of attempts. The correct number was {secret_number}.")

def get_valid_input(prompt, valid_range=None):
    while True:
        try:
            user_input = int(input(prompt))
            if valid_range and user_input not in valid_range:
                print(f"Please enter a number between {valid_range[0]} and {valid_range[-1]}.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play the game again? (yes or no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye, have a nice day!")
            break

if __name__ == "__main__":
    main()

 