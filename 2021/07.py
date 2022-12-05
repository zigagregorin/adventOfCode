import numpy as np

data = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
data2 = np.genfromtxt('adventOfCode\\2021\\07data.txt', dtype=int, delimiter=',')


def fuelUsed(array, location):
	return np.sum(np.abs(array - location))

def fuelUsed2(array, location):
	diff = np.abs(array - location)
	return np.sum(diff*(diff+1)/2)

if __name__ == '__main__':
	from matplotlib import pyplot as plt

	out = [fuelUsed(data, i) for i in range(11)]
	out2 = [fuelUsed2(data, i) for i in range(11)]

	out3 = [fuelUsed2(data2, i) for i in range(462, 467)]


