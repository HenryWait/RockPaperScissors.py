#!/usr/bin/env python3

# Rock, Paper, Scissor

from enum import Enum
import random
import time

DELAY = 1


class RPSBase(Enum):
    def __new__(cls, value):
        int_value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = int_value
        obj._beats_ = value
        return obj

    def vs(self, throw):
        if self == throw:
            return 0  # Tie
        if throw.name in self._beats_:
            return 1  # Player wins
        else:
            return -1  # Opponent wins

    @staticmethod
    def random():
        return Throw(random.randint(1, len(Throw)))

    @staticmethod
    def options():
        return '\n'.join(['{0} = {1}'.format(t.name, t.value) for t in Throw])


class ClassicRPS(RPSBase):
    # Value = { Values it beats }
    Rock = {'Scissors'}
    Paper = {'Rock'}
    Scissors = {'Paper'}


class FiveRPS(RPSBase):
    # Value = { Values it beats }
    Rock = {'Scissors', 'Lizard'}
    Paper = {'Rock', 'Spock'}
    Scissors = {'Paper', 'Lizard'}
    Spock = {'Scossors', 'Rock'}
    Lizard = {'Spock', 'Paper'}


Throw = ClassicRPS

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
    computer = Throw.random()
    play(player, computer)
    return play_again()


def move():
    # Loop until we get valid input
    while True:
        print()
        player = input(Throw.options() + "\n")
        try:
            player = int(player)
            # Will throw a ValueError if not a valid choice
            return Throw(player)
        except ValueError:
            pass
        print("Choose 1, 2 or 3.")


def play(player, computer):
    print("1...")
    time.sleep(DELAY)
    print("2...")
    time.sleep(DELAY)
    print("3...")
    time.sleep(0.5 * DELAY)

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
    if answer.lower() in ("y", "yes"):
        return answer
    else:
        print("Thank you for palying.")


def scores():
    print("HIGH SCORES")
    print("Player: ", SCORE["player"])
    print("Computer: ", SCORE["computer"])


if __name__ == '__main__':
    start()
