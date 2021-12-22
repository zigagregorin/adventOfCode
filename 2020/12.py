import re
import numpy as np

pattern = re.compile(r'(\w)(\d*)')
orientations = ['N', 'E', 'S', 'W']
angles = {'N':0, 'E':90, 'S':180, 'W':270}

def rotation(x, y, phi_deg):
	radians = phi_deg * np.pi / 180
	matrix = np.array([[np.cos(radians), -np.sin(radians)],
	                   [np.sin(radians), np.cos(radians)]])
	newX, newY = matrix.dot([x, y])
	return round(newX), round(newY)

if __name__ == '__main__':
	with open('adventOfCode\\12data.txt', 'r') as f:
		lines = f.read().splitlines()

	# starting condition
	# x = 0  # cosine
	# y = 0  # sine
	# orientation = 90
	# direction = 90
	#
	# for line in lines:
	# 	order, num = pattern.findall(line)[0]
	# 	num = int(num)
	#
	# 	# rotations
	# 	if order == 'R':
	# 		orientation += num
	# 		continue
	# 	elif order == 'L':
	# 		orientation -= num
	# 		continue
	#
	# 	if order == 'F':
	# 		direction = orientation
	# 	elif order in orientations:
	# 		direction = angles[order]
	# 	else:
	# 		print('unhandled error', order, num)
	# 		continue
	#
	# 	# move
	# 	x += num*np.cos(direction/180*np.pi)
	# 	y += num*np.sin(direction/180*np.pi)
	#
	# print(x, y)
	# print(round(np.abs(x) + np.abs(y)))

	waypointX = 1
	waypointY = 10

	shipX = 0
	shipY = 0

	for line in lines:
		order, num = pattern.findall(line)[0]
		num = int(num)

		# rotations
		if order in 'RL':
			if order == 'L':
				# negative rotation
				num *= -1
			waypointX ,waypointY = rotation(waypointX, waypointY, num)

		elif order == 'F':
			shipX += num*waypointX
			shipY += num*waypointY

		elif order in orientations:
			waypointX += num*np.cos(angles[order]/180*np.pi)
			waypointY += num*np.sin(angles[order]/180*np.pi)

		else:
			print('unhandled error', order, num)
			continue

	print(shipX, shipY)
	print(round(np.abs(shipX) + np.abs(shipY)))

