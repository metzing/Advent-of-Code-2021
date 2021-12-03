def _digitAtIndexEquals(digit : str, index : int):

    def _result(line : str):
        return line[index] == digit
    
    return _result

file = open("Day03.txt", "r")

lines = file.readlines()

length = len(lines[0])

# finding oxygen value

i = 0
oxygenCandidateLines = lines

while len(oxygenCandidateLines) > 1:

    ones = 0
    zeroes = 0

    for line in oxygenCandidateLines:
        if line[i] == '0':
            zeroes += 1
        else:
            ones += 1

    if ones > zeroes:
        oxygenCandidateLines = list(filter(_digitAtIndexEquals("1", i), oxygenCandidateLines))
    elif ones < zeroes:
        oxygenCandidateLines = list(filter(_digitAtIndexEquals("0", i), oxygenCandidateLines))
    else:
        oxygenCandidateLines = list(filter(_digitAtIndexEquals("1", i), oxygenCandidateLines))

    i += 1 
        
oxygen = int(oxygenCandidateLines[0], 2)

# finding co2 value

co2CandidateLines = lines
i = 0

while len(co2CandidateLines) > 1:

    ones = 0
    zeroes = 0

    for line in co2CandidateLines:
        if line[i] == '0':
            zeroes += 1
        else:
            ones += 1

    if ones > zeroes:
        co2CandidateLines = list(filter(_digitAtIndexEquals("0", i), co2CandidateLines))
    elif ones < zeroes:
        co2CandidateLines = list(filter(_digitAtIndexEquals("1", i), co2CandidateLines))
    else:
        co2CandidateLines = list(filter(_digitAtIndexEquals("0", i), co2CandidateLines))

    i += 1 

co2 = int (co2CandidateLines[0], 2)

print(oxygen * co2)

