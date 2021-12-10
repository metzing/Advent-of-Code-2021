pointValueByClosing = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137,
}

corresponding = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">",
}

stack = []
points = 0

for line in open("Day10.txt", "r").readlines():
    
    for char in line.strip():

        if char in corresponding.keys():
            stack.append(char)

        else:
            last = stack.pop()

            if char != corresponding[last]:
                points += pointValueByClosing[char]
                break

print(points)