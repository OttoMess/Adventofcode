import time
from heapq import heappush, heappop
from functools import cache

EXAMPLE = "AoC_inputs/2025/day_11_example.txt"
INPUT = "AoC_inputs/2025/day_11.txt"


class Puzzle11:
    def __init__(self, path) -> None:
        start_time = time.time()

        self.file_path = path
        self.input = dict()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self) -> None:
        data = dict()
        keys = []
        with open(self.file_path) as file:
            for line in file:
                key = line.split(":")[0]
                output = line.split(":")[1].strip().split()
                data[key] = output
                keys.append(key)

        self.keys = keys
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

    def find_end(self, start, end) -> int:
        queue = {}
        queue[start] = 1

        counter = 0
        while len(queue) > 0:
            item = next(iter(queue))
            amount = queue[item]
            del queue[item]

            if item == end:
                counter += amount
            elif item == "out":
                continue
            else:
                to_add = self.input[item]

                for i in to_add:
                    try:
                        queue[i] += amount
                    except:
                        queue[i] = amount

        return counter

    def part2(self) -> int:

        a = self.find_end("svr", "fft")
        b = self.find_end("fft", "dac")
        c = self.find_end("dac", "out")

        d = self.find_end("svr", "dac")
        e = self.find_end("dac", "fft")
        f = self.find_end("fft", "out")

        return a * b * c + d * e * f


Puzzle11(EXAMPLE)
Puzzle11(INPUT)
