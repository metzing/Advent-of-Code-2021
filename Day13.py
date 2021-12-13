class Paper:
    
    def __init__(self):
        self.__points = set()

    def mark(self, xy):
        self.__points.add(xy)

    def fold(self, dir : str, coord : int):

        def transform(x, y):
            if dir == "y":
                if y <= coord :
                    return x, y
                else:
                    return x, coord - (y - coord)
            else:
                if x <= coord :
                    return x, y
                else:
                    return coord - (x - coord), y
            
        copy = Paper()

        for x, y in self.__points:
            copy.mark(transform(x, y))

        return copy

    @property
    def width(self):
        return max(point[0] for point in self.__points) + 1

    @property
    def height(self):
        return max(point[1] for point in self.__points) + 1

    def print(self):

        for j in range(self.height):
            for i in range(self.width): 

                if (i, j) in self.__points:
                    print("#", end="")
                else:
                    print(".", end="")
            
            print()
        print()

    @property
    def numberOfPoints(self) -> int:
        return len(self.__points)
        
file = open("Day13.txt", "r")

paper = Paper()

while (line := file.readline().strip()) != "":

    coords = [int(s) for s in line.split(",")]

    paper.mark((coords[0], coords[1]))

folds = []

while line := file.readline().strip():
    line = line.replace("fold along ", "")
    fold = line.split("=")
    folds.append((fold[0], int(fold[1])))

paper.print()

paper = paper.fold(folds[0][0], folds[0][1])

paper.print()

print(paper.numberOfPoints)