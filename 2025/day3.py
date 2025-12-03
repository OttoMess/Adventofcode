import time


EXAMPLE = "AoC_inputs/2025/day_3_example.txt"
INPUT = "AoC_inputs/2025/day_3.txt"


class Puzzle3:
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
                lose = tuple([int(n) for n in line.strip()])
                data.append(lose)
        self.input = data

    def part1(self):
        collector = 0

        for bank in self.input:
            max_joltage = int()

            for i,left_bat in enumerate(bank):
                left = left_bat
                if left * 10 < max_joltage:
                    continue

                for right_loc in range(i+1,len(bank)):
                    right = bank[right_loc]
                    joltage = left * 10 + right

                    if joltage > max_joltage:
                        max_joltage = joltage

            collector += max_joltage

        return collector

    def part2(self):
        collector = 0
        return collector


Puzzle3(EXAMPLE)
Puzzle3(INPUT)
