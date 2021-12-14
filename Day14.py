file = open("Day14.txt", "r")

template = file.readline().strip()

file.readline()

insertionrules = {}

while line := file.readline().strip():
    split = line.split(" -> ")
    insertionrules[split[0]] = split[1]

for _ in range(10):

    newTemplate = ""

    for i in range(len(template) - 1):

        inserted = insertionrules[template[i] + template[i + 1]]

        newTemplate += template[i] + inserted

    newTemplate += template[len(template) - 1]
    template = newTemplate
    
count = {}

for char in template:
    
    if char not in count.keys():
        count[char] = 0
    
    count[char] += 1

sorted = sorted(count.values())
print(count)
print(next(iter(reversed(sorted))) - next(iter(sorted)))

