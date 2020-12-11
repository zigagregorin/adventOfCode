import numpy as np
neighbouringIndex = [[a-1, b-1] for a in range(3) for b in range(3)]
neighbouringIndex.pop(4)

def occupied(mStart, nStart, dataSet):
	count = 0
	for m, n in neighbouringIndex:
		try:
			if mStart+m >= 0 and nStart+n >= 0:
				if dataSet[mStart+m, nStart+n] == '#':
					count += 1
		except IndexError:
			continue
	return count

def occupied2(mStart, nStart, dataSet):
	count = 0
	for m, n in neighbouringIndex:
		locM = mStart + m
		locN = nStart + n
		while True:
			if locM < 0 or locN < 0:
				break
			try:
				element = dataSet[locM, locN]
				if element == '#':
					count += 1
					break
				if element == 'L':
					break
				locM += m
				locN += n
			except IndexError:
				break
	return count

if __name__ == '__main__':
	with open('adventOfCode\\11data.txt', 'r') as f:
		lines = f.read().splitlines()

	data = np.char.array([[c for c in line] for line in lines])
	steps = 0
	while True:
		changes = 0
		temp = data.copy()

		for i in range(data.shape[0]):
			for j in range(data.shape[1]):
				element = data[i, j]
				if element == '.':
					continue
				occ = occupied2(i, j, data)
				if element == 'L' and occ == 0:
					temp[i, j] = '#'
					changes += 1
				elif element == '#' and occ >= 5:
					temp[i, j] = 'L'
					changes += 1

		if changes < 1:
			break

		steps += 1
		# print(f'step {steps}')
		# print(temp)
		data = temp.copy()

	print('steps =', steps)
	print('occupied seats =', np.sum(data=='#'))
	#
	# testlines = '.......#.\n' \
	#             '...#.....\n' \
	#             '.#.......\n' \
	#             '.........\n' \
	#             '..#L....#\n' \
	#             '....#....\n' \
	#             '.........\n' \
	#             '#........\n' \
	#             '...#.....'
	# data2 = np.char.array([[c for c in line] for line in testlines.splitlines()])
	# occupied2(4, 3, data2)