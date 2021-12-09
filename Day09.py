tableHeight = 0
tableWidth = 0

heights = []

for line in open("Day09.txt", "r").readlines():
    
    tableWidth = 0
    heights.append([])

    for char in line.strip():
        tableWidth += 1
        heights[tableHeight].append(int(char))
    
    tableHeight += 1


def isLowest(x, y):
    value = heights[x][y] 

    return (x - 1 == -1 or heights[x - 1][y] > value) and (y - 1 == -1 or heights[x][y - 1] > value) and \
        (x + 1 == tableHeight or heights[x + 1][y] > value) and (y + 1 == tableWidth or heights[x][y + 1] > value)

sum = 0

print(heights)

for i in range(0, tableHeight):
    for j in range(0, tableWidth):

        if isLowest(i, j):
            sum += (heights[i][j] + 1)

print(sum)