file = open("Day07.txt", "r")

positions = sorted(list(map(int, file.readline().split(","))))

mean = round(sum(positions) / len(positions))

for i in range(mean - 1, mean + 2):
    fuelSpent = 0
    for position in positions:
        fuelSpent += sum(range(abs(position - i + 1) + 1))
    print(fuelSpent)
