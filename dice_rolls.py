import math
import random


def d2_roll():
    roll_d2 = random.randint(1, 100)
    if roll_d2 % 2 != 0:
        return 1
    else:
        return 2


def d3_roll():
    roll_d3 = random.randint(1, 6)
    roll_d3 = math.ceil(roll_d3/2)
    return roll_d3


def d4_roll():
    roll_d4 = random.randint(1, 4)
    return roll_d4


def d6_roll():
    roll_d6 = random.randint(1, 6)
    return roll_d6


def d8_roll():
    roll_d8 = random.randint(1, 8)
    return roll_d8


def d10_roll():
    roll_d10 = random.randint(1, 10)
    return roll_d10


def d12_roll():
    roll_d12 = random.randint(1, 12)
    return roll_d12


def d20_roll():
    roll_d20 = random.randint(1, 20)
    return roll_d20


def d100_roll():
    roll_d100_tens = random.randint(0, 9)
    roll_d100_singles = random.randint(0, 10)
    roll_d100_tens = roll_d100_tens * 10
    roll_d100 = roll_d100_tens + roll_d100_singles
    if roll_d100 == 0:
        return 100
    else:
        return roll_d100
