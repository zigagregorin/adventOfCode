import numpy as np
import os.path as p

PATH = p.join('adventOfCode', '2022')

testData = np.array([])

test = False

if test:
    filename = '01testData.txt'
else:
    filename = '01data.txt'

data = []
calories = []
with open(p.join(PATH, filename), 'r') as file:
    text = []
    for line in file:
        if line == '\n':
            # print('separate')
            data.append(text)
            calories.append(np.sum(text))

            text = []
        else:
            text.append(int(line.strip()))
        # print(line.strip())

print(f'Elf num {np.argmax(calories)+1} is carrying {np.max(calories)} cals')

calories.sort()
np.sum(calories[-3:])