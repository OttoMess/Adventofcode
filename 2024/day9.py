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

    def part1(self):
        data, single_files, _ = self.process_info()
        new = list()
        self.a = len(data)
        # end results will be length of all single files
        for i in range(len(single_files)):
            if data[i] == ".":
                new.append(single_files.pop())
            else:
                new.append(data[i])

        return self.count(new)

    def part2(self):
        data, _, blocks = self.process_info()

        blocks.reverse()  # search from left to right for free space that will fit the block
        for block in blocks:
            for i in range(block.index):  # prevent finding free-space right to block
                if data[i] == ".":
                    free_space = 1
                    for k in range(1, len(data) - i):
                        pointer = k + i
                        if data[pointer] == ".":
                            free_space += 1
                        else:
                            break
                    # check of block fits in free space
                    if block.amount <= free_space:
                        for w in range(block.amount):
                            data[i + w] = block.id
                            data[block.index + w] = "."
                        break
        return self.count(data)

    def process_info(self):
        id_number = 0
        blocks = list()
        data = list()
        id_list = list()
        for i, d in enumerate(self.input):
            amount = int(d)
            if amount == 0:
                continue
            # alternate between data and free space
            elif i % 2 == 0:
                blocks.append(Block(id_number, amount, len(data)))
                for _ in range(amount):
                    data.append(id_number)
                    id_list.append(id_number)
                id_number += 1
            else:
                for _ in range(amount):
                    data.append(".")
        return data, id_list, blocks

    @staticmethod
    def count(data):
        counter = 0
        for i, value in enumerate(data):
            if value != ".":
                counter += i * value
        return counter


@dataclass
class Block:
    id: int
    amount: int
    index: int


Puzzle9(EXAMPLE)
Puzzle9(INPUT)
