import numpy as np
import os.path as p


PATH = p.join('adventOfCode', '2022')
N = 10

test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'

x = 1
previous = 1
cycle = 1
count = 0
table = np.empty((0, 2), dtype=int)
# with open(p.join(PATH, filename), 'r') as file:
#     for border in range(20, 230, 40):
#         for line in file:
#             orders = line.strip().split(' ')
#
#             if orders[0] == 'noop':
#                 table = np.append(table, [[cycle, x]], axis=0)
#                 cycle += 1
#                 previous, x = x, x
#             elif orders[0] == 'addx':
#                 table = np.append(table, [[cycle, x]], axis=0)
#                 table = np.append(table, [[cycle+1, x]], axis=0)
#                 cycle += 2
#                 previous, x = x, x + int(orders[1])
#             # print(f'order {orders}, cycle {cycle},x = {x}, previous = {previous}')
#
#             if cycle > border:
#                 break
#
#         strength = previous * border
#         count += strength
#         print(f'\tcycle {border}, register x = {previous}, signal strength = {strength}')
# print(f'sum of signal strengths = {count}')

with open(p.join(PATH, filename), 'r') as file:
    for line in file:
        orders = line.strip().split(' ')

        if orders[0] == 'noop':
            table = np.append(table, [[cycle, x]], axis=0)
            cycle += 1
            previous, x = x, x
        elif orders[0] == 'addx':
            table = np.append(table, [[cycle, x]], axis=0)
            table = np.append(table, [[cycle+1, x]], axis=0)
            cycle += 2
            previous, x = x, x + int(orders[1])
        # print(f'order {orders}, cycle {cycle},x = {x}, previous = {previous}')
print(f'sum of signal strengths = {np.sum(table[19::40, 0]*table[19::40, 1])}')

# screen = np.zeros((6, 40), dtype=bool)
screen = np.zeros((240), dtype=bool)

for c, sprite in table:
    if np.abs((c-1)%40 - sprite) <= 1:
        screen[c-1] = True

from matplotlib import pyplot as plt
plt.imshow(screen.reshape((6, -1)))