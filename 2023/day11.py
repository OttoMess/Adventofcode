import time
import itertools

DATA = "data/day11.txt"
EXAMPLE = "data/day11_example.txt"
TEST = "data/day11_test.txt"


class Puzzle11:

    def __init__(self, path):
        self.part1_distance = None
        self.raw = None
        self.galaxy_list = None
        self.row_exp = None
        self.col_exp = None
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.part1()
        self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        self.read_txt()
        self.col_expansion(True)
        self.row_expansion(True)
        self.galaxy_finder()

        sets = [subset for subset in itertools.combinations(self.galaxy_list, 2)]
        distance = list()
        for s in sets:
            distance.append(self.distance(s))
        self.part1_distance = distance
        self.part1_collector = sum(distance)

    def part2(self):
        # del self.data
        self.read_txt()
        self.col_expansion()
        self.row_expansion()
        self.galaxy_finder()

        sets = [subset for subset in itertools.combinations(self.galaxy_list, 2)]
        distance = list()
        for s in sets:
            distance.append(self.distance_non_expanded(s, int(1e6)-1))

        self.part2_collector = sum(distance)

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        self.data = raw

    def col_expansion(self, grow=False):
        expand = list()
        for j, _ in enumerate(self.data[0]):
            collector = str()
            for i in self.data:
                collector += i[j]
            if collector.count("#") == 0:
                expand.append(j)

        self.col_exp = expand
        # expand.sort(reverse=True)
        if grow is True:
            for e in sorted(expand, reverse=True):
                for j, i in enumerate(self.data):
                    self.data[j] = i[0:e] + '.' + i[e:]

    def row_expansion(self, grow=False):
        expand = list()
        for j, _ in enumerate(self.data):
            if _.count("#") == 0:
                expand.append(j)
        self.row_exp = expand

        # expand.sort(reverse=True)
        space = "".join("." for _ in self.data[0])
        if grow is True:
            for i in sorted(expand, reverse=True):
                self.data.insert(i, space)

    def galaxy_finder(self):
        galaxy = list()
        for j, i in enumerate(self.data):
            for u, c in enumerate(i):
                if c == "#":
                    galaxy.append([j, u])
        self.galaxy_list = galaxy

    @staticmethod
    def distance(combination: list):
        first = combination[0]
        second = combination[1]

        row_dis = first[0] - second[0]
        col_dis = first[1] - second[1]

        return abs(row_dis) + abs(col_dis)

    def distance_non_expanded(self, combination: list, expand: int = 1):
        first = combination[0]
        second = combination[1]

        row_space = sorted([first[0], second[0]])
        col_space = sorted([first[1], second[1]])

        col_count = 0
        for s in self.col_exp:
            if col_space[0] < s < col_space[1]:
                col_count += 1

        row_count = 0
        for s in self.row_exp:
            if row_space[0] < s < row_space[1]:
                row_count += 1

        row_dis = abs(row_space[0] - row_space[1]) + row_count * expand
        col_dis = abs(col_space[0] - col_space[1]) + col_count * expand

        return col_dis + row_dis


Puzzle11(EXAMPLE)
Puzzle11(DATA)
