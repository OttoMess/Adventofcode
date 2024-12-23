import time
from functools import cache

EXAMPLE = "AoC_inputs/2024/day_19_example.txt"
INPUT = "AoC_inputs/2024/day_19.txt"

# https://www.geeksforgeeks.org/number-of-ways-to-form-a-given-string-from-the-given-set-of-strings/


class Puzzle19:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()
        answer = self.part1and2()

        print(f"output part one: {next(answer)}")
        print(f"output part two: {next(answer)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        self.patterns = list()
        with open(self.file_path) as file:
            for i, line in enumerate(file):
                if i == 0:
                    self.towels = [i.strip() for i in line.strip().split(",")]
                elif i > 1:
                    self.patterns.append(line.strip())

    def part1and2(self):
        self.towels.sort(key=lambda s: len(s))
        self.small = len(self.towels[0])  # used in self.possible
        self.large = len(self.towels[-1])
        counter_1 = 0
        counter_2 = 0
        for p in self.patterns:
            found = self.possible(p, tuple(self.towels))
            if found > 0:
                counter_1 += 1
                counter_2 += found
        yield counter_1
        yield counter_2

    @cache
    def possible(self, pattern, towels):
        # recursive function which returns how many are found
        if len(pattern) == 0:
            return 1
        elif len(pattern) >= self.large:
            view = range(self.small, self.large + 1)
        else:
            view = range(self.small, len(pattern) + 1)

        total = 0
        for i in view:
            if pattern[0:i] in towels:
                found = self.possible(pattern[i:], towels)
                if found > 0:
                    total += found
        return total


Puzzle19(EXAMPLE)
Puzzle19(INPUT)
