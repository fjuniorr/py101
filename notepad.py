# display scoreboard with clear screen
# allow [h]elp for accessing game rules

"""Rock Paper Scissors Spock Lizard"""

from collections import namedtuple
import random
import logging
import time
import os
import textwrap

logger = logging.getLogger(__name__)

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
        game_result = get_result_message({user_choice.choice, computer_choice.choice})
        if winner and winner.username == "player":
            tally["player"] += 1
            display_winner(winner, game_result)
            display_scoreboard(tally)
        if winner and winner.username == "computer":
            tally["computer"] += 1
            display_winner(winner, game_result)
            display_scoreboard(tally)

Play = namedtuple("Play", ["username", "choice"]) 

def get_user_choice() -> Play:
    message = f"""Choose one of:
- [r]ock
- [p]aper
- [sc]issors
- [l]izard
- [sp]ock"""
    prompt(message)
    choice = input()
    while is_user_choice_invalid(choice):
        prompt(f"{choice!r} is not valid. {message}")
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
    if playA.choice == "scissors" and playB.choice in ("paper", "lizard"):
        return playA
    if playA.choice == "paper" and playB.choice in ("rock", "spock"):
        return playA
    if playA.choice == "spock" and playB.choice in ("scissors", "rock"):
        return playA
    if playA.choice == "lizard" and playB.choice in ("spock", "paper"):
        return playA

    return playB

def display_winner(winner: Play, result_message):
    prompt("%s won! %s" % (winner.username.capitalize(), result_message))
    print("...")
    time.sleep(2)
    os.system("clear")

def display_scoreboard(tally):
    horizontal_line = f"+-{'-'*26}-+"
    print(horizontal_line)
    print("| Player (%d) vs Computer (%d) |" % (tally["player"], tally["computer"]))
    print(horizontal_line)

def get_result_message(choices):

 if len(choices) == 1:
    return "Draw!"
 if choices == {"lizard", "spock"}:
    return "Lizard poisons Spock."
 if choices == {"lizard", "paper"}:
    return "Lizard eats Paper."
 if choices == {"spock", "scissors"}:
    return "Spock smashes Scissors."
 if choices == {"spock", "rock"}:
    return "Spock vaporizes Rock."
 if choices == {"paper", "rock"}:
    return "Paper covers Rock."
 if choices == {"paper", "spock"}:
    return "Paper disproves Spock."
 if choices == {"scissors", "lizard"}:
    return "Scissors decapitates Lizard."
 if choices == {"scissors", "paper"}:
    return "Scissors cuts Paper."
 if choices == {"rock", "scissors"}:
    return "Rock crushes Scissors."
 if choices == {"rock", "lizard"}:
    return "Rock crushes Lizard."

def prompt(message):
    print(f"==> {message}")

if __name__ == "__main__":
    main()
