import time
from heapq import heappush, heappop
from functools import cache

EXAMPLE = "AoC_inputs/2025/day_7_example.txt"
INPUT = "AoC_inputs/2025/day_7.txt"


class Puzzle7:
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
                data.append(line.strip())
        self.input = data

    def part1(self) -> int:
        n_rows = len(self.input)
        counter = 0  # count if laser hit a splitter
        queue = []
        for i, c in enumerate(self.input[0]):  # find laser start
            if c == "S":
                heappush(queue,  (1, i))

        while len(queue) != 0:
            check = heappop(queue)
            if check[0] >= n_rows-1:
                break

            c = self.input[check[0] + 1][check[1]]
            if c == "^":
                counter += 1

                left = (check[0]+2, check[1]-1)
                right = (check[0]+2, check[1]+1)

                if left not in queue:
                    heappush(queue, left)
                if right not in queue:
                    heappush(queue, right)

            elif c == ".":
                lower = (check[0]+2, check[1])
                if lower not in queue:
                    heappush(queue, lower)

        return counter

    @staticmethod
    @cache
    def next_point(map, check) -> list:
        new_points = []
        c = map[check[0] + 1][check[1]]
        priority = -(check[0]+2)
        if c == "^":
            left = (check[0]+2, check[1]-1)
            right = (check[0]+2, check[1]+1)

            new_points.append([priority, left])
            new_points.append([priority, right])

        elif c == ".":
            lower = (check[0]+2, check[1])
            new_points.append([priority, lower])

        return new_points

    def part2(self) -> int:
        # count when search  hit the bottom
        start_time = time.time()
        n_rows = len(self.input)
        counter = 0  # count if laser hit a splitter
        queue = []

        data_cache = []
        for i in self.input:
            data_cache.append(tuple(i))
        data_cache = tuple(data_cache)

        for i, c in enumerate(self.input[0]):  # find laser start
            if c == "S":
                heappush(queue, [1, (1, i)])

        loop = 0
        while len(queue) != 0:
            # TODO way to slow. possible cache ?
            _, check = heappop(queue)
            if check[0] >= n_rows-1:
                counter += 1
                continue

            add_queue = self.next_point(data_cache, check)
            for i in add_queue:
                heappush(queue, i)
            loop += 1

            if loop % 5000000 == 0:
                print(
                    f"{round(time.time() - start_time, 2)} [sec], counter {counter}, queue len {len(queue)}")

        return counter


Puzzle7(EXAMPLE)
Puzzle7(INPUT)
# 6421586086 to low part 2
