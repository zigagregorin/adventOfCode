import numpy as np
import os.path as p


PATH = p.join('adventOfCode', '2022')
N = 7

test = False

if test:
    filename = f'{N:02d}testData.txt'
else:
    filename = f'{N:02d}data.txt'


class Folder:
    folderSizes = []

    def __init__(self, name, size=0):
        self.name = name
        self.subfolders = dict()
        self.selfSize = size

    def size(self):
        count = 0
        for sub in self.subfolders.values():
            count += sub.size()

        return count + self.selfSize

    def open(self, name):
        return self.subfolders[name]

    def add(self, name, size=0):
        self.subfolders[name] = Folder(name, size)

    def printout(self, tabs=0, onlyDirs=False):
        if onlyDirs:
            if self.isFolder():
                print(tabs*'  ' + f'- {self.name} size={self.selfSize}, includedSize={self.size()}')
        else:
            print(tabs * '  ' + f'- {self.name} size={self.selfSize}, includedSize={self.size()}')
        for sub in self.subfolders.values():
            sub.printout(tabs=tabs + 1, onlyDirs=onlyDirs)

    def FolderSizesFill(self):
        if self.isFolder():
            Folder.folderSizes.append(self.size())
        for sub in self.subfolders.values():
            sub.FolderSizesFill()

    def sizesBelow(self, threshold):
        count = 0
        for sub in self.subfolders.values():
            count += sub.sizesBelow(threshold)
        if self.isFolder():
            s = self.size()
            if s <= threshold:
                count += s

        return count

    def isFolder(self):
        return self.selfSize == 0

    def freeUpSpace(self, value):
        for sub in self.subfolders.values():
            pass



def readout(f, currentFolder:Folder):
    for line in f:
        line = line.strip()
        if line.startswith('$'):
            # change the main order
            order = line[2:]

            if order.startswith('ls'):
                continue

        if order.startswith('ls'):
            size, name = line.split(' ')
            if size == 'dir':
                size = 0
            else:
                size = int(size)

            currentFolder.add(name, size)

        elif order.startswith('cd'):
            _, name = order.split(' ')
            if name == '..':
                return
            elif name == '/':
                pass
            else:
                readout(f, currentFolder.open(name))


with open(p.join(PATH, filename), 'r') as file:
    # lines = file.readlines()
    structure = Folder('/')
    fileSystem = readout(file, structure)

# structure.printout(onlyDirs=True)
sizeLimit = 100000
print('part 1 ',structure.sizesBelow(sizeLimit))

totalSpace = 70000000
neededSpace = 30000000
allocatedSpace = structure.size()
freeSpace = totalSpace - allocatedSpace
needToFree = neededSpace - freeSpace

structure.FolderSizesFill()
a = np.array(Folder.folderSizes)
a [a < needToFree] = totalSpace
print('part 2 ', np.min(a))