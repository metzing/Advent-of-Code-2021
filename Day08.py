from functools import reduce

class SegmentDigit:
    allSegments = [ "a", "b", "c", "d", "e", "f", "g" ]

    digitBySegments = {
        "abcefg" : 0,
        "cf" : 1,
        "acdeg" : 2,
        "acdfg" : 3,
        "bcdf" : 4,
        "abdfg" : 5,
        "abdefg" : 6,
        "acf" : 7,
        "abcdefg" : 8,
        "abcdfg" : 9,
    }

    digitsBySegment = {
        "a" : [ 0, 2, 3, 5, 6, 7, 8, 9 ],
        "b" : [ 0, 4, 5, 6, 8, 9 ],
        "c" : [ 0, 1, 2, 3, 4, 7, 8, 9 ],
        "d" : [ 2, 3, 4, 5, 6, 8, 9 ],
        "e" : [ 0, 2, 6, 8 ],
        "f" : [ 0, 1, 3, 4, 5, 6, 7, 8, 9 ],
        "g" : [ 0, 2, 3, 5, 6, 8, 9 ]
    }

    segmentsCountByDigit = {
        0 : 6,
        1 : 2,
        2 : 5,
        3 : 5,
        4 : 4,
        5 : 5,
        6 : 6,
        7 : 3,
        8 : 7,
        9 : 6,
    }

    digitsBySegmentsCount = {
        2 : [ 1 ],
        3 : [ 7 ],
        4 : [ 4 ],
        5 : [ 2, 3, 5 ],
        6 : [ 0, 6, 9 ],
        7 : [ 8 ],
    }

    def uniqueSegmentCounts() -> list:

        for segmentsCount in SegmentDigit.digitsBySegmentsCount:
            if len(SegmentDigit.digitsBySegmentsCount[segmentsCount]) == 1:
                yield segmentsCount, SegmentDigit.digitsBySegmentsCount[segmentsCount][0]


    def __init__(self, segments : str) -> None:
        self.__segments = segments

    @property
    def segments(self) -> str:
        return self.__segments

    @property
    def segmentsCount(self) -> int:
        return len(self.__segments)

Digits = list[SegmentDigit]

class Display:

    def parse(line : str):

        split = line.strip().split(" | ")

        allDigits = [SegmentDigit(item) for item in split[0].split(" ")]
        outputDigits = [SegmentDigit(item) for item in split[1].split(" ")]

        return Display(allDigits, outputDigits)
    
    def __init__(self, allDigits : list, outputDigits : list):
        self.__allDigits = allDigits
        self.__outputDigits = outputDigits
        self.__value = -1
        self.__mapping = {}

    @property 
    def outputDigits(self) -> Digits:
        return self.__outputDigits

    @property 
    def allDigits(self) -> Digits:
        return self.__allDigits

    @property
    def value(self) -> int:

        if self.__value == -1:
            self.solve()
        
        return self.__value
        
    def solve(self):

        one = next(filter(lambda digit: digit.segmentsCount == 2 , self.allDigits))
        four = next(filter(lambda digit: digit.segmentsCount == 4, self.allDigits))
        seven = next(filter(lambda digit: digit.segmentsCount == 3, self.allDigits))

        # segment a
        self.__mapping["a"] = next(segment for segment in seven.segments if segment not in one.segments)

        sumOfOccurences = dict((char, 0) for char in SegmentDigit.allSegments)
        
        for char in "".join([digit.segments for digit in self.__allDigits]):
            sumOfOccurences[char] += 1

        # segment b
        self.__mapping["b"] = next(char for char in sumOfOccurences if sumOfOccurences[char] == 6)

        # segment c
        self.__mapping["c"] = next(char for char in sumOfOccurences if sumOfOccurences[char] == 8 and char != self.__mapping["a"])

        # segment e
        self.__mapping["e"] = next(char for char in sumOfOccurences if sumOfOccurences[char] == 4)

        # segment f
        self.__mapping["f"] = next(char for char in sumOfOccurences if sumOfOccurences[char] == 9)

        dg = [char for char in SegmentDigit.allSegments if char not in self.__mapping.values()]

        # segment g
        self.__mapping["g"] = next(char for char in dg if char not in four.segments)

        # segment d
        self.__mapping["d"] = next(char for char in dg if char not in self.__mapping["g"])
    
    
        decode = {v: k for k, v in self.__mapping.items()}

        output = [SegmentDigit.digitBySegments["".join(sorted([decode[segment] for segment in digit.segments]))] for digit in self.outputDigits]

        self.__value = output[0] * 1000 + output[1] * 100 + output[2] * 10 + output[3]



displays = [Display.parse(line) for line in open("Day08.txt", "r").readlines()]

print(sum([display.value for display in displays]))