import numpy as np
import re

pattern = re.compile(r'(\d*),(\d*) -> (\d*),(\d*)')

def fill(array, *coordinates):
	x1, y1, x2, y2 = coordinates

	gradient = [x2 - x1, y2 - y1]
	scalingFactor = np.gcd(*gradient)

	unitGradient = (gradient/scalingFactor).astype(int)
	xShift = unitGradient[0]
	yShift = unitGradient[1]

	for i in range(scalingFactor + 1):
		array[y1, x1] += 1
		x1 += xShift
		y1 += yShift

	return array


def getCoordinates(line):
	coordinates = pattern.findall(line)[0]
	x1 = int(coordinates[0])
	y1 = int(coordinates[1])
	x2 = int(coordinates[2])
	y2 = int(coordinates[3])

	return x1, y1, x2, y2



if __name__ == '__main__':
	field = np.zeros((1000, 1000), dtype=int)

	with open('adventOfCode\\2021\\05data.txt', 'r') as f:
		while True:
			line = f.readline()
			if not line:
				break

			x1, y1, x2, y2 = getCoordinates(line)

			# if x1 == x2 or y1 == y2:
			field = fill(field, x1, y1, x2, y2)

	# print(field)
	print(np.sum(field > 1))