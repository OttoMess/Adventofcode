import time
import re

EXAMPLE = "AoC_inputs/2024/day_4_example.txt"
INPUT = "AoC_inputs/2024/day_4.txt"


class Puzzle4:
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
                data.append(line.strip())
        self.input = data

    def part1(self):
        default = self.find_xmas(self.input)
        transposed = self.find_xmas(self.transpose(self.input))
        diagonal = self.find_xmas(self.diagonal(self.input))
        diagonal_reverse = self.diagonal_reverse(self.input)
        return default + transposed + diagonal

    def part2(self):
        return

    @staticmethod
    def find_xmas(data):
        collect = 0
        for line in data:
            normal = re.findall("XMAS", line)
            inverse = re.findall("SAMX", line)
            collect += len(normal + inverse)
        return collect

    @staticmethod
    def transpose(data):
        transposed = ["" for i in data]
        for line in data:
            for i, _ in enumerate(line):
                transposed[i] += line[i]

        return transposed

    @staticmethod
    def diagonal(data):
        stack = list()
        for b in range(len(data[0])):
            w = ""
            for i in range(len(data[0]) - b):
                w += data[i][b + i]
            stack.append(w)

        for a in range(1, len(data)):
            w = ""
            for i in range(len(data[0]) - a):
                w += data[a + i][i]
            stack.append(w)

        return stack

    @staticmethod  # TODO update and check if it works
    def diagonal_reverse(data):
        stack = list()
        for b in range(len(data[0])):
            w = ""
            for i in range(len(data[0]) - b, 0):
                w += data[i][i - b]
            stack.append(w)

        for a in range(1, len(data)):
            w = ""
            for i in range(len(data[0]) - a):
                w += data[a + i][i]
            stack.append(w)

        return stack

    # TODO build function to make move the data into a diagonal. Likely need 2 functions 45° and -45°
    # start positions top left side[i,j] add next pos would be [i+1, j+1]


Puzzle4(EXAMPLE)
Puzzle4(INPUT)
