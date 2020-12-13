import numpy as np

# def firstPart():
# 	with open('adventOfCode\\13data.txt', 'r') as f:
# 		time = int(f.readline().strip())
# 		busses = f.readline().strip().split(',')
#
# 	busses.sort()
# 	ind = busses.index('x')
#
# 	busNumbers = np.array(busses[:ind], dtype=np.int)
#
# 	firstBusNumber = np.ceil(time/busNumbers)
# 	delay = busNumbers*firstBusNumber - time
#
# 	fastestBusIndex = np.argmin(delay)
#
# 	return delay[fastestBusIndex]*busNumbers[fastestBusIndex]

if __name__ == '__main__':
	import time

	with open('C:\\Dropbox\\Programiranje\\adventOfCode\\13data.txt', 'r') as f:
		_ = int(f.readline().strip())
		busses = f.readline().strip().split(',')

	# # version 1
	# step = int(busses[0])
	# currentTime = step
	#
	# t1 = time.time()
	# while True:
	# 	for i, bus in enumerate(busses):
	# 		if bus == 'x':
	# 			continue
	# 		if (currentTime + i) % int(bus) != 0:
	# 			break
	# 	else:
	# 		print(currentTime)
	# 		break
	#
	# 	currentTime += step
	# t2 = time.time()
	# print('Evaluation time for v1: ', 1000*(t2 - t1), 'ms')

	# version 2
	busNumber = []
	shift = []
	for i, b in enumerate(busses):
		if b == 'x':
			continue

		shift.append(i)
		busNumber.append(int(b))

	indMax = int(np.argmax(busNumber))
	busMax = busNumber[indMax]

	# starting time
	# start higher
	# currentTime = busMax - shift[indMax]
	currentTime = (100000000000000//busMax)*busMax - shift[indMax]

	t3 = time.time()
	while True:
		for i, bus in enumerate(busNumber):
			if (currentTime + shift[i]) % bus != 0:
				break
		else:
			print(currentTime)
			break
		currentTime += busMax
	t4 = time.time()
	print('Evaluation time for v2: ', 1000*(t4 - t3), 'ms')
