import numpy as np

def boardingPass(text):
    """

    :param text:
    :return:
    >>> boardingPass('BFFFBBFRRR')
    (70, 7, 567)
    >>> boardingPass('FFFBBBFRRR')
    (14, 7, 119)
    >>> boardingPass('BBFFBBFRLL')
    (102, 4, 820)
    """
    row = int(text[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(text[7:].replace('L', '0').replace('R', '1'), 2)
    seatID = row*8 + column

    return row, column, seatID


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    ids = []

    with open('adventOfCode\\05data.txt', 'r') as f:
        for line in f:
            ids.append(boardingPass(line.strip())[2])

    print(max(ids))
    ids.sort()
    d = np.diff(ids)
    ind = np.argwhere(d==2)[0,0]
    print(ids[ind]+1)