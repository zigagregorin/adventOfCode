import numpy as np
import os.path as p


PATH = p.join('adventOfCode', '2022')
N = 8

test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


def isVisible(location, array):
    row, col = location
    element = array[row, col]
    try:
        if np.max(array[row, col+1:]) < element:
            return True
        if np.max(array[row, :col]) < element:
            return True
        if np.max(array[row+1:, col]) < element:
            return True
        if np.max(array[:row, col]) < element:
            return True
    except ValueError:
        return True
    return False


def viewingDistance(location, array):
    row, col = location
    element = array[row, col]
    product = 1

    product *= visionLength(element, array[row, col+1:])
    product *= visionLength(element, array[row, col-1::-1])
    product *= visionLength(element, array[row+1:, col])
    product *= visionLength(element, array[row-1::-1, col])

    return product


def visionLength(element, array):
    count = 0
    for tree in array:
        if tree < element:
            count += 1
        else:
            return count+1
    return count


with open(p.join(PATH, filename), 'r') as file:
    lines = file.readlines()

data = np.array([list(elem.strip()) for elem in lines], dtype=int)

# part 1
# vision = [[isVisible([i, j], data) for j in range(data.shape[0])] for i in range(data.shape[1])]
# print('result for part 1 ', np.sum(vision))

# part 2
views = np.array([[viewingDistance([i, j], data) for j in range(data.shape[0])] for i in range(data.shape[1])])
for k in range(data.shape[0]):
    views[0, k] = 0
    views[k, 0] = 0
print('result for part 2 ', np.max(views))
