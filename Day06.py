file = open("Day06.txt", "r")

fish = list(map(int, file.readline().split(",")))

for i in range(0, 80):
    for index, days in enumerate(fish):
        if days == 0:
            fish.append(9)
            fish[index] = 6
        else:
            fish[index] = days - 1

print(len(fish))