import time
from heapq import heappush, heappop

EXAMPLE = "AoC_inputs/2024/day_16_example.txt"
INPUT = "AoC_inputs/2024/day_16.txt"


""" 
mapping used for the coordinates
     x ->
y      0 1 2
|    0 . . . 
V    1 . . .
     2 . . .
So get x,y point from data[y][x]
input is [x,y]
"""
# https://www.reddit.com/r/adventofcode/comments/1hfhgl1/2024_day_16_part_1_alternate_test_case/


class Puzzle16:
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
        self.map = data

    def part1(self):
        start = self.find_position("S")
        end = self.find_position("E")

        paths = self.node_list()

        queue = list()
        heappush(queue, (1, start, (0, 1)))
        visited = set()
        first = True

        while len(queue) > 0:
            node = heappop(queue)
            visited.add(node[1])
            self.update_map(node[1])
            if first:
                paths[node[1]] = [0, (0, 0)]
                first = False
            # if node[1] == (9, 2):
            #     print("e")
            # BUG 105512 to high off by 4 .. ?

            neighbors = self.adjacent(node[1])
            for n in neighbors:  # BUG not updating value for sites visited
                # if n[0] == (2, 4):
                #     print("break")
                if (
                    paths[node[1]][1][0] - n[1][0] == node[1][0]
                    and paths[node[1]][1][1] - n[1][1] == node[1][1]
                ):
                    if paths[node[1]][0] + 1 < paths[n[0]][0]:
                        paths[n[0]][0] = paths[node[1]][0] + 1
                        paths[n[0]][1] = node[1]
                else:
                    if paths[node[1]][0] + 1001 < paths[n[0]][0]:
                        paths[n[0]][0] = paths[node[1]][0] + 1001
                        paths[n[0]][1] = node[1]

                if n[0] not in visited:
                    heappush(
                        queue, (paths[n[0]], n[0], n[1])
                    )  # not updated if new lower path is found
            if node[1] == end:
                break

        return paths[end]

    def part2(self):
        return

    def find_position(self, char: str):
        for y, line in enumerate(self.map):
            for x, cha in enumerate(line):
                if cha == char:
                    return (y, x)

    def adjacent(self, cor):
        adjacent: list = list()
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for step in steps:
            next = (cor[0] + step[0], cor[1] + step[1])
            if self.map[next[0]][next[1]] != "#":
                adjacent.append((next, step))
        return adjacent

    def update_map(self, n, string="%"):
        self.map[n[0]] = self.map[n[0]][: n[1]] + string + self.map[n[0]][n[1] + 1 :]

    def node_list(self):
        nodes = dict()
        for y, line in enumerate(self.map):
            for x, char in enumerate(line):
                if char != "#":
                    nodes[(y, x)] = [int(1e18), (-1, -1)]
        return nodes


Puzzle16(EXAMPLE)
Puzzle16(INPUT)
