import numpy as np
import re

def checkLine(text):
	"""

	:param text:
	:return:

	>>> checkLine('1-3 a: abcde')
	True
	>>> checkLine('1-3 b: cdefg')
	False
	"""

	m = re.match(r'(\d*)-(\d*)\s([a-z]):\s(\w+)', text)
	low, high, letter, password = m.group(1, 2, 3, 4)
	# print(low, high, letter, password)
	occurencies = len(re.findall(letter, password))
	# print(occurencies)

	return occurencies >= int(low) and occurencies <= int(high)

def checkLine2(text):
	"""

	:param text:
	:return:

	>>> checkLine2('1-3 a: abcde')
	True
	>>> checkLine2('1-3 b: cdefg')
	False
	"""

	m = re.match(r'(\d*)-(\d*)\s([a-z]):\s(\w+)', text)
	low, high, letter, password = m.group(1, 2, 3, 4)

	return (password[int(low)-1] == letter) != (password[int(high)-1] == letter)



if __name__ == '__main__':
	import doctest
	doctest.testmod()

	counter = 0
	with open('adventOfCode\\02data.txt', 'r') as f:
		for line in f:

			counter += checkLine2(line)


	print(counter)