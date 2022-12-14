import numpy as np
import os.path as p


PATH = p.join('adventOfCode', '2022')
N = 9

test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


def moveTail(head, tail):
    # move tail
    delta = head - tail
    distance = np.abs(delta)
    sign = np.sign(delta)
    if distance[0] == 2:
        tail[0] += sign[0]
        tail[1] += sign[1]

    elif distance[1] == 2:
        tail[1] += sign[1]
        tail[0] += delta[0]

    if distance[0] > 2 or distance[1] > 2:
        print('distance', distance)

    return tail


# T = np.array([0, 0])
# H = np.array([0, 0])
size = 32 if test else 512
marks = np.zeros((size, size), dtype=bool)
marksPart1 = marks.copy()
knots = np.zeros((10, 2), dtype=np.int)
for k in range(10):
    if test:
        knots[k] = [11, 5]
    else:
        knots[k] = [100, 100]

with open(p.join(PATH, filename), 'r') as file:
    for line in file:
        direction, step = line.strip().split(' ')
        step = int(step)

        # move
        for i in range(step):
            # move head
            if direction == 'U':
                knots[0, 1] += 1
            elif direction == 'D':
                knots[0, 1] -= 1
            elif direction == 'L':
                knots[0, 0] -= 1
            elif direction == 'R':
                knots[0, 0] += 1
            else:
                print('error, direction = ', direction)

            # move tail
            for j in range(9):
                knots[j+1] = moveTail(knots[j].copy(), knots[j+1].copy())

            # mark it
            marks[knots[-1, 0], knots[-1, 1]] = True
            marksPart1[knots[1, 0], knots[1, 1]] = True
            # print(knots[-1])
            # print(T)

print('part 1 =', np.sum(marksPart1))
print('part 2 =', np.sum(marks))

from matplotlib import pyplot as plt
# plt.imshow(np.roll(np.roll(marks, 11, 0), 5, 1).T, origin='lower')
plt.imshow(marks.T, origin='lower')
