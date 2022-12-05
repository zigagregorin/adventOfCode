import numpy as np
import os.path as p

PATH = p.join('adventOfCode', '2022')
N = 3


test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


def priorityNumber(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    elif c.isupper():
        return ord(c) - ord('A') + 27
    else:
        return 0


# with open(p.join(PATH, filename), 'r') as file:
#     # lines = file.readlines()
#     score = 0
#     for line in file:
#         rucksack = line.strip()
#         # print(rucksack)
#         length = len(rucksack)
#         comp1 = rucksack[:length//2]
#         comp2 = rucksack[length//2:]
#         commonItem = set(comp1).intersection(set(comp2)).pop()
#         score += priorityNumber(commonItem)
#
#     print(score)

with open(p.join(PATH, filename), 'r') as file:
    lines = np.array(file.read().splitlines(), dtype=set).reshape((-1, 3))

score = 0
for line in lines:
    score += priorityNumber(set.intersection(set(line[0]), set(line[1]), set(line[2])).pop())

print(score)