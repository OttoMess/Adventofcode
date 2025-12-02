import time
import math

EXAMPLE = "AoC_inputs/2025/day_2_example.txt"
INPUT = "AoC_inputs/2025/day_2.txt"


class Puzzle2:
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
                raw = line.strip().split(",")
                for i in raw:
                    if i == "":
                        continue
                    data.append([int(j) for j in i.split("-")])
        self.input = data

    @staticmethod
    def check_for_doubles(id):
        digits = int(math.log10(id))+1

        if digits % 2 == 0:
            power = int(10**(digits/2))
            right = id % power
            left = id//power
            if left == right:
                return id

        return 0

    def part1(self):
        collector = 0
        for j in self.input:
            ids = range(j[0], j[1]+1)
            for i in ids:
                collector += self.check_for_doubles(i)

        return collector

    def part2(self):
        return


Puzzle2(EXAMPLE)
Puzzle2(INPUT)
