import numpy as np
# from matplotlib import pyplot as plt

data = np.genfromtxt('adventOfCode\\01data.txt', dtype=np.int)
data.sort()

# two numbers
for num in data:
	# need to sum up to 2020
	if 2020-num in data:
		print(num*(2020-num))
		break

N = data.size
for i in range(N):
	for j in range(i+1, N):
		if 2020-data[i]-data[j] in data:
			print((2020-data[i]-data[j])*data[i]*data[j])
			# break
