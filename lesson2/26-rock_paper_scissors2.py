# Bonus
# Notice how the display_winner function calls the prompt function. What happens if you move the display_winner function definition above the prompt function definition? Does it still work?
# How would you use the display_winner function differently if it returned a string, as opposed to outputting the string directly?
# We used a while loop with an always-true condition and a break statement to decide whether to replay the game. Can you rewrite the loop so that we don't need to use the break statement to stop the loop?

import random

VALID_CHOICES = ["rock", "paper", "scissors"]

def prompt(message):
    print(f"==> {message}")

def resolve_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        return "You win!"
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        return "Computer wins!"
    else:
        return "It's a tie!"

def play_again():
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    
    while answer not in ("y", "n"):
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer == "y":
        return True
    else:
        return False

def play():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    winner = resolve_winner(choice, computer_choice)
    prompt(winner)

play()
while play_again():
    play()
