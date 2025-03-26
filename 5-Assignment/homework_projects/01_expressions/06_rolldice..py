"""Simulate rolling two dice, and prints results of each roll as well as the total."""



import random


sides: int = 6

def rolldice():
    while True:
  
            dice1 = random.randint(1, sides)
            dice2 = random.randint(1, sides)
            total : int = dice1 + dice2

            print(f"Dice have {sides} sides")
            print(f"Dice 1: {dice1}")
            print(f"Dice 2: {dice2}")
            print(f"Total of both dice: {total}")
            break

rolldice()