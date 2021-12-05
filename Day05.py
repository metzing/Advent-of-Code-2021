def between(start : int, end : int):
    if (start < end):
        return range(start, end + 1)
    elif (start > end):
        return range(start, end - 1, -1)
    else:
        return [start]

class Vent:

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    @property
    def x1(self) -> int:
        return self.__x1

    @property
    def x2(self) -> int:
        return self.__x2

    @property
    def y1(self) -> int:
        return self.__y1

    @property
    def y2(self) -> int:
        return self.__y2

    @property
    def isVertical(self) -> bool:
        return self.y1 == self.y2

    @property
    def isHorizontal(self) -> bool:
        return self.x1 == self.x2

    def parse(line : str):
        split = line.split(" -> ")
        start = split[0].split(",")
        end = split[1].split(",")

        return Vent(int(start[0]), int(start[1]), int(end[0]), int(end[1]))


class Map:

    def __init__(self) -> None:
        self.__fields = {}
        self.__dangerousFieldsCount = 0
    
    def addvent(self, vent : Vent):
        if vent.isHorizontal:
            for y in between(vent.y1, vent.y2):
                self.add(vent.x1, y)
        
        if vent.isVertical:
            for x in between(vent.x1, vent.x2):
                self.add(x, vent.y1)
    
    def add(self, x : int, y : int):
        if not x in self.__fields.keys():
            self.__fields[x] = {}
        
        if not y in self.__fields[x].keys():
            self.__fields[x][y] = 0

        self.__fields[x][y] += 1

        if self.__fields[x][y] == 2:
            self.__dangerousFieldsCount += 1
    
    @property
    def dangerousFieldsCount(self):
        return self.__dangerousFieldsCount

file = open("Day05.txt", "r")

map = Map()

for line in file.readlines():
    vent = Vent.parse(line)
    map.addvent(vent)

print(map.dangerousFieldsCount)