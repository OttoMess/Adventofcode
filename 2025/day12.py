import time


EXAMPLE = "AoC_inputs/2025/day_12_example.txt"
INPUT = "AoC_inputs/2025/day_12.txt"


class Puzzle12:
    def __init__(self, path) -> None:
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self) -> None:
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.input = data

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0


Puzzle12(EXAMPLE)
Puzzle12(INPUT)

"""
volkskrant.nl/?referrer=https%3A%2F%2Fduckduckgo.com%2F
"""
