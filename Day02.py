def _parse(line : str):
    split = line.split(" ")

    return split[0], int(split[1])

file = open("Day02.txt", "r")

instructions = list(map(_parse, file.readlines()))

depth = 0
distance = 0
aim = 0

for direction, length in instructions:
    if direction == "forward":
        distance += length
        depth += length * aim
    elif direction == "up":
        aim -= length
    else:
        aim += length

print(depth * distance)