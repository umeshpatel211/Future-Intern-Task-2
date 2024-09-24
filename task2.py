'''Create a program that allows users to play the classic game of rock, paper,
scissors against the computer. The user will input their choice, and the computer 
will randomly select one of the three options. The program will then determine
the winner based on the rules of the game and display the result. The game 
will continue until the user decides to stop playing.'''

import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

# Start the game
play_game()
