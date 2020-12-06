import re
VALIDATION = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def isPassport(line):
	pattern = r'(\w{3}):'
	identifiers = set(re.findall(pattern, line))

	return VALIDATION.issubset(identifiers)


def byr(line):
	"""

	:param line:
	:return:
	>>> byr('byr:2002')
	True
	>>> byr('byr:2003')
	False
	"""
	pattern = r'byr:(\d{4,})'
	value = int(re.findall(pattern, line)[0])

	if not value:
		return False
	if value < 1920:
		return False
	if value > 2002:
		return False
	return True


def iyr(line):
	pattern = r'iyr:(\d{4,})'
	value = int(re.findall(pattern, line)[0])

	if not value:
		return False
	if value < 2010:
		return False
	if value > 2020:
		return False
	return True

def eyr(line):
	pattern = r'eyr:(\d{4,})'
	value = int(re.findall(pattern, line)[0])

	if not value:
		return False
	if value < 2020:
		return False
	if value > 2030:
		return False
	return True

def hgt(line):
	"""

	:param line:
	:return:
	>>> hgt('hgt:58in')
	False
	>>> hgt('hgt:59in')
	True
	>>> hgt('hgt:193cm')
	True
	>>> hgt('hgt:194cm')
	False
	"""
	pattern = r'hgt:(\d+)(\w{2})'
	try:
		value = re.findall(pattern, line)[0]
	except IndexError:
		return False
	val, unit = value
	val = int(val)

	if unit == 'cm' and val >= 150 and val <= 193:
		return True
	if unit == 'in' and val >= 59 and val <= 76:
		return True

	return False

def hcl(line):
	pattern = r'hcl:#([0-9a-z]{6,})'
	try:
		value = re.findall(pattern, line)[0]
	except IndexError:
		return False

	if len(value) == 6:
		return True
	return False

def ecl(line):
	pattern = r'ecl:(\w{3})'
	try:
		value = re.findall(pattern, line)[0]
	except IndexError:
		return False

	if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return True
	return False

def pid(line):
	pattern = r'pid:(\d{9,})'
	try:
		value = re.findall(pattern, line)[0]
	except IndexError:
		return False

	if len(value) == 9:
		return True
	return False


def check2(line):
	if not byr(line):
		return False
	if not iyr(line):
		return False
	if not eyr(line):
		return False
	if not hgt(line):
		return False
	if not hcl(line):
		return False
	if not ecl(line):
		return False
	if not pid(line):
		return False
	return True




if __name__ == '__main__':
	import doctest
	doctest.testmod()

	counter = 0
	currentPassport = ''
	with open('adventOfCode\\04data.txt', 'r') as f:
		for line in f:
			currentPassport += line
			if line == '\n':
				# print('Passport\n', currentPassport)
				if isPassport(currentPassport):
					counter += check2(currentPassport)
				currentPassport = ''
	print(counter)