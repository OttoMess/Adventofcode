import matplotlib.pyplot as plt
import time
from dataclasses import dataclass
# import matplotlib
# matplotlib.use('TkAgg')

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
            coordinates = []
            for i in range(begin, end):
                if i % 5 == 0:
                    marker = int(data[i][0])
                else:
                    for j, c in enumerate(data[i]):
                        if c == "#":
                            plt.ion()
                            coordinates.append([(i % 5)-1, j])

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

    @staticmethod
    def plot_map(size):
        # plt.ion()
        width = size[0]
        height = size[1]
        b = 6
        fig = plt.figure(figsize=((width/height)*b, b))
        plt.xlim(1, width)
        plt.ylim(1, height)
        plt.xticks(range(1, width+1))
        plt.yticks(range(1, height+1))
        plt.grid()
        fig.tight_layout()
        # plt.plot([1, 2], [2, 3])
        plt.show(block=True)

    def part1(self) -> int:
        t: Region
        for t in self.trees:
            self.plot_map(t.size)
        return 0

    def part2(self) -> int:
        return 0


@dataclass
class Region:
    size: list
    pieces: dict


Puzzle12(EXAMPLE)
# Puzzle12(INPUT)

"""
https://medium.com/better-programming/automating-puzzle-solving-with-python-f3ecc242e059
"""
