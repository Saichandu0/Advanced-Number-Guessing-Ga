import  random


def get_valid_input(prompt, valid_range=None):
    while True:
        try:
            user_input = int(input(prompt))
            if valid_range and user_input not in valid_range:
                print(f"Please enter a number between {valid_range[0]} and {valid_range[-1]}.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
 print ("welcome to the advance number guessing game!")
 

def diffuculty_level():
 diffuculty_level+{"easy":10, "medium":7, "hard":5}
 while True:
  diffuculty= input("choose a duffucult level(easy, medium, hard): ").loweer()
  if diffuculty in diffuculty_level:
   attempt= diffuculty_level[diffuculty]
   break
  else :
   print("Invalid input . please choose again from the abve options.")



   secret_number= random.randint(1, 100)
   print (f"You have{attempts} attempts to guess a number between 1 to 100.")

   for attempts in range(1, attempts + 1):
     guess = get_valid_input(f"Attempt {attempt}/{attempts}enter your guess:", range(1, 100))
     
     if guess== secret_number:
      print(f"Congratulations! You have guessed the the correct number{secret_number} in {attempt} attpemts!")
      
      break
     elif guess < secret_number:
      print("Too low")

     else:
      print( "Too high")

      if attempt== attempts:
       print(f" Sorry you are out of attempts and the correct answer is {secret_number}")




def get_valid_input(prompt, valid_range=None):
    while True:
        try:
            user_input = int(input(prompt))
            if valid_range and user_input not in valid_range:
                print(f"Please enter a number between {valid_range[0]} and {valid_range[-1]}.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")



def main():
  while True:
    play_game()
    play_again = input(" Do you want to play the game again? (say yes or no):").lower()
    if play_again != "yes":
      print("thanks for playing! Goodbye have a nice day!")
      break
    if __name__ == "__main__":
      main()
    
 
 