file = open("Day06.txt", "r")

fish = list(map(int, file.readline().split(",")))

fishbyday = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for f in fish:
    fishbyday[f] += 1

for days in range(0, 256):
    
    spawning = fishbyday[0]

    for i in range(1, 9):
        fishbyday[i - 1] = fishbyday[i]

    fishbyday[6] += spawning

    fishbyday[8] = spawning

sum = 0

for f in fishbyday:
    sum += f

print(sum)