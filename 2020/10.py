import numpy as np

count = 0
def options(sortedTable):
	# recursion takes too ling

	element = sortedTable[0]
	# stop condition
	if sortedTable[1:].size == 0:
		return 1

	count = 0
	# check next 3 elements
	for i in range(1, 4):
		try:
			token = sortedTable[i]
			if token - element <= 3:
				count += options(sortedTable[i:])
		except IndexError:
			continue

	return count

def numOfOptions(sortedTable):
	# hope to be linear
	optionCounter = np.zeros_like(sortedTable, dtype=np.uint64)
	optionCounter[-1] = 1

	for i in range(sortedTable.size)[::-1]:
		element = sortedTable[i]
		# check next three elements
		for j in range(1, 4):
			try:
				token = sortedTable[i+j]
				if token - element <= 3:
					optionCounter[i] += optionCounter[i+j]
			except IndexError:
				continue

	return optionCounter[0]


if __name__ == '__main__':

	data = np.genfromtxt('adventOfCode\\10data.txt', dtype=np.int)
	data = np.append(data, [0])
	data = np.append(data, data.max()+3)
	data.sort()
	dif = np.diff(data)

	ones = np.sum(dif == 1)
	threes = np.sum(dif == 3)

	# print(ones*threes)

	# print(options(data))
	print(numOfOptions(data))