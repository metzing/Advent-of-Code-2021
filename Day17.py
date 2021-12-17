input = open("Day17.txt", "r").readline().strip()

input = input.replace("target area: x=", "").replace(", y=", "..").split("..")

xRange = range(int(input[0]),int(input[1]) + 1)
yRange = range(int(input[2]), int(input[3]) + 1)

def x_hits(candidate):

    position = 0
    stepsCounter = 0
    speed = candidate
    steps = []

    while position <= xRange[-1] and speed != 0:

        stepsCounter += 1
        position += speed
        speed = speed - 1 if speed > 0 else speed + 1

        if position in xRange:
            steps.append((stepsCounter, speed))
         
    return candidate, steps

xCandidates = dict((x, steps) for (x, steps) in (x_hits(x) for x in range(xRange[-1] + 1)) if any(steps))
print(xCandidates)

# since if we start with x speed of 24 we stop (on the x axis) exactly inside the target
# and we always have a point at (24, 0)
# we can use the throw that would have the maximum y speed downwards at (24, 0)
# to still remain inside the y bounds of the target
# that means that our starting y speed is one less than the abs of our lower y bounds
print(sum(range(0, -yRange.start)))
