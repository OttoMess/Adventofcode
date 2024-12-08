import time
import itertools

EXAMPLE = "AoC_inputs/2024/day_8_example.txt"
INPUT = "AoC_inputs/2024/day_8.txt"


class Puzzle8:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

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
        self.input = data

    @staticmethod
    def find_antennas(data):
        book = dict()
        for y, line in enumerate(data):
            for x, cha in enumerate(line):
                if cha != ".":
                    if cha not in book.keys():
                        book[cha] = [(y, x)]
                    else:
                        book[cha].append((y, x))
        return book

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
                a = (one[0] + delta_y, one[1] + delta_x)
                b = (two[0] - delta_y, two[1] - delta_x)
                if (
                    a not in nodes
                    and 0 <= a[0] < len(self.input)
                    and 0 <= a[1] < len(self.input[0])
                ):
                    nodes.append(a)
                    node_map = self.place_antinode(node_map, a)
                if (
                    b not in nodes
                    and 0 <= b[0] < len(self.input)
                    and 0 <= b[1] < len(self.input[0])
                ):
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
                while 0 <= a[0] < len(self.input) and 0 <= a[1] < len(self.input[0]):
                    if a not in nodes:
                        nodes.append(a)
                    node_map = self.place_antinode(node_map, a)
                    a = [a[0] + delta_y, a[1] + delta_x]

                a = [pair[0][0] - delta_y, pair[0][1] - delta_x]
                while 0 <= a[0] < len(self.input) and 0 <= a[1] < len(self.input[0]):
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
