import time
import itertools

EXAMPLE = "AoC_inputs/2024/day_8_example.txt"
INPUT = "AoC_inputs/2024/day_8.txt"

""" 
mapping used for the coordinates
     x ->
y      0 1 2
|    0 . . . 
V    1 . . .
     2 . . .
So get x,y point from data[y][x]
"""


class Puzzle8:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input: list
        self.x_lim: int
        self.x_lim: int

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.input = data

    @staticmethod
    def find_antennas(data):
        """
        Each antenna type will be key in dictionary.
        Each antenna of that type is added to the list of that type
        """
        book = dict()
        for y, line in enumerate(data):
            for x, cha in enumerate(line):
                if cha != ".":
                    if cha not in book.keys():
                        book[cha] = [(y, x)]
                    else:
                        book[cha].append((y, x))
        return book

    def in_grid(self, point):
        if 0 <= point[0] < self.y_lim and 0 <= point[1] < self.x_lim:
            return True
        return False

    def part1(self):
        node_map = self.duplicate()
        nodes = list()
        book = self.find_antennas(self.input)
        for antenna in book.keys():
            pairs = list(itertools.combinations(book[antenna], 2))
            for pair in pairs:
                one = pair[0]
                two = pair[1]
                delta_x = one[1] - two[1]
                delta_y = one[0] - two[0]
                a = (one[0] + delta_y, one[1] + delta_x)  # first is higher so add
                b = (two[0] - delta_y, two[1] - delta_x)  # second is lower so subtract
                if self.in_grid(a) and a not in nodes:
                    nodes.append(a)
                    node_map = self.place_antinode(node_map, a)
                if self.in_grid(b) and b not in nodes:
                    nodes.append(b)
                    node_map = self.place_antinode(node_map, b)
        return len(nodes)

    def part2(self):
        node_map = self.duplicate()
        nodes = list()
        book = self.find_antennas(self.input)
        for antenna in book.keys():
            pairs = list(itertools.combinations(book[antenna], 2))
            for pair in pairs:
                delta_x = pair[0][1] - pair[1][1]
                delta_y = pair[0][0] - pair[1][0]

                a = [pair[0][0], pair[0][1]]
                while self.in_grid(a):
                    if a not in nodes:
                        nodes.append(a)
                    node_map = self.place_antinode(node_map, a)
                    a = [a[0] + delta_y, a[1] + delta_x]

                # reset a to lower x,y cord
                a = [pair[0][0] - delta_y, pair[0][1] - delta_x]
                while self.in_grid(a):
                    if a not in nodes:
                        nodes.append(a)
                    node_map = self.place_antinode(node_map, a)
                    a = [a[0] - delta_y, a[1] - delta_x]

        return len(nodes)

    def duplicate(self):  # only for visual purposes
        duplicate = list()
        for line in self.input:
            duplicate.append("".join(["." for i in line]))
        return duplicate

    @staticmethod
    def place_antinode(map, node):  # only for visual purposes
        map[node[0]] = map[node[0]][: node[1]] + "#" + map[node[0]][node[1] + 1 :]
        return map


Puzzle8(EXAMPLE)
Puzzle8(INPUT)
