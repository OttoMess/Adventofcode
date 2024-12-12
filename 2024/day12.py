import time
from dataclasses import dataclass

TEST = "AoC_inputs/2024/day_12_test.txt"
EXAMPLE = "AoC_inputs/2024/day_12_example.txt"
INPUT = "AoC_inputs/2024/day_12.txt"

""" 
mapping used for the coordinates
     x ->
y      0 1 2
|    0 . . . 
V    1 . . .
     2 . . .
So get x,y point from data[y][x]
"""


class Puzzle12:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        answer = self.part1and2()
        print(f"output part one: {next(answer)}")
        print(f"output part two: {next(answer)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.input = data

    def part1and2(self):
        queue = list()
        plots = list()
        # starting queue with all nodes in the map
        for y, line in enumerate(self.input):
            for x, _ in enumerate(line):
                queue.append((y, x))

        while len(queue) > 0:
            focus = queue[0]
            crop: str = self.input[focus[0]][focus[1]]
            sub_queue = [focus]
            fences_total: int = 0
            field: set = set()  # field with all the same crop
            field.add(focus)
            # making sub queue, to find nodes with same crop. The total field
            while len(sub_queue) > 0:
                sub_focus = sub_queue.pop()
                neighbors, fences = self.adjacent(sub_focus, crop)
                fences_total += fences

                for n in neighbors:
                    if n not in field:
                        sub_queue.append(n)
                        field.add(n)

            plots.append((field, fences_total, crop))
            [queue.remove(f) for f in field]  # nodes in crop field should be removed

        yield sum([i[1] * len(i[0]) for i in plots])

        fences_bulk = 0
        for plot in plots:
            fences_bulk += self.find_corners(plot)

        yield fences_bulk

    def in_grid(self, point: tuple):
        if 0 <= point[0] < self.y_lim and 0 <= point[1] < self.x_lim:
            return True
        return False

    def adjacent(self, cor: tuple, cha: str):
        adjacent: list = list()
        y = cor[0]
        x = cor[1]
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for step in steps:
            next = (y + step[0], x + step[1])
            if self.in_grid(next) and self.input[next[0]][next[1]] == cha:
                adjacent.append(next)
        # fences needed inverse of number of adjacent fields
        fences: int = 4 - len(adjacent)
        return adjacent, fences

    def bulk_discount(self, plot):  # BUG does not work
        steps = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 0))  # clockwise search
        directions = ("up", "right", "down", "left", "up")
        fences = plot[1]
        queue = self.find_a_left_top_corner(plot)
        # previous = None
        visited = set()
        while len(queue) > 0:
            node = queue.pop()
            y = node[0]
            x = node[1]
            for i in range(1, len(steps)):
                next = (y + steps[i][0], x + steps[i][1])
                check = (y + steps[i - 1][0], x + steps[i - 1][1])
                if (
                    next in plot[0]
                    and check not in plot[0]
                    and (next, directions[i]) not in visited
                ):
                    queue.append(next)
                    visited.add((next, directions[i]))
                    # previous = node
                    break
        bulk = (fences - len(visited)) * len(plot[0])
        return bulk

    def find_corners(self, plot):
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        sides = 0
        outside_corner = [
            {(0, 1), (1, 0)},
            {(1, 0), (0, -1)},
            {(0, -1), (-1, 0)},
            {(0, 1), (-1, 0)},
        ]

        inside_corner = [
            ((0, -1), (1, -1), (1, 0)),
            ((1, 0), (1, 1), (0, 1)),
            ((0, 1), (-1, 1), (-1, 0)),
            ((-1, 0), (-1, -1), (0, -1)),
        ]

        for node in plot[0]:
            # check if outward point
            matches = set()

            for step in steps:
                next = (node[0] + step[0], node[1] + step[1])
                if next in plot[0]:
                    matches.add(step)
            if len(matches) == 1:
                sides += 2
            elif len(matches) == 0:
                sides += 4
            elif matches in outside_corner:
                sides += 1
            for corner in inside_corner:
                # inside = list()
                one = (node[0] + corner[0][0], node[1] + corner[0][1])
                two = (node[0] + corner[1][0], node[1] + corner[1][1])
                three = (node[0] + corner[2][0], node[1] + corner[2][1])
                if one in plot[0] and two in plot[0] and three not in plot[0]:
                    sides += 1

        return sides * len(plot[0])

    @staticmethod
    def find_a_left_top_corner(plot):
        steps = ((0, -1), (-1, 0))
        queue = [list(plot[0])[0]]
        while len(queue) > 0:
            node = queue.pop()
            for step in steps:
                next = (node[0] + step[0], node[1] + step[1])
                if next in plot[0]:
                    queue.append(next)
                    break
        return [node]

    @dataclass
    class plot:
        symbol: str
        coordinates: list


# Puzzle12(EXAMPLE)
Puzzle12(TEST)
Puzzle12(INPUT)
