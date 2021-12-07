file = open("Day07.txt", "r")

positions = sorted(list(map(int, file.readline().split(","))))

median = positions[int(len(positions) / 2)]

fuelSpent = 0

for position in positions:
    fuelSpent += abs(position - median)

print(fuelSpent)
