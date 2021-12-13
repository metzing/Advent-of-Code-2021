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
        
        return (candidate not in self.__caves or candidate.islarge) and \
            candidate.name in self.__caves[-1].connections

    def __str__(self) -> str:
        return f"[{', '.join(c.name for c in self.__caves)}]"

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

print(len([path for path in finished if any(cave for cave in path.caves if cave.issmall)]))