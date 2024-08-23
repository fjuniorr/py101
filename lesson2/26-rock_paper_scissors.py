"""Rock Paper Scissors"""

from collections import namedtuple
import random

CHOICES = ("rock", "paper", "scissors")

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
    print("rock, paper, scissors:")
    choice = input()
    return Play("alice", choice)

def get_computer_choice() -> Play:
    choice = random.choice(CHOICES)
    return Play("bob", choice)

def decide_winner(playA, playB) -> Play:
    """
    Given a pair of Plays (username, choice), return the tuple of the winner player or None in case of draw.
    """
    if playA.choice == playB.choice:
        return None
    if playA.choice == "rock" and playB.choice == "scissors":
        return playA
    if playA.choice == "scissors" and playB.choice == "paper":
        return playA
    if playA.choice == "paper" and playB.choice == "rock":
        return playA

    return playB

def display_winner(winner):
    print(winner)

if __name__ == "__main__":
    main()
