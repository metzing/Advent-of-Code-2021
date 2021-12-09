from functools import reduce 

class SegmentDigit:
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
    
    @property
    def hasDefiniteValue(self) -> bool:

        for unique, value in SegmentDigit.uniqueSegmentCounts():
            if self.segmentsCount == unique:
                self.__value = value
                return True

        return False
    
    @property
    def value(self) -> int:
        if (self.hasDefiniteValue):
            return self.__value
        else:
            raise "No definite Value"

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

    @property 
    def outputDigits(self) -> Digits:
        return self.__outputDigits

    @property
    def definitiveOutputNumbers(self):
        for digit in self.outputDigits:
            if digit.hasDefiniteValue:
                yield digit 



displays = [Display.parse(line) for line in open("Day08.txt", "r").readlines()]

print(reduce(lambda sum, count: sum + count, [len(list(display.definitiveOutputNumbers)) for display in displays], 0))