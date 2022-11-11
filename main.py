from ascii import logo
import random

secret_number = random.randint(1,100)
turns = 0

def start_game():
    global turns    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    difficulty = input("Choose a difficulty. Type 'easy', 'hard', or 'extreme': ").lower()

    if difficulty == "easy":
        turns = 10
    elif difficulty == "hard": 
        turns = 5
    elif difficulty == "extreme":
        turns = 1
    else:
        print("Invalid difficulty selection.")
        start_game()
    return turns

def get_guess():
    global user_guess
    print(f"\nYou have {turns} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    return user_guess

def check_guess():
    global turns
    turns -= 1
    if turns == 0:  
        print("You have run out of guesses, you lose!")
    elif user_guess == secret_number:
        turns = 0
        print(f"You got it! The number was {secret_number}.")
    elif user_guess > secret_number:
        print("Too high!")
        print("Guess again.")
    elif user_guess < secret_number:
        print("Too low!")
        print("Guess again.")
        

start_game()
while turns > 0:  
    get_guess()
    check_guess()