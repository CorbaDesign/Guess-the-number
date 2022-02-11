from art import logo
import random
print(logo)

TURNS_FOR_EASY = 10
TURNS_FOR_HARD = 5

number_to_guess = random.randint(1,100)

def check_number(your_guess, attempts):
  if your_guess == number_to_guess and attempts > 0:
    return "You got it. The answer was "
  elif your_guess > number_to_guess and attempts > 0:
    return "To high. \nGuess again"
  elif your_guess < number_to_guess and attempts > 0:
    return "To low. \nGuess again."
  elif your_guess < number_to_guess and attempts == 0:
    return "To low. \nYou've run out of guesses, you lose."
  else:
    return "To high. \nYou've run out of guesses, you lose."
#Chose difficulty levels
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
# print(f"Pssst, the correct answer is {number_to_guess}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
  attempts = TURNS_FOR_EASY
else:
  attempts = TURNS_FOR_HARD
playing = True

while playing and attempts > 0:
  if attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    your_guess = int(input("Make a guess:  "))
  if attempts == 0:
      playing = False
  attempts -= 1  
  if(check_number(your_guess, attempts)) != "You got it. The answer was " and attempts > 0: 
    print(check_number(your_guess, attempts))
  elif attempts == 0:
    print(check_number(your_guess, attempts))
  else:
    
    playing = False
    print(check_number(your_guess, attempts) + str(your_guess))
