import time
import itertools

DATA = "data/day12.txt"
EXAMPLE = "data/day12_example.txt"
TEST = "data/day12_test.txt"


class Puzzle12:

    def __init__(self, path):
        self.vents = None
        self.groups = None
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.part1()
        # self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        # print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        self.read_txt()
        print("test")

    def read_txt(self):
        raw = list()
        groups = list()
        vents = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
                groups.append(line.split(" ")[1].strip().split(","))
                vents.append(line.split(" ")[0].strip())
        self.data = raw
        self.groups = groups
        self.vents = vents


Puzzle12(EXAMPLE)