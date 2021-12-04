import functools

class Field:

    def __init__(self, value) -> None:
        self.__value = value
        self.__isMarked = False

    @property
    def value(self):
        return self.__value
    
    @property
    def isMarked(self):
        return self.__isMarked

    def mark(self):
        self.__isMarked = True

    def __str__(self) -> str:
        return f'({self.__value} {self.__isMarked})'

    def __repr__(self) -> str:
        return f'({self.__value} {self.__isMarked})'

class Board:
        
    def __init__(self, numbers : list):
        self.__fields = list(map(lambda row: list(map(Field, row)), numbers))
        self.__announced = False

    @property
    def fields(self):
        return self.__fields

    def mark(self, number : int):
        for row in self.__fields:
            for field in row:
                if field.value == number:
                    field.mark()

    def isWinner(self):
        
        rowsWin = [True, True, True, True, True]
        columnsWin = [True, True, True, True, True]

        for i in range(0, 5):
            for j in range(0, 5):
                rowsWin[i] = rowsWin[i] and self.__fields[i][j].isMarked
                columnsWin[j] = columnsWin[j] and self.__fields[i][j].isMarked
        
        rowsWin.extend(columnsWin)

        return functools.reduce(lambda i, j: i or j, rowsWin, False)

    def sumUnmarkedNumbers(self):
        sum = 0

        for row in self.__fields:
            for field in row:
                if not field.isMarked:
                    sum += field.value

        return sum

    def print(self):
        for i in range(0, 5):
            print(f'[{self.__fields[i]}]')

    def announceWin(self, value : int):
        if not self.__announced:
            print(value)
            self.__announced = True


file = open("Day04.txt", "r")

draws = list(map(int, file.readline().split(",")))
file.readline()

boards = []
buildingRows = []

while (line := file.readline()):

    if line != "\n":
        numbers = list(map(str.strip, line.strip().replace("  "," ").split(" ")))
        buildingRows.append(list(map(int, numbers)))
    else:
        boards.append(Board(buildingRows))
        buildingRows = []

for drawn in draws:

    for board in boards:
        
        board.mark(drawn)

        if board.isWinner():
            unmarkedSum = board.sumUnmarkedNumbers()
            board.announceWin(unmarkedSum * drawn)

