#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

answer = random.randint(1, 100)

difficulty_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_mode == "easy":
    number_of_tries = 10
else:
    number_of_tries = 5


while number_of_tries > 0:
    print(f"You have {number_of_tries} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))

    if guessed_number == answer:
        print(f"You got it! The answer was {answer}.")
        break

    elif guessed_number > answer:
        print("Too high.")

    else:
        print("Too low")

    number_of_tries -= 1
    

if number_of_tries == 0 :
    print(f"You have run out of guesses, you lose.")
    
