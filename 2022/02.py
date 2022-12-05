import numpy as np
import os.path as p

PATH = p.join('adventOfCode', '2022')
N = 2


test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


def result(input1, input2):

    outcome = (ord(input2) - ord(input1)) % 3
    if outcome == 0:
        return 3
    elif outcome == 1:
        return 6
    return 0


with open(p.join(PATH, filename), 'r') as file:
    lines = file.readlines()
    # for line in file:
    #     print(line.strip())


"""
A - rock
B - paper
C - scissors

The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected
(1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round
(0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

options = {'A', 'B', 'C'}
optionScore = {
    'A': 1,
    'B': 2,
    'C': 3
}

# for x in ['A', 'B', 'C']:
#     for y in ['A', 'B', 'C']:
#         print(f'{x} | {y} = {(ord(y)-ord(x))%3}')

for x in options:
    for y in options - {x}:
        for z in options - {x, y}:
            # print(x, y, z)
            replacements = {
                'X': x,
                'Y': y,
                'Z': z
            }

            score = 0
            for line in lines:
                option1, fakeOption2 = line.strip().split(' ')
                option2 = replacements[fakeOption2]

                score += result(option1, option2) + optionScore[option2]

            print(x, y, z, score)

score = 0
for line in lines:
    option1, fakeOption2 = line.strip().split(' ')
    if fakeOption2 == 'X':
        option2 = chr((ord(option1) - 65 - 1) % 3 + 65)
    elif fakeOption2 == 'Y':
        option2 = option1
    elif fakeOption2 == 'Z':
        option2 = chr((ord(option1) - 65 + 1) % 3 + 65)
    else:
        print('error')

    score += result(option1, option2) + optionScore[option2]

print(score)
