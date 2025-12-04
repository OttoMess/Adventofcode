import time


EXAMPLE = "AoC_inputs/2025/day_4_example.txt"
INPUT = "AoC_inputs/2025/day_4.txt"

""" 
mapping used for the coordinates
     x -> row
y      0 1 2
|    0 . . . 
V    1 . . .
     2 . . .
column     
So get x,y point from data[y][x]
input is [x,y]
"""


class Puzzle4:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        self.adjacent = ((1, 0), (-1, 0), (0, 1), (0, -1),
                         (-1, -1), (1, 1), (-1, 1), (1, -1))

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.input = data

    def check_adjacent(self, x, y):
        paper = 0
        for adjacent in self.adjacent:
            check_x = x - adjacent[0]
            check_y = y - adjacent[1]

            if check_x < 0 or check_y < 0:
                continue
            if check_x >= 10 or check_y >= 10:
                continue
            elif self.input[check_y][check_x] == "@":
                paper += 1

        if paper < 4:
            return False

        return True

    def part1(self):
        counter = 0
        for y, row in enumerate(self.input):
            for x, slot in enumerate(row):
                if slot == ".":
                    continue
                else:
                    movable = self.check_adjacent(x, y)
                    if movable:
                        print(x, y)
                        counter += 1
        return counter

    def part2(self):
        return


Puzzle4(EXAMPLE)
# Puzzle4(INPUT)
