import numpy as np


def checkBingo(boardSystem):
    lineSum = np.sum(boardSystem.reshape(-1, 5), 1)
    columnSum = np.sum(np.moveaxis(boardSystem, 1, 2).reshape(-1, 5), 1)

    completedLines = np.argwhere(lineSum == -5)
    completedColumns = np.argwhere(columnSum == -5)

    return np.concatenate((completedLines, completedColumns)).flatten()


if __name__ == '__main__':

    with open('adventOfCode\\2021\\04data.txt', 'r') as f:
        draw = np.fromstring(f.readline(), sep=',', dtype=int)
        _ = f.readline()

        boards = np.fromfile(f, sep=' ', dtype=int).reshape((-1, 5, 5))

    # for num in draw:
    #     # print('number =', num)
    #     boards[boards == num] = -1
    #     # print(boards)
    #     winner = checkBingo(boards)
    #     if winner.size > 0:
    #         if winner.size != 1:
    #             print('winner size is', winner.size)
    #         winningBoard = boards[winner[0]//5]
    #         sumUnmarked = np.sum(winningBoard[winningBoard > 0])
    #
    #         result = num*sumUnmarked
    #
    #         print('First winner', result)

    for num in draw:
        boards[boards == num] = -1

        winners = checkBingo(boards)
        if winners.size > 0:
            winningBoards = winners//5

            if boards.shape[0] == 1:
                winningBoard = boards[winningBoards[0]]
                sumUnmarked = np.sum(winningBoard[winningBoard > 0])
                result = num*sumUnmarked
                print('Last winner', result)

            boards = np.delete(boards, winningBoards, axis=0)
