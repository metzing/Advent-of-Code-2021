from functools import reduce
from itertools import permutations
import math

class Pair:
    def __init__(self, left, right) -> None:
        left.parent = self
        left.left_side = True
        right.parent = self
        right.left_side = False
        self.__left = left
        self.__right = right
        self.__left_side = None
        self.__parent = None

    def __repr__(self) -> str:
        return f"[{self.__left},{self.__right}]"

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value
    
    @property
    def left_side(self):
        return self.__left_side

    @left_side.setter
    def left_side(self, value):
        self.__left_side = value
    
    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value
    
    @property
    def magnitude(self):
        return self.__left.magnitude * 3 + self.__right.magnitude * 2

    def explode(self):
        left = self.__left.value
        right = self.__right.value

        left_node = find(self, True)
        if left_node is not None:
            left_node.value += left

        right_node = find(self, False)
        if right_node is not None:
            right_node.value += right

        replace(self, Regular(0))

class Regular:
    def __init__(self, value) -> None:
        self.__value = value
        self.__left_side = None
        self.__parent = None

    def __repr__(self) -> str:
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left_side(self):
        return self.__left_side

    @left_side.setter
    def left_side(self, value):
        self.__left_side = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value
    
    @property
    def magnitude(self):
        return self.__value

    def split(self):
        left = Regular(math.floor(self.__value / 2))
        right = Regular(math.ceil(self.__value / 2))
 
        parent = Pair(left, right)
        
        replace(self, parent)

def find(node, left):
    while node.left_side == left:
        node = node.parent
    
    node = node.parent
    
    if isinstance(node, Pair):
        node = node.left if left else node.right

    while True:
        if isinstance(node, Pair):
            node = node.right if left else node.left
        else:
            break

    return node

def replace(original, replacement):

    if original.left_side:
        original.parent.left = replacement
        replacement.left_side = True
        replacement.parent = original.parent
    else:
        original.parent.right = replacement
        replacement.left_side = False
        replacement.parent = original.parent

    return replacement


numbers = []

def parse(line):
    stack = []

    for char in line.strip():

        if char.isdigit():
            stack.append(Regular(int(char)))

        elif char == "]":
            right = stack.pop()
            left = stack.pop()

            pair = Pair(left, right)

            stack.append(pair)
    
    root = stack.pop()
    root.parent = None

    return root

for line in open("Day18.txt", "r").readlines():
    root = parse(line)
    
    numbers.append(root)

def reduce(root):

    return  reducedepth(root) or reducelarge(root)

def reducedepth(node, depth=None):
    if depth is None:
        depth = 0
    
    if isinstance(node, Pair):
        if depth > 3 and not (isinstance(node.left, Pair) or isinstance(node.right, Pair)):
            node.explode()
            return True
        else:
            return reducedepth(node.left, depth + 1) or reducedepth(node.right, depth + 1)
    else:
        return False

def reducelarge(node):
    if isinstance(node, Regular):
        if node.value > 9:
            node.split()
            return True
        else:
            return False
    else:
        return reducelarge(node.left) or reducelarge(node.right)

magnitudes = []

for left, right in permutations(numbers, 2):
    p = parse(f"[{left},{right}]")

    while True:
        if not reduce(p):
            break
    
    magnitudes.append(p.magnitude)

print(max(magnitudes))