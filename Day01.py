def _parse(line : str):
    return int(line.strip())

file = open("Day01.txt", "r")

increases = 0

depths = list(map(_parse, file.readlines()))

for index in range(3, len(depths)):
    last = depths[index - 3]
    current = depths[index]

    if (last < current):
        increases = increases + 1

print(increases)
