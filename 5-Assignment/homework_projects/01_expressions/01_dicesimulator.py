"""Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

"""

import random


sides = 6


def roll_dice():
    dice1 = random.randint(1, sides)
    dice2 = random.randint(1, sides)
    total = dice1 + dice2
    print(f'Rolling two dice... {dice1} and {dice2} = {total}')


def main():
    dice1 = 100
    print(f"Startung value of dice1 : {dice1}")

    roll_dice()
    roll_dice()
    roll_dice()

    print(f"Final value of dice1 : {dice1}")

main()

