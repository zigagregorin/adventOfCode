import numpy as np

def validation(preamble, number):
	for i, n in enumerate(preamble):
		if number-n in preamble[i+1:]:
			return True

	return False


def canYouSum(arr, result):
	i = 0
	counter = 0
	while counter < result:
		counter += arr[i]
		i += 1
	if counter == result:
		return arr[:i]
	return None



if __name__ == '__main__':
	fileLines = np.genfromtxt('adventOfCode\\09data.txt', dtype=np.uint64)
	PRE_SIZE = 25
	result = 0
	N = fileLines.size
	for j in range(PRE_SIZE, N):
		if not validation(fileLines[j-PRE_SIZE:j], fileLines[j]):
			result = fileLines[j]

	print(result)
	# second part
	for j in range(N):
		a = canYouSum(fileLines[j:], result)
		if a is not None:
			print(a)
			break

	print('Result 2 =', a.min() + a.max())
