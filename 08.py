def checkCode(lines):
    i = 0
    acc = 0
    orderOfExecution = []
    while True:
        if i in orderOfExecution:
            break
        orderOfExecution.append(i)
        order = lines[i]
        word, num = order.split(' ')
        num = int(num)
        if word == 'nop':
            i += 1
        elif word == 'acc':
            acc += num
            i += 1
        elif word == 'jmp':
            i += num
        elif word == 'end':
            return acc
    return None


if __name__ == '__main__':
    with open('adventOfCode\\08data.txt', 'r') as f:
        fileLines = f.read().splitlines()

    for j in range(len(fileLines)):
        if fileLines[j].split(' ')[0] == 'nop':
            tempFile = fileLines.copy()
            tempFile[j] = tempFile[j].replace('nop', 'jmp')
        elif fileLines[j].split(' ')[0] == 'jmp':
            tempFile = fileLines.copy()
            tempFile[j] = tempFile[j].replace('jmp', 'nop')
        else:
            continue
        a = checkCode(tempFile)
        if a:
            print(j, a)
