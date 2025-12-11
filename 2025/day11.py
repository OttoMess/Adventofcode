import time
from heapq import heappush, heappop

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
        loop = 0
        while len(queue) > 0:
            item = heappop(queue)
            if item[0] == "out":
                if item[1] and item[2]:
                    counter += 1
            else:
                if item[0] == "fft":
                    item[1] = True
                elif item[0] == "dac":
                    item[2] = True

                # for i in self.input[item[0]]:
                #     heappush(queue, [i] + item[1:])
                # # a = 1
                [heappush(queue, [i] + item[1:]) for i in self.input[item[0]]]
            loop += 1

            if loop % 1_000_000 == 0:
                print(len(queue), counter)

        return counter


Puzzle11(EXAMPLE)
Puzzle11(INPUT)

# 992940 to low for part 2
