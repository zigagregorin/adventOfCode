import numpy as np
import re


def mask(text):
    if len(text) != 36:
        raise AttributeError('String length not correct!')
    zeros = (1 << 36) - 1  # base
    ones = 0
    for i, ch in enumerate(text[::-1]):
        if ch == '1':
            ones += 1 << i
        elif ch == '0':
            zeros -= 1 << i

    return zeros, ones


if __name__ == '__main__':
    memIndex = re.compile(r'mem\[(\d+)')
    with open('adventOfCode\\14data.txt', 'r') as f:
        lines = f.read().splitlines()

    maskZeros = (1 << 36) - 1
    maskOnes = 0
    mem = np.zeros(65361, dtype=np.uint64)

    jTable = []
    for line in lines:
        order, value = line.split(' = ')
        # print(order, value)

        if order == 'mask':
            maskZeros, maskOnes = mask(value)
        else:
            j = int(memIndex.findall(order)[0])
            jTable.append(j)
            num = int(value)
            # apply mask
            num = num | maskOnes
            num = num & maskZeros

            mem[j] = num

    print(np.sum(mem))
