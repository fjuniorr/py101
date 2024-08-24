"""Rock Paper Scissors Spock Lizard"""

from collections import namedtuple
import random

CHOICES = ("rock", "paper", "scissors", "lizard", "spock")

def main():
    """
    Program entry point
    """
    winner = None
    while not winner:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = decide_winner(user_choice, computer_choice)
    display_winner(winner)

Play = namedtuple("Play", ["username", "choice"]) 

def get_user_choice() -> Play:
    print(", ".join(CHOICES), ":", sep="")
    choice = input()
    return Play("player", choice)

def get_computer_choice() -> Play:
    choice = random.choice(CHOICES)
    return Play("computer", choice)

def decide_winner(playA, playB) -> Play:
    """
    Given a pair of Plays (username, choice), return the tuple of the winner player or None in case of draw.
    """
    if playA.choice == playB.choice:
        return None
    if playA.choice == "rock" and playB.choice in ("scissors", "lizard"):
        return playA
    if playA.choice == "scissors" and playB.choice == ("paper", "lizard"):
        return playA
    if playA.choice == "paper" and playB.choice == ("rock", "spock"):
        return playA
    if playA.choice == "spock" and playB.choice == ("scissors", "rock"):
        return playA
    if playA.choice == "lizard" and playB.choice == ("spock", "paper"):
        return playA

    return playB

def display_winner(winner):
    print(winner)

if __name__ == "__main__":
    main()
