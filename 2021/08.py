

def findConnections(numID):
	listNums = [set(num) for num in numID.split(' ')]

	numbers = {
		0:set(),
		1:set(),
		2:set(),
		3:set(),
		4:set(),
		5:set(),
		6:set(),
		7:set(),
		8:set(),
		9:set()
	}

	# get unique length items
	for item in listNums:
		length = len(item)

		if length == 2:
			numbers[1] = item
		elif length == 3:
			numbers[7] = item
		elif length == 4:
			numbers[4] = item
		elif length == 7:
			numbers[8] = item

	for item in listNums:
		length = len(item)

		if length == 5:
			if len(item.intersection(numbers[1])) == 2:
				numbers[3] = item
			elif len(item.intersection(numbers[4] - numbers[1])) == 2:
				numbers[5] = item
			else:
				numbers[2] = item

		elif length == 6:
			if len(item.intersection(numbers[1])) == 1:
				numbers[6] = item
			elif len(item.intersection(numbers[4])) == 4:
				numbers[9] = item
			else:
				numbers[0] = item

	return numbers


def getNumber(dictConnections, text):

	return list(dictConnections.keys())[list(dictConnections.values()).index(set(text))]


if __name__ == '__main__':

	counter = 0

	# with open('adventOfCode\\2021\\08testData.txt', 'r') as f:
	with open('adventOfCode\\2021\\08data.txt', 'r') as f:
		while True:
			line = f.readline().strip()
			if not line:
				break

			numberIdentification, output = line.split(' | ')

			# digits = output.split(' ')
			# for d in digits:
			# 	if len(d) in [2, 3, 4, 7]:
			# 		counter += 1

			connections = findConnections(numberIdentification)

			screenNumber = [str(getNumber(connections, digit)) for digit in output.split(' ')]

			counter += int(''.join(screenNumber))
			# print(screenNumber)


	print(counter)
