pointValueByClosing = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4,
}

corresponding = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">",
}

points = []

for line in open("Day10.txt", "r").readlines():

    corrupted = False
    stack = []

    for char in line.strip():

        if char in corresponding.keys():
            stack.append(char)

        else:
            last = stack.pop()

            if char != corresponding[last]:
                corrupted = True
                break
    
    if (not corrupted):

        score = 0

        missingClosingChars = [corresponding[item] for item in reversed(stack)]

        for char in missingClosingChars:
            score = score * 5 + pointValueByClosing[char]

        points.append(score)


print(sorted(points)[int(len(points) / 2)])