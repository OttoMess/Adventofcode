import time
from collections import Counter

EXAMPLE = "AoC_inputs/2024/day_2_example.txt"
INPUT = "AoC_inputs/2024/day_2.txt"


class Puzzle2:
    def __init__(self, path):
        self.file_path = path
        self.input = list()
        self.reports = list()

        print(self.file_path)

        start_time = time.time()
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append([int(i) for i in line.strip().split()])
        self.input = data

    def part1(self):
        counter = 0
        for line in self.input:
            if self.validate(line):
                counter += 1
        return counter

    @staticmethod
    def validate(line):
        delta = [line[i] - line[i - 1] for i in range(1, len(line))]

        if all([d in [1, 2, 3] for d in delta]):
            return True
        elif all([d in [-1, -2, -3] for d in delta]):
            return True
        else:
            False

    def part2(self):
        counter = 0
        for line in self.input:
            for i, _ in enumerate(line):
                test_line = line[:i] + line[i + 1 :]
                if self.validate(test_line):
                    counter += 1
                    break

        return counter


Puzzle2(EXAMPLE)
Puzzle2(INPUT)
