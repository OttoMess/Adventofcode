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
                # make the puzzle pieces with 1 to 5 numbers, for visualization
                data.append(line.strip())

        shapes = {}
        begin = 0
        while begin < 28:
            end = begin + 5
            base = [["." for _ in range(3)] for _ in range(3)]
            coordinates = []
            for i in range(begin, end):
                if i % 5 == 0:
                    marker = int(data[i][0])
                else:
                    for j, c in enumerate(data[i]):
                        if c == "#":
                            base[(i % 5)-1][j] = marker
                            coordinates.append([(i % 5)-1, j])
            shapes[marker] = base
            begin += 5
        self.shapes = shapes

        for i in range(30, len(data)+1):
            a, b = data[i].split(":")
            size = [int(x) for x in a.split("x")]
            pieces = [int(x) for x in b.split()]
        self.input = data

    @staticmethod
    def rotate_shape(shape) -> list:
        """
        turn can be 

        :param shape: input list of shape to be turned
        """
        turned_shape = []
        return turned_shape

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0


Puzzle12(EXAMPLE)
Puzzle12(INPUT)

"""
volkskrant.nl/?referrer=https%3A%2F%2Fduckduckgo.com%2F
"""
