import numpy as np
import os.path as p


PATH = p.join('adventOfCode', '2022')
N = 12

test = True
# test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


# with open(p.join(PATH, filename), 'r') as file:
with open(p.join(filename), 'r') as file:
    lines = file.readlines()

table = np.array([[ord(c)-ord('a') for c in line.strip()] for line in lines])

startingIndex = np.argwhere(table == -14)[0]


def steps(dataTable, i, j, n=0, height=0):
    tempTable = dataTable.copy()

    # check if end is near and finish
    if height >= 24:
        try:
            if dataTable[i+1, j] == -28:
                print(n+1)
        except IndexError:
            pass
        try:
            if dataTable[i, j+1] == -28:
                print(n+1)
        except IndexError:
            pass
        if i > 0:
            if dataTable[i-1, j] == -28:
                print(n+1)
        if j > 0:
            if dataTable[i, j-1] == -28:
                print(n+1)

    # do the step
    try:
        if np.abs(dataTable[i+1, j] - height) <= 1:
            tempTable[i+1, j] = -100-n
            n += 1
            steps(tempTable, i+1, j, n, dataTable[i+1, j])
    except IndexError:
        pass
    try:
        if np.abs(dataTable[i, j+1] - height) <= 1:
            tempTable[i, j+1] = -100-n
            n += 1
            steps(tempTable, i, j+1, n, dataTable[i, j+1])
    except IndexError:
        pass
    if i > 0:
        tempTable[i-1, j] = -100 - n
        n += 1
        steps(tempTable, i-1, j, n, dataTable[i-1, j])
    if j > 0:
        tempTable[i, j-1] = -100 - n
        n += 1
        steps(tempTable, i, j-1, n, dataTable[i, j-1])


# test = table.flatten()
# test.sort()
# h = np.histogram(test, bins=26, range=(-0.5,25.5))
#
# from matplotlib import pyplot as plt
# plt.imshow(table)

steps(table, startingIndex[0], startingIndex[1], n=0, height=0)
