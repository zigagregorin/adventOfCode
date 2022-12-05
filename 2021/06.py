import numpy as np

# input = np.array([3, 4, 3, 1, 2])
input = np.genfromtxt('adventOfCode\\2021\\06data.txt', dtype=int, delimiter=',')

def lanternfishCounter(array):
	return np.sum(array)

def timeStep(array):
	extendedArray = np.concatenate((array, [0]))
	extendedArray[7] += extendedArray[0]
	extendedArray[9] += extendedArray[0]
	return extendedArray[1:]


if __name__ == '__main__':
	timerCounter = np.zeros(9)

	# initial state
	for num in input:
		timerCounter[num] += 1

	numOfDays = 256
	for t in range(1, numOfDays + 1):
		timerCounter = timeStep(timerCounter)

	print('day', numOfDays, timerCounter)
	print('number of lanternfish: ', int(lanternfishCounter(timerCounter)))