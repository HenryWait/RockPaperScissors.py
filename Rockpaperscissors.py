#!/usr/bin/env python3

# Rock, Paper, Scissor

from enum import Enum
import random
import time


class Throw(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    def vs(self, throw):
        RULES = {self.Rock: self.Scissors,
                 self.Paper: self.Rock,
                 self.Scissors: self.Paper
                 }
        if self == throw:
            return 0  # Tie
        if RULES[self] == throw:
            return 1  # Player wins
        else:
            return -1  # Computer wins


# For keeping score
SCORE = {"player": 0,
         "computer": 0,
         }


def start():
    print ("Let's play a game of Rock, Paper, Scissors.")
    while game():
        pass
    scores()


def game():
    player = move()
    computer = Throw(random.randint(1, 3))
    play(player, computer)
    return play_again()


def move():
    while True:
        print()
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            return Throw(player)
        except ValueError:
            pass
        print("Choose 1, 2 or 3.")


def play(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer threw {0}!".format(computer.name))
    result = player.vs(computer)
    if result == 0:
        print("Tie.")
    elif result == 1:
        print("You win!")
        SCORE["player"] += 1
    else:
        print("Computer wins!")
        SCORE["computer"] += 1


def play_again():
        answer = input("Would you like to play again? y/n: ")
        if answer in ("y", "Y", "Yes", "yes"):
            return answer
        else:
            print("Thank you for palying.")


def scores():
    print("HIGH SCORES")
    print("Player: ", SCORE["player"])
    print("Computer: ", SCORE["computer"])


if __name__ == '__main__':
    start()
