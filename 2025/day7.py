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

    def part2(self) -> int:
        """
        count when search  hit the bottom
        .......S.......
        .......|.......
        ......1^1......
        ......|.|......
        .....1^2^1.....
        .....|.|.|.....
        ....1^3^3^1....
        ...............

        From above example below the point are given with there values
        The number is a sum of possible parts at higher level 

                    1|
                1|      1|
            1|      2|      1|
        1|      3|      3|      1|

        using dict to collect the possible path to that point
        added new element and adding n path of above point to already exciting element in dict.
        key is the location in tuple(column,row)
        value in the dict is the number of path to that location

        working with search tree. Tried heapq but since this approach there is a need to alter elements in 
        the queue this did not work. 
        """
        n_rows = len(self.input)
        counter = 0
        queue = {}

        # find laser start
        for i, c in enumerate(self.input[0]):
            if c == "S":
                queue[(1, i)] = 1

        while len(queue) != 0:
            check = next(iter(queue))
            n = queue[check]
            del queue[check]

            if check[0] >= n_rows-1:
                counter += n
                continue

            c = self.input[check[0] + 1][check[1]]
            if c == "^":
                left = (check[0]+2, check[1]-1)
                right = (check[0]+2, check[1]+1)

                if left not in queue:
                    queue[left] = n
                else:
                    queue[left] += n

                if right not in queue:
                    queue[right] = n
                else:
                    queue[right] += n

            elif c == ".":
                lower = (check[0]+2, check[1])
                if lower not in queue:
                    queue[lower] = n
                else:
                    queue[lower] += n

        return counter


Puzzle7(EXAMPLE)
Puzzle7(INPUT)
