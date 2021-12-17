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

x_candidates = dict((x, steps) for (x, steps) in (x_hits(x) for x in range(xRange[-1] + 1)) if any(steps))
print(x_candidates)

# since if we start with x speed of 24 we stop (in the x direction) exactly inside the target
# and we always have a point at (24, 0)
# we can use the throw that would have the maximum y speed downwards at (24, 0)
# to still remain inside the y bounds of the target
# that means that our starting y speed is one less than the abs of our lower y bounds
print(sum(range(0, -yRange.start)))

velocities = []

def y_hits(x_speed, y_candidate, steps, stops):
    speed = (x_speed, y_candidate)
    position = (0, 0)
    steps_counter = 0

    while steps_counter <= steps[-1] or (stops and position[1] > yRange.start):

        steps_counter += 1
        position = (position[0] + speed[0], position[1] + speed[1]) 

        if position[0] in xRange and position[1] in yRange and \
            (steps_counter in steps or (steps_counter > steps[-1] and stops)):
            return True

        speed = (speed[0] - 1 if speed[0] > 0 else 0, speed[1] - 1)

    return False

for x, steps_velocities in x_candidates.items():
    steps = [step for step, _ in steps_velocities]
    stops = any(1 for _, velocity in steps_velocities if velocity == 0)
    for y_candidate in range(yRange.start, -yRange.start + 1):
        print(f"{x}, {y_candidate}, {steps}, {stops}")
        if y_hits(x, y_candidate, steps, stops):
            velocities.append((x, y_candidate))

counter = 0
for velocity in velocities:
    print(velocity, end="\t")
    counter += 1
    if counter % 8 == 0:
        print()
print()
print()
print(len(velocities))