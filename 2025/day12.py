import time
from dataclasses import dataclass

EXAMPLE = "AoC_inputs/2025/day_12_example.txt"
INPUT = "AoC_inputs/2025/day_12.txt"


class Puzzle12:
    def __init__(self, path) -> None:
        start_time = time.time()

        self.file_path = path
        self.shapes = {}
        self.trees = []

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self) -> None:
        with open(self.file_path) as file:
            data = [x.strip() for x in file]

        shapes = {}
        begin = 0
        marker = int()
        while begin < 28:
            end = begin + 5
            # base = [["." for _ in range(3)] for _ in range(3)]
            coordinates = []
            for i in range(begin, end):
                if i % 5 == 0:
                    marker = int(data[i][0])
                else:
                    for j, c in enumerate(data[i]):
                        if c == "#":
                            # base[(i % 5)-1][j] = marker
                            coordinates.append([(i % 5)-1, j])
            # shapes[marker] = base
            shapes[marker] = coordinates
            begin += 5
        self.shapes = shapes

        tasks = []
        for i in range(30, len(data)):
            a, b = data[i].split(":")
            size = [int(x) for x in a.split("x")]
            pieces = {}
            for i, j in enumerate([int(x) for x in b.split()]):
                pieces[i] = j

            tasks.append(Region(size=size, pieces=pieces))

        self.trees = tasks

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


@dataclass
class Region:
    size: list
    pieces: dict


Puzzle12(EXAMPLE)
Puzzle12(INPUT)

"""
https://medium.com/better-programming/automating-puzzle-solving-with-python-f3ecc242e059
"""
