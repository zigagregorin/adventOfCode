import numpy as np

data = np.genfromtxt('adventOfCode\\2021\\03data.txt', dtype=np.str)
numericData = np.array([int(i, 2) for i in data])
numWidth = len(data[0])


def outputBinary(dataArray):
    for element in dataArray:
        print(bin(element))

    print('\n')


def gamma(dataArray, arrayWidth):
    n = len(dataArray)
    result = 0
    for i in range(arrayWidth):
        if np.sum((dataArray & (1 << i)) >> i) > n/2:
            result += 1 << i
    return result


def epsilon(dataArray, arrayWidth):
    n = len(dataArray)
    result = 0
    for i in range(arrayWidth):
        if np.sum((dataArray & (1 << i)) >> i) < n/2:
            result += 1 << i
    return result


def oxygen(dataArray, arrayWidth):
    temporaryArray = dataArray.copy()
    for j in range(arrayWidth):
        i = arrayWidth - j - 1
        mask = (temporaryArray & (1 << i)) >> i
        # print(mask)
        if np.sum(mask) >= len(temporaryArray)/2:
            temporaryArray = temporaryArray[mask.astype(bool)]
        else:
            temporaryArray = temporaryArray[mask.astype(bool).__invert__()]

        # outputBinary(temporaryArray)

        if len(temporaryArray) == 1:
            break

    return temporaryArray[0]


def co2(dataArray, arrayWidth):
    temporaryArray = dataArray.copy()
    for j in range(arrayWidth):
        i = arrayWidth - j - 1
        mask = (temporaryArray & (1 << i)) >> i
        # print(mask)
        if np.sum(mask) < len(temporaryArray)/2:
            temporaryArray = temporaryArray[mask.astype(bool)]
        else:
            temporaryArray = temporaryArray[mask.astype(bool).__invert__()]

        # outputBinary(temporaryArray)

        if len(temporaryArray) == 1:
            break

    return temporaryArray[0]



# g = gamma(numericData, numWidth)
# e = epsilon(numericData, numWidth)

o = oxygen(numericData, numWidth)
c = co2(numericData, numWidth)

print(f'oxygen = {o}')
print(f'CO2 = {c}')
print(f'result = {o*c}')
