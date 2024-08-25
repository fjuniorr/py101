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
    """Program entry point"""
    play_best_of_five()
    while keep_going():
        play_best_of_five()

def play_best_of_five():
    """Play a single game of best of five"""
    rounds = 0
    tally = {"player": 0, "computer": 0}
    while tally["player"] < 3 and tally["computer"] < 3:
        rounds += 1
        user_choice = get_user_choice()
        if user_choice.choice == "help":
            display_help()
            continue
        computer_choice = get_computer_choice()

        winner = decide_winner(user_choice, computer_choice)
        display_winner(winner)

        tally = tally_result(winner, tally)
        display_scoreboard(tally, rounds)

Winner = namedtuple("Winner", ["play", "action"])
Play = namedtuple("Play", ["username", "choice"])

def tally_result(winner, tally):
    """Determine winner and tally results for scoreboard"""
    if winner and winner.play.username == "player":
        tally["player"] += 1
    if winner and winner.play.username == "computer":
        tally["computer"] += 1
    return tally

def get_user_choice() -> Play:
    """Get a valid user choice"""
    message = """Choose one of (or [h]elp for game rules):
- [r]ock
- [p]aper
- [sc]issors
- [l]izard
- [sp]ock"""
    prompt(message)
    choice = input().strip().lower()
    while is_user_choice_invalid(choice):
        prompt(f"{choice!r} is not valid. {message}")
        choice = input().strip().lower()
    return Play("player", CHOICES.get(choice, "help"))

def is_user_choice_invalid(choice: str):
    """Returns True if user choice is invalid.
    
    Allows user asking for help.
    """
    return choice not in CHOICES and choice not in ["help", "h"]

def get_computer_choice() -> Play:
    """Select a random play for computer"""
    choice = random.choice(list(set(CHOICES.values())))
    return Play("computer", choice)

def decide_winner(play_player, play_computer) -> Play:
    """
    Given a pair of Plays returns Winner
    """
    game_result = get_result_message({play_player.choice, play_computer.choice})
    if play_player.choice == play_computer.choice:
        result = None
    if play_player.choice == "rock" and play_computer.choice in ("scissors", "lizard"):
        result = Winner(play_player, game_result)
    if play_player.choice == "scissors" and play_computer.choice in ("paper", "lizard"):
        result = Winner(play_player, game_result)
    if play_player.choice == "paper" and play_computer.choice in ("rock", "spock"):
        result = Winner(play_player, game_result)
    if play_player.choice == "spock" and play_computer.choice in ("scissors", "rock"):
        result = Winner(play_player, game_result)
    if play_player.choice == "lizard" and play_computer.choice in ("spock", "paper"):
        result = Winner(play_player, game_result)

    result = Winner(play_computer, game_result)
    return result

def display_winner(winner: Winner):
    """Display winner and winner action"""
    if winner:
        winner_username = winner.play.username.capitalize()
        prompt(f"{winner_username} won! {winner.action}")
    else:
        prompt("Drawn!")

    print("...")
    time.sleep(2)
    clear()

def display_scoreboard(tally, rounds):
    """Display scoreboard with total rounds"""
    horizontal_line = f"+-{'-'*26}-+"
    print(horizontal_line)
    print(f"|  Best of five ({rounds:02} rounds)  |")
    player_score = tally["player"]
    computer_score = tally["computer"]
    print(f"| Player ({player_score}) vs Computer ({computer_score}) |")
    print(horizontal_line)

def display_help():
    """Display help"""
    clear()
    prompt("""Scissors cuts paper. Paper covers rock. Rock crushes lizard.
Lizard poisons Spock. Spock smashes scissors. Scissors decapitates lizard.
Lizard eats paper. Paper disproves Spock. Spock vaporizes rock. 
Rock crushes scissors.""")

def get_result_message(choices):
    """Retrieve action performed by winning player"""

    result = None

    if choices == {"lizard", "spock"}:
        result = "Lizard poisons Spock."
    if choices == {"lizard", "paper"}:
        result = "Lizard eats Paper."
    if choices == {"spock", "scissors"}:
        result = "Spock smashes Scissors."
    if choices == {"spock", "rock"}:
        result = "Spock vaporizes Rock."
    if choices == {"paper", "rock"}:
        result = "Paper covers Rock."
    if choices == {"paper", "spock"}:
        result = "Paper disproves Spock."
    if choices == {"scissors", "lizard"}:
        result = "Scissors decapitates Lizard."
    if choices == {"scissors", "paper"}:
        result = "Scissors cuts Paper."
    if choices == {"rock", "scissors"}:
        result = "Rock crushes Scissors."
    if choices == {"rock", "lizard"}:
        result = "Rock crushes Lizard."

    return result

def prompt(message):
    """Format message for printing to user"""
    print(f"==> {message}")

def keep_going():
    """Continue playing?"""
    prompt("Play again? Yes/No")
    if input().strip().lower() in ["y", "yes"]:
        return True
    return False

def clear():
    """Clear terminal screen"""
    if os.name == "posix":
        _ = os.system("clear")  # mac/linux
    else:
        _ = os.system("cls")  # windows

if __name__ == "__main__":
    main()
