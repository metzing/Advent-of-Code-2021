file = open("Day14.txt", "r")

template = file.readline().strip()

file.readline()

insertionrules = {}

while line := file.readline().strip():
    split = line.split(" -> ")
    insertionrules[split[0]] = split[1]

replacementPairs = {}

for pair in insertionrules.keys():
    replacementPairs[pair] = [ pair[0] + insertionrules[pair], insertionrules[pair] + pair[1] ]

currentPairs = {}

for i in range(len(template) - 1):

    pair = template[i] + template[i + 1]
    
    if pair not in currentPairs.keys():
        currentPairs[pair] = 0

    currentPairs[pair] += 1

for _ in range(40):

    nextPairs = {}

    for pair in currentPairs.keys():

        replacements = replacementPairs[pair]

        if replacements[0] not in nextPairs.keys():
            nextPairs[replacements[0]] = 0

        if replacements[1] not in nextPairs.keys():
            nextPairs[replacements[1]] = 0

        nextPairs[replacements[0]] += currentPairs[pair]
        nextPairs[replacements[1]] += currentPairs[pair]

    currentPairs = nextPairs

count = {}

for pair in currentPairs.keys():
    
    for char in pair:

        if char not in count.keys():
            count[char] = 0
    
        count[char] += currentPairs[pair]

sorted = sorted(round(value / 2) for value in count.values())

print(next(iter(reversed(sorted))) - next(iter(sorted)))

