import numpy as np

testData = np.array([
199,
200,
208,
210,
200,
207,
240,
269,
260,
263
])
data = np.genfromtxt('adventOfCode\\2021\\01data.txt')

print(np.sum(np.diff(data)>0))

def second(data):
    return np.sum((data[3:] - data[:-3]) > 0)