tableHeight = 0
tableWidth = 0

squares = []
squareUpdates = {}

def addUpdate(x, y, reach):

    if (x, y) not in squareUpdates.keys() or squareUpdates[(x, y)] > reach:
        squareUpdates[(x, y)] = reach

def dequeueUpdate():
    xy = next(iter(sorted((xy for xy in squareUpdates.keys()), key=lambda xy: xy[0] + xy[1])))

    return xy[0], xy[1], squareUpdates.pop(xy)

class Square:

    def __init__(self, x, y, level) -> None:
        self.__x = x
        self.__y = y
        self.__level = level
        self.__reach = -1
        pass

    def tryUpdateReach(self, reachBefore):

        if self.__reach == -1 or self.__reach > reachBefore + self.__level:
            self.__reach = reachBefore + self.__level
            addUpdate(self.__x, self.__y, self.__reach)

    @property
    def reach(self):
        return self.__reach

    @property
    def level(self):
        return self.__level

for line in open("Day15.txt", "r").readlines():
    
    tableWidth = 0
    squares.append([])

    for char in line.strip():
        squares[tableHeight].append(Square(tableHeight, tableWidth, int(char)))
        tableWidth += 1
    
    tableHeight += 1

originalTableHeight = tableHeight
originalTableWidth = tableWidth

for i in range(0, 5):
    for j in range(0, 5):
        if i == 0 and j == 0:
            continue

        if j == 0:
            for _ in range(originalTableHeight):
                squares.append([])

        def mapValue(x, y):
            value = squares[x][y].level + i + j

            while value > 9:
                value -= 9

            return value 

        for k in range(originalTableHeight):
            for l in range(originalTableWidth):
                squares[i * originalTableHeight + k].append(Square(i * originalTableHeight + k, j * originalTableWidth + l, mapValue(k, l)))

tableHeight = tableHeight * 5
tableWidth = tableWidth * 5

def isInTable(x : int, y : int) -> bool:
    return 0 <= x and x < tableHeight and 0 <= y and y < tableWidth


squares[1][0].tryUpdateReach(0)
squares[0][1].tryUpdateReach(0)

while any(squareUpdates):
    x, y, reach = dequeueUpdate()

    print(f"{x}, {y}, {reach}")

    if isInTable(x - 1, y):
        squares[x - 1][y].tryUpdateReach(reach)

    if isInTable(x, y - 1):
        squares[x][y - 1].tryUpdateReach(reach)

    if isInTable(x + 1, y):
        squares[x + 1][y].tryUpdateReach(reach)

    if isInTable(x, y + 1):
        squares[x][y + 1].tryUpdateReach(reach)

print(squares[tableHeight - 1][tableWidth - 1].reach)
