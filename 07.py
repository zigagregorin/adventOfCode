import re


class Bag:
    colorSplit = re.compile(r'(\d+) (\w+ \w+)')

    def __init__(self, color, dataDict):
        self.visited = set()
        self.color = color
        self.visited.add(color)
        self.data = dataDict
        self.numOfBags = 0
        self.accessible(self.color)

    def accessible(self, currentColor, multiplier=1):
        # if currentColor == 'shiny gold':
        #     return None

        for option in self.data[currentColor]:
            # get color name without number
            number, newColor = self.colorSplit.findall(option)[0]

            # if newColor in self.visited:
            #     print('duplicate')
            #     continue
            self.visited.add(newColor)
            self.numOfBags += multiplier*int(number)
            self.accessible(newColor, multiplier*int(number))


if __name__ == '__main__':

    with open('adventOfCode\\07data.txt', 'r') as f:
        lines = f.readlines()

    # fill dictionary
    data = dict()

    linePattern = re.compile(r'(\w+ \w+) bags contain (.+)')
    insidePattern = re.compile(r'(\d+ \w+ \w+) bag\w*')

    for line in lines:
        c, inside = linePattern.match(line).groups()
        inSplit = insidePattern.findall(inside)

        data[c] = inSplit

    # totCount = 0
    # for color in data:
    #     colorTree = Bag(color, data)
    #     # print(color)
    #     # print(colorTree.visited)
    #     if 'shiny gold' in colorTree.visited:
    #         totCount += 1
    #
    # print('First part:', totCount-1)

    ### second part
    b = Bag('shiny gold', data)
    print(b.numOfBags)
