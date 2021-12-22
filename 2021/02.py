import numpy as np
import re

pattern = re.compile(r'(\w*) (\d*)')

if __name__ == '__main__':
    with open('adventOfCode\\2021\\02data.txt', 'r') as f:
        lines = f.read().splitlines()

    horizontal = 0
    depth = 0

    for line in lines:
        order, num = pattern.findall(line)[0]

        if order == 'forward':
            horizontal += int(num)
        elif order == 'down':
            depth += int(num)
        elif order == 'up':
            depth -= int(num)
        else:
            print('error, values: ', order, num)

    print(horizontal*depth)


    # second part
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        order, num = pattern.findall(line)[0]

        if order == 'forward':
            horizontal += int(num)
            depth += aim * int(num)
        elif order == 'down':
            aim += int(num)
        elif order == 'up':
            aim -= int(num)
        else:
            print('error, values: ', order, num)

    print(horizontal * depth)