#!/usr/bin/env python3

# Rock, Paper, Scissor

import random
import time

ROCK = 1
PAPER = 2
SCISSORS = 3

# Rules
NAMES = {ROCK: "Rock", PAPER: "Paper", SCISSORS: "Scissors"}
RULES = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}

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
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print()
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Choose 1, 2 or 3.")


def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer threw {0}!".format(NAMES[computer]))
    if player == computer:
        print("Tie.")
    else:
        if RULES[player] == computer:
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
