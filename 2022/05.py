import numpy as np
import os.path as p
import re

pattern = re.compile(r'move (\d*) from (\d*) to (\d*)')

PATH = p.join('adventOfCode', '2022')
N = 5

test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


crateFormation = [[] for i in range(10)]

with open(p.join(PATH, filename), 'r') as file:
    # lines = file.readlines()
    initLines = ''
    for line in file:
        if line == '\n':
            break
        initLines += line

    for line in initLines.splitlines()[-2::-1]:
        # print(line)
        for i in range(1,10):
            try:
                element = line[4*i - 3]
                if element == ' ':
                    pass
                else:
                    crateFormation[i].append(line[4*i - 3])
            except IndexError:
                pass
    print(crateFormation)

    for line in file:
        num, start, final = pattern.findall(line)[0]
        num = int(num)
        start = int(start)
        final = int(final)

        # part 1
        # for n in range(num):
        #     element = crateFormation[start].pop()
        #     crateFormation[final].append(element)

        # part 2
        addon = []
        for n in range(num):
            addon.append(crateFormation[start].pop())

        crateFormation[final] += addon[::-1]

print(crateFormation)

print('result = ', end='')
for col in crateFormation[1:]:
    print(col[-1], end='')
print('\n')