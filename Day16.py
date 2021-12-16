from functools import reduce

class ValuePacket:
    def __init__(self, version, value) -> None:
        self.__version = version
        self.__value = value

    @property
    def version(self):
        return self.__version 

    @property
    def value(self):
        return self.__value 

class OperatorPacket:
    def __init__(self, version, typeid, children) -> None:
        self.__version = version
        self.__typeid = typeid
        self.__children = children

    @property
    def version(self):
        return self.__version

    @property
    def children(self):
        return self.__children

    @property
    def value(self):
        childvalues = [child.value for child in self.children]

        match self.__typeid:
            case 0:
                return reduce(lambda aggr, item: aggr + item, childvalues, 0)
            case 1:
                return reduce(lambda aggr, item: aggr * item, childvalues, 1)
            case 2:
                return min(childvalues)
            case 3:
                return max(childvalues)
            case 5:
                return 1 if childvalues[0] > childvalues[1] else 0
            case 6:
                return 1 if childvalues[0] < childvalues[1] else 0
            case 7:
                return 1 if childvalues[0] == childvalues[1] else 0 

def parseValuePacket(version, tail):

    value = ""
    offset = 0
    packetend = False

    while not packetend:
        group = tail[offset : offset + 5]
        if group[0] == "0":
            packetend = True
        offset += 5
        value += group[1 : 5]

    result = ValuePacket(version, int(value, 2))
    
    return result, tail[offset : len(tail)]

def parseOperatorPacket(version, typeid, tail):
    lengthtypeid = tail[0]
    children = []
    if lengthtypeid == "0":
        numberofbits = int(tail[1 : 16], 2)
        inpacket = tail[16 : 16 + numberofbits]
        remainder = tail[16 + numberofbits : len(tail)]

        while inpacket != "":
            child, inpacket = parse(inpacket)
            children.append(child)

        return OperatorPacket(version, typeid, children), remainder
    else:
        numberofpackets = int(tail[1 : 12], 2)
        tail = tail[12 : len(tail)]

        for _ in range(numberofpackets):
            child, tail = parse(tail)
            children.append(child)
        
        return OperatorPacket(version, typeid, children), tail

def parse(bits : str):
    version = int(bits[0 : 3], 2)
    typeid =  int(bits[3 : 6], 2)
    if (typeid == 4):
        # value packet
        return parseValuePacket(version, bits[6 : len(bits)])
    else:
        # operator packet
        return parseOperatorPacket(version, typeid, bits[6 : len(bits)])

hextobits = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}

bits = ""

hexes = open("Day16.txt", "r").readline().strip()

for hex in hexes:
    bits += hextobits[hex]

root, tail = parse(bits)

print(root.value)