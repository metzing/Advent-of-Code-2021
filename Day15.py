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

for line in open("Day15.txt", "r").readlines():
    
    tableWidth = 0
    squares.append([])

    for char in line.strip():
        squares[tableHeight].append(Square(tableHeight, tableWidth, int(char)))
        tableWidth += 1
    
    tableHeight += 1

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
