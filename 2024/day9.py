import time
from dataclasses import dataclass


EXAMPLE = "AoC_inputs/2024/day_9_example.txt"
INPUT = "AoC_inputs/2024/day_9.txt"


class Puzzle9:
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
                data = line
        self.input = data

    """
    6349343813585 to low
    """

    def part1(self):
        id_number = 0
        id_list = list()
        data = list()
        for i, c in enumerate(self.input):
            amount = int(c)
            if i % 2 == 0:
                for _ in range(amount):
                    data.append(id_number)
                    id_list.append(id_number)
                id_number += 1
            else:
                for _ in range(amount):
                    data.append(".")

        new = list()
        self.a = len(data)
        for i in range(len(id_list)):
            if data[i] == ".":
                new.append(id_list.pop())
            else:
                new.append(data[i])

        counter = 0
        for i, value in enumerate(new):
            counter += i * value
        return counter

    def part2(self):
        id_number = 0
        block_list = list()
        data = list()
        for i, d in enumerate(self.input):
            amount = int(d)
            if amount == 0:
                continue
            elif i % 2 == 0:
                for _ in range(amount):
                    data.append([id_number, amount])
                block_list.append([id_number, amount])
                id_number += 1
            else:
                for _ in range(amount):
                    data.append([".", amount])
        new = list()
        block_list.reverse()
        for block in block_list:
            # search from lest to right for free space that will fit the block
            for i, d in enumerate(data):
                if d[0] != ".":
                    continue
                else:
                    free_space = 1
                    for k in range(1, len(data) - i):
                        pointer = k + i
                        if data[pointer][0] == ".":
                            free_space += 1
                        else:
                            break
                    if block[1] <= free_space:
                        data = [[".", 0] if item == block else item for item in data]
                        for w in range(block[1]):
                            data[i + w] = block
                        break

        return


Puzzle9(EXAMPLE)
Puzzle9(INPUT)
