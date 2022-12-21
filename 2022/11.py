import numpy as np
import os.path as p
import re

pattern = re.compile('Monkey (\d+):\n' +
                     '  Starting items: ([0-9,\s]+)\n' +
                     '  Operation: new = old (.) (\d+|old)\n' +
                     '  Test: divisible by (\d+)\n' +
                     '    If true: throw to monkey (\d+)\n' +
                     '    If false: throw to monkey (\d+)\n')


PATH = p.join('adventOfCode', '2022')
N = 11

test = True

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


with open(p.join(PATH, filename), 'r') as file:
    lines = file.readlines()

commands = pattern.findall(''.join(lines))
length = len(commands)

monkeys = []
for line in commands:
    monkeys.append(list(map(int, line[1].split(', '))))


def throw(monkeyCommands, worry):
    operation = monkeyCommands[2]
    operation = int.__add__ if operation == '+' else int.__mul__

    value = monkeyCommands[3]
    if value == 'old':
        value = worry
    else:
        value = int(value)

    worry = operation(worry, value)
    # worry //= 3

    if worry % int(monkeyCommands[4]) == 0:
        throwTo = int(monkeyCommands[5])
    else:
        throwTo = int(monkeyCommands[6])

    return throwTo, worry


monkeyCounter = np.zeros(length, dtype=int)
# round
for n in range(10000):
    if n % 500 == 0:
        print(n)
    for i in range(length):
        while monkeys[i]:
            item = monkeys[i][0]
            monkeyNumber, worryLevel = throw(commands[i], item)
            monkeys[i].remove(item)
            monkeys[monkeyNumber].append(worryLevel)
            monkeyCounter[i] += 1
            # print(monkeyNumber, worryLevel)

    # print(monkeys)

print(monkeyCounter)
print('part 1 ', np.product(np.sort(monkeyCounter)[-2:]))
np.sign()