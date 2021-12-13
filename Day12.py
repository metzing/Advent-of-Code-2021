from os import truncate


caves = {}

class Cave:

    def __init__(self, name) -> None:
        self.__name = name
        self.__connections = []

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def islarge(self) -> bool:
        return str.isupper(self.__name)

    @property
    def issmall(self) -> bool:
        return self.__name not in [ "start", "end" ] and str.islower(self.__name)

    @property
    def connections(self) -> list:
        return self.__connections
    
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

class Path:

    def __init__(self, copy = None, next = None) -> None:

        if copy is None:
            self.__caves = [ caves["start"] ]
        else:
            self.__caves = list(copy.caves)
            self.__caves.append(next)

    @property
    def caves(self) -> list:
        return self.__caves

    def continueable(self, candidate : Cave) -> bool:
        
        if candidate.name not in self.__caves[-1].connections or candidate.name == "start":
            return False

        if candidate.name == "end" or candidate.islarge:
            return True
        
        smallCavesVisited = [cave.name for cave in self.__caves if cave.issmall]
        hasSmallDuplicate = len(smallCavesVisited) != len(set(smallCavesVisited))

        return candidate.name not in smallCavesVisited or not hasSmallDuplicate

    def __str__(self) -> str:
        return f"[{', '.join(c.name for c in self.__caves)}]"

    def __repr__(self) -> str:
        return self.__str__()

for line in open("Day12.txt", "r").readlines():

    read = [Cave(name) for name in line.strip().split("-")]
    
    for cave in read:
        if cave.name not in caves.keys():
            caves[cave.name] = cave
        
    caves[read[0].name].connections.append(read[1].name)
    caves[read[1].name].connections.append(read[0].name)

paths = [ Path() ]

finished = []

while True:

    buildingPaths = []

    for path in paths:

        continueables = [cave for cave in caves.values() if path.continueable(cave)]

        for continuable in continueables:
            
            continued = Path(path, continuable)

            if continuable.name == "end":
                finished.append(continued)
            else:
                buildingPaths.append(continued)
    
    paths = buildingPaths

    if not any(paths):
        break

    print("building")
    for path in paths:
        print(path)

    print("finished")
    for path in finished:
        print(path)
    
    print()

print(len(finished))