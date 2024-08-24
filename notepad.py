"""Rock Paper Scissors Spock Lizard"""

from collections import namedtuple
import random

CHOICES = {
    "rock": "rock",
    "r": "rock",
    "paper": "paper",
    "p": "paper",
    "scissors": "scissors",
    "sc": "scissors",
    "lizard": "lizard",
    "l": "lizard",
    "spock": "spock",
    "sp": "spock",
}

def main():
    """
    Program entry point
    """
    tally = {"player": 0, "computer": 0}
    while tally["player"] < 3 and tally["computer"] < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = decide_winner(user_choice, computer_choice)
        if winner and winner.username == "player":
            tally["player"] += 1
            display_winner(winner, tally)
        if winner and winner.username == "computer":
            tally["computer"] += 1
            display_winner(winner, tally)

Play = namedtuple("Play", ["username", "choice"]) 

def get_user_choice() -> Play:
    message = f'Choose one of [r]ock, [p]aper, [sc]issors, [l]izard, [sp]ock:'
    print(message)
    choice = input()
    while is_user_choice_invalid(choice):
        print(f"{choice} is not valid. {message}")
        choice = input()
    return Play("player", CHOICES[choice])

def is_user_choice_invalid(choice: str):
    return choice not in CHOICES

def get_computer_choice() -> Play:
    choice = random.choice(list(set(CHOICES.values())))
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

def display_winner(winner: Play, tally: dict):
    print("%s won! (%d, %d)" % (winner.username, tally["player"], tally["computer"]))

if __name__ == "__main__":
    main()
