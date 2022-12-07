import numpy as np
import os.path as p

PATH = p.join('adventOfCode', '2022')
N = 4

test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


def sections(elf):
    border1, border2 = elf.split('-')
    return {i for i in range(int(border1), int(border2) + 1)}

with open(p.join(PATH, filename), 'r') as file:
    # lines = file.readlines()
    score1 = 0
    score2 = 0
    for line in file:
        elf1, elf2 = line.strip().split(',')
        range1 = sections(elf1)
        range2 = sections(elf2)
        # print(range1, range2)
        if range1.issubset(range2) or range2.issubset(range1):
            # print('subsets')
            score1 += 1
        if len(range1.intersection(range2)) > 0:
            score2 += 1

print(score1)
print(score2)
