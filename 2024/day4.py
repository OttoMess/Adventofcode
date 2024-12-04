import time
import re

TEST = "AoC_inputs/2024/day_4_test.txt"
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
        diagonal_reverse = self.find_xmas(self.diagonal_reverse(self.input))
        return default + transposed + diagonal + diagonal_reverse

    def part2(self):
        a_index = list()
        for i in range(1, len(self.input) - 1):
            a_index.append([i, self.find_a_index(self.input[i])])
        data = self.input
        crosses = 0
        for line in a_index:
            y = line[0]
            for i in line[1]:
                x = i
                one = data[y - 1][x - 1] + data[y][x] + data[y + 1][x + 1]
                two = data[y + 1][x - 1] + data[y][x] + data[y - 1][x + 1]
                if one in ["MAS", "SAM"] and two in ["MAS", "SAM"]:
                    crosses += 1
        return crosses

    @staticmethod
    def find_a_index(line):
        return [i for i in range(1, len(line) - 1) if line[i] == "A"]

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

    @staticmethod
    def diagonal_reverse(data):
        stack = list()
        for b in range(len(data[0])):
            w = ""
            for i in range(len(data[0]) - b):
                w += data[i][len(data) - 1 - i - b]
            stack.append(w)

        for a in range(1, len(data)):
            w = ""
            for i in range(len(data[0]) - a):
                w += data[a + i][len(data[0]) - 1 - i]
            stack.append(w)

        return stack


# Puzzle4(TEST)
Puzzle4(EXAMPLE)
Puzzle4(INPUT)
