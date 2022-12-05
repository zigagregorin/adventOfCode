import numpy as np
from scipy.signal import find_peaks
from scipy.ndimage import minimum_filter, maximum_filter, label
from matplotlib import pyplot as plt

footprint = np.array([
	[0, 1, 0],
	[1, 1, 1],
	[0, 1, 0]
])


if __name__ == '__main__':
	data = np.genfromtxt('adventOfCode\\2021\\09data.txt', dtype=int, delimiter=1)
	# data = np.genfromtxt('adventOfCode\\2021\\09testData.txt', dtype=int, delimiter=1)

	data_min = minimum_filter(data, footprint=footprint)
	data_max = maximum_filter(data, footprint=footprint)
	minima = data == data_min
	diff = (data_max - data_min) > 0
	minima[diff == 0] = 0

	print(np.sum((data+1)[minima]))

	areas, n = label(data != 9)
	sizes = [np.sum(areas == i) for i in range(1, n+1)]
	sizes.sort()

	print(np.product(sizes[-3:]))

	#
	# plt.imshow(data)
	# plt.colorbar()
	#
	# for i in range(len(minima)):
	# 	for j in range(len(minima[0])):
	# 		if minima[i, j]:
	# 			plt.scatter(j, i, c='k')
	#
	# minimaLocations = np.argwhere(minima)
	#
	# for i, j in minimaLocations:
	# 	print(i, j)