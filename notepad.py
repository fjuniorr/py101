# display scoreboard with clear screen
# allow [h]elp for accessing game rules
# display drawn in the same manner as winners

"""Rock Paper Scissors Spock Lizard"""

from collections import namedtuple
import random
import logging
import time
import os

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
    rounds = 0
    tally = {"player": 0, "computer": 0}
    while tally["player"] < 3 and tally["computer"] < 3:
        rounds += 1
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        winner = decide_winner(user_choice, computer_choice)
        display_winner(winner)
        
        tally = tally_result(winner, tally)
        display_scoreboard(tally, rounds)

Winner = namedtuple("Winner", ["play", "action"])
Play = namedtuple("Play", ["username", "choice"]) 

def tally_result(winner, tally):
    if winner and winner.play.username == "player":
        tally["player"] += 1
    if winner and winner.play.username == "computer":
        tally["computer"] += 1
    return tally

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
    game_result = get_result_message({playA.choice, playB.choice})
    if playA.choice == playB.choice:
        return None
    if playA.choice == "rock" and playB.choice in ("scissors", "lizard"):
        return Winner(playA, game_result)
    if playA.choice == "scissors" and playB.choice in ("paper", "lizard"):
        return Winner(playA, game_result)
    if playA.choice == "paper" and playB.choice in ("rock", "spock"):
        return Winner(playA, game_result)
    if playA.choice == "spock" and playB.choice in ("scissors", "rock"):
        return Winner(playA, game_result)
    if playA.choice == "lizard" and playB.choice in ("spock", "paper"):
        return Winner(playA, game_result)

    return Winner(playB, game_result)

def display_winner(winner: Winner):
    if winner:
        prompt("%s won! %s" % (winner.play.username.capitalize(), winner.action))
    else:
        prompt("Drawn!")
        
    print("...")
    time.sleep(2)
    os.system("clear")

def display_scoreboard(tally, rounds):
    horizontal_line = f"+-{'-'*26}-+"
    print(horizontal_line)
    print(f"|  Best of five ({rounds:02} rounds)  |")
    print("| Player (%d) vs Computer (%d) |" % (tally["player"], tally["computer"]))
    print(horizontal_line)

def get_result_message(choices):

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
