import time
from heapq import heappush, heappop

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
        # count if laser hit a splitter
        n_rows = len(self.input)

        counter = 0
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

    def part2(self) -> int:
        return 0


Puzzle7(EXAMPLE)
Puzzle7(INPUT)
