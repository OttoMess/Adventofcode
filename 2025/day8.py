import time


EXAMPLE = "AoC_inputs/2025/day_8_example.txt"
INPUT = "AoC_inputs/2025/day_8.txt"


class Puzzle8:
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
                data.append(tuple([int(i) for i in line.strip().split(",")]))
        self.input = tuple(data)

    def part1(self) -> int:
        """
        https://en.wikipedia.org/wiki/Euclidean_distance


        Docstring for part1
        {\displaystyle d(p,q)={\sqrt {(p_{1}-q_{1})^{2}+(p_{2}-q_{2})^{2}+(p_{3}-q_{3})^{2}}}.}
        :param self: Description
        :return: Description
        :rtype: int
        """

        return 0

    def part2(self) -> int:
        return 0


Puzzle8(EXAMPLE)
Puzzle8(INPUT)
