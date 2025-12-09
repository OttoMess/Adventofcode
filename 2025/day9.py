import time
import itertools

EXAMPLE = "AoC_inputs/2025/day_9_example.txt"
INPUT = "AoC_inputs/2025/day_9.txt"


class Puzzle9:
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
                x, y = line.strip().split(",")
                data.append((int(x), int(y)))
        self.input = tuple(data)

    def part1(self) -> int:
        combinations = [list(x) for x in itertools.combinations(self.input, 2)]
        max_area = 0
        for a, b in combinations:
            height = abs(a[0] - b[0]) + 1
            length = abs(a[1]-b[1]) + 1
            area = height * length
            if area > max_area:
                max_area = area

        return max_area

    def part2(self) -> int:
        return 0


Puzzle9(EXAMPLE)
Puzzle9(INPUT)
