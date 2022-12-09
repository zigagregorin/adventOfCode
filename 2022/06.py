import numpy as np
import os.path as p


PATH = p.join('adventOfCode', '2022')
N = 6

test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


crateFormation = [[] for i in range(10)]

with open(p.join(PATH, filename), 'r') as file:
    # lines = file.readlines()
    i = 14
    word = file.read(14)

    while True:
        character = file.read(1)
        if character == '\n':
            break
        if len(set(word)) == 14:
            print(i)
            break

        word += character
        word = word[1:]
        # print(i, character)
        i += 1
