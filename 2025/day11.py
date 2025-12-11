import time
from heapq import heappush, heappop

EXAMPLE = "AoC_inputs/2025/day_11_example.txt"
INPUT = "AoC_inputs/2025/day_11.txt"


class Puzzle11:
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
        data = dict()
        with open(self.file_path) as file:
            for line in file:
                key = line.split(":")[0]
                output = line.split(":")[1].strip().split()
                data[key] = output
        self.input = data

    def part1(self) -> int:
        queue = []
        [heappush(queue, i) for i in self.input["you"]]

        counter = 0
        while len(queue) > 0:
            item = heappop(queue)
            if item == "out":
                counter += 1
            else:
                [heappush(queue, i) for i in self.input[item]]

        return counter

    def part2(self) -> int:
        queue = []
        [heappush(queue, [i, False, False]) for i in self.input["svr"]]

        counter = 0
        while len(queue) > 0:
            item = heappop(queue)
            if item[0] == "out":
                if "fft" in item and "dac" in item:
                    counter += 1
            else:

                # [heappush(queue, [i] + item) for i in self.input[item[0]]]

        return counter


Puzzle11(EXAMPLE)
Puzzle11(INPUT)
