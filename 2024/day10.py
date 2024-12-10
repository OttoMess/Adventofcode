import time
from heapq import heappush, heappop

TEST = "AoC_inputs/2024/day_10_test.txt"
EXAMPLE = "AoC_inputs/2024/day_10_example.txt"
INPUT = "AoC_inputs/2024/day_10.txt"


class Puzzle10:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()
        self.find_level_ground()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.input = data

    def part1(self):
        trails = 0
        queue = list()
        for start in self.starts:
            tops_reached = 0
            heappush(queue, start)
            visited = set()

            while len(queue) > 0:
                loc = heappop(queue)
                visited.add(loc)

                if self.input[loc[0]][loc[1]] == "9":
                    tops_reached += 1

                options = self.adjacent(loc)
                if len(options) > 0:
                    for option in options:
                        if option not in visited:
                            heappush(queue, option)
            trails += tops_reached
        return trails

    def part2(self):
        trails = 0
        queue = list()
        priority = 0  # lower is better
        while len(self.starts) > 0:
            start = self.starts.pop(0)
            map_view = self.clean_map()  # for vitalization only
            tops_reached = 0
            heappush(queue, (priority, start))
            visited = set()

            while len(queue) > 0:
                loc = heappop(queue)
                map_view = self.update_map(map_view, loc[1])  # for vitalization only
                priority += 1  # TODO might work find without any priority
                visited.add(loc[1])

                if self.input[loc[1][0]][loc[1][1]] == "9":
                    tops_reached += 1

                """adding secondary option(s) to start list.
                each split will search to "9" """
                options = self.adjacent(loc[1])
                if len(options) > 0:
                    for p, option in enumerate(options):
                        if option not in visited and p == 0:
                            heappush(queue, (priority, option))
                        else:
                            self.starts.append(option)

            trails += tops_reached
        return trails

    def find_level_ground(self):
        starts = list()
        for y, line in enumerate(self.input):
            for x, height in enumerate(line):
                if height == "0":
                    starts.append((y, x))
        self.starts = starts

    def in_grid(self, point):
        if 0 <= point[0] < self.y_lim and 0 <= point[1] < self.x_lim:
            return True
        return False

    def clean_map(self):  # only for visual purposes
        duplicate = list()
        for line in self.input:
            duplicate.append("".join(["." for i in line]))
        return duplicate

    def adjacent(self, cor):
        adjacent = list()
        y = cor[0]
        x = cor[1]
        start_height = int(self.input[y][x])
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for step in steps:
            next = (y + step[0], x + step[1])
            if (
                self.in_grid(next) and self.input[next[0]][next[1]] == "."
            ):  # only for test file
                continue
            elif (
                self.in_grid(next)
                and int(self.input[next[0]][next[1]]) == start_height + 1
            ):
                adjacent.append(next)

        return adjacent

    @staticmethod
    def update_map(maps, node, string="#"):  # only for visual purposes
        maps[node[0]] = maps[node[0]][: node[1]] + string + maps[node[0]][node[1] + 1 :]
        return maps


Puzzle10(TEST)
Puzzle10(EXAMPLE)
Puzzle10(INPUT)
