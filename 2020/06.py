def uniqueAnswers(text):
    s = set()
    for letter in text:
        s.add(letter)
    s.remove('\n')

    return s


def sameAnswers(text):
    lines = text.splitlines()
    s = set(lines[0])
    for line in lines:
        s = s.intersection(set(line))

    return s



if __name__ == '__main__':
    import doctest

    doctest.testmod()

    counter = 0
    currentLine = ''
    with open('adventOfCode\\06data.txt', 'r') as f:
        for line in f:
            if line == '\n':
                counter += len(sameAnswers(currentLine))
                currentLine = ''
                continue
            currentLine += line
    print(counter)
