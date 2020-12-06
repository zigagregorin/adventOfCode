VALUE = {'.': 0, '#':1}


def treeCounter(data, rightSkip, downSkip):
	i = 0  # starting point
	counter = 0
	lineLength = len(data[0])
	fullLength = len(data)

	for lineNum in range(0, fullLength, downSkip):
		counter += VALUE[data[lineNum][i%lineLength]]
		i += rightSkip

	return counter


if __name__ == '__main__':

	with open('adventOfCode\\03data.txt', 'r') as f:
		lines = f.read().splitlines()

	arr = [[1, 1],
	       [3, 1],
	       [5, 1],
	       [7, 1],
	       [1, 2]]

	product = 1
	for right, down in arr:

		val = treeCounter(lines, right, down)
		print(f'right={right} down={down} numTrees={val}')
		product *= val

	print('solution =', product)