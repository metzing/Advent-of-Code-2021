from colorama import Fore

heights = []

tableHeight = 0
tableWidth = 0

for line in open("Day09.txt", "r").readlines():
    
    tableWidth = 0
    heights.append([])

    for char in line.strip():
        tableWidth += 1
        heights[tableHeight].append(int(char))
    
    tableHeight += 1

def isInTable(x : int, y : int) -> bool:
    return 0 <= x and x < tableHeight and 0 <= y and y < tableWidth

class Basin:
    def __init__(self, x, y, height):
        self.__height = height
        self.__includedpoints = set([(x, y)])

    def expand(self, expandingHeight : int):

        for x, y in list(self.__includedpoints):
            self._extend(x + 1, y, self.__height, expandingHeight)
            self._extend(x - 1, y, self.__height, expandingHeight)
            self._extend(x, y + 1, self.__height, expandingHeight)
            self._extend(x, y - 1, self.__height, expandingHeight)

    def _extend(self, x : int, y : int, fromHeight : int, expandingHeight: int):

        if not isInTable(x, y):
            return

        height = heights[x][y]
        
        if (x, y) not in self.__includedpoints and height == expandingHeight and height >= fromHeight:

            self.__includedpoints.add((x, y))

            self._extend(x + 1, y, height, expandingHeight)
            self._extend(x - 1, y, height, expandingHeight)
            self._extend(x, y + 1, height, expandingHeight)
            self._extend(x, y - 1, height, expandingHeight)

    @property
    def numberOfPoints(self):
        return len(self.__includedpoints)

    def __contains__(self, tuple):
        return tuple in self.__includedpoints

basins = []

def printTable():
    for i in range(0, tableHeight):
        for j in range(0, tableWidth):
            if any((i ,j) in basin for basin in basins):
                print(Fore.LIGHTGREEN_EX + str(heights[i][j]), end="")
            else:
                print(Fore.RED + str(heights[i][j]), end="")
        print("")

def isLowest(x, y):
    value = heights[x][y] 

    return (x - 1 == -1 or heights[x - 1][y] > value) and (y - 1 == -1 or heights[x][y - 1] > value) and \
        (x + 1 == tableHeight or heights[x + 1][y] > value) and (y + 1 == tableWidth or heights[x][y + 1] > value)

for i in range(0, tableHeight):
    for j in range(0, tableWidth):

        if isLowest(i, j):
            basins.append(Basin(i, j, heights[i][j]))

for level in range(0, 9):

    print(level)

    for basin in basins:
        basin.expand(level)
    
    printTable()

basinsBySize = list(reversed(sorted([basin.numberOfPoints for basin in basins])))
print(basinsBySize[0] * basinsBySize[1] * basinsBySize[2])

