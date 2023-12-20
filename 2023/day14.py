import time

# from functools import cache
# import itertools

DATA = "data/day14.txt"
EXAMPLE = "data/day14_example.txt"
TEST = "data/day14_test.txt"


class Puzzle14:

    def __init__(self, path):
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.read_txt()

        self.part1()
        # self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        # print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        self.up_north()
        pass

    def part2(self):
        pass

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        self.data = raw

    def up_north(self):
        north = list()

        while

        for j, line in enumerate(self.data):
            north.append(line)
            if j == 0:
                continue
            else:
                loc = [k for k, c in enumerate(line) if c == "O"]
                if len(loc) == 0:
                    continue
                else:
                    for l in loc:
                        if north[j-1][l] == ".":
                            north[j-1] = north[j-1][:l] + "O" + north[j-1][l+1:]
                            north[j] = north[j][:l] + "." + north[j][l+1:]

            self.north = north




Puzzle14(EXAMPLE)
