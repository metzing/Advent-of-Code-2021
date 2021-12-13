from colorama import Fore

octupi = []

tableHeight = 0
tableWidth = 0

flashingOctupi = []

class Octopus:

    def __init__(self, x : int, y : int, lightLevel : int) -> None:
        self.__lightLevel = lightLevel
        self.__x = x
        self.__y = y
        self.__numberOfFlashes = 0

    @property
    def lightlevel(self):
        return self.__lightLevel    
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
    @property
    def numberOfFlashes(self):
        return self.__numberOfFlashes

    def increaseLightLevel(self):

        self.__lightLevel += 1

        if self.__lightLevel == 10:   
            flashingOctupi.append(self)

    @property
    def flashed(self):
        return self.__lightLevel == 0
     
    def resetFlashed(self):

        if self.__lightLevel > 9:
            self.__lightLevel = 0
            self.__numberOfFlashes += 1

for line in open("Day11.txt", "r").readlines():
    
    tableWidth = 0
    octupi.append([])

    for char in line.strip():
        octupi[tableHeight].append(Octopus(tableHeight, tableWidth, int(char)))
        tableWidth += 1
    
    tableHeight += 1

def isInTable(x : int, y : int) -> bool:
    return 0 <= x and x < tableHeight and 0 <= y and y < tableWidth

def printTable():
    for i in range(0, tableHeight):
        for j in range(0, tableWidth):

            octopus = octupi[i][j]

            if octopus.flashed:
                print(Fore.RED + str(octopus.lightlevel), end="")
            else:
                print(Fore.WHITE + str(octopus.lightlevel), end="")
        print("")
    print("")

cycles = 0

while True:

    cycles += 1

    for line in octupi:
        for octopus in line:
            octopus.increaseLightLevel()
    
    while any(flashingOctupi):
        current = flashingOctupi.pop()

        for i in [ -1, 0, 1 ]:
            for j in [ -1, 0, 1 ]:

                if isInTable(current.x + i, current.y + j) and not (i == 0 and j == 0):
                    octupi[current.x + i][current.y + j].increaseLightLevel()

    for line in octupi:
        for octopus in line:

            octopus.resetFlashed()

    printTable()

    numberOfFlashes = sum([len([a for a in l if a.flashed]) for l in octupi])

    if numberOfFlashes == tableWidth * tableHeight:
        break

print(cycles)
