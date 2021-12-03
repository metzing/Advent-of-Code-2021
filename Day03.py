file = open("Day03.txt", "r")

lines = file.readlines()

length = len(lines[0])

gamma = ""
epsilon = ""

for i in range(0, length - 1):

    ones = 0
    zeroes = 0

    for line in lines:
        if line[i] == '0':
            zeroes += 1
        else:
            ones += 1

    if ones > zeroes:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gammaParsed = int(gamma, 2)
epsilonParsed = int(epsilon, 2)

print(gammaParsed * epsilonParsed)

