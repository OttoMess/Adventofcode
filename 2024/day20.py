import time
import networkx as nx
from matplotlib import pyplot as plt

EXAMPLE = "AoC_inputs/2024/day_20_example.txt"
INPUT = "AoC_inputs/2024/day_20.txt"


class Puzzle20:
    def __init__(self, path, time_part1: int, time_part2: int):
        start_time = time.time()
        self.file_path = path
        self.time_part1 = time_part1
        self.time_part2 = time_part2
        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        walls = list()
        with open(self.file_path) as file:
            for y, line in enumerate(file):
                depth = y
                for x, char in enumerate(line):
                    width = x
                    if char == "#":
                        walls.append((y, x))
                    elif char == "S":
                        self.start = (y, x)
                    elif char == "E":
                        self.end = (y, x)

        self.grid = nx.grid_2d_graph(depth + 1, width + 1)
        self.inner_walls = list()
        for wall in walls:
            self.grid.remove_node(wall)
            if 0 < wall[0] < depth and 0 < wall[1] < width:
                self.inner_walls.append(wall)
        # only 1 shortest path, all nodes are in the shortest path
        self.ref = nx.shortest_path(self.grid, self.start, self.end)
        return

    def part1(self):
        cheat_times = list()
        lookup = set(self.ref)
        for wall in self.inner_walls:
            possible, next, prev = self.one_wall_short_cut(lookup, wall)
            if possible:
                a = self.ref.index(next)
                b = self.ref.index(prev)
                time_saved = abs(a - b) - 2  # for steps taken in shortcut

                if time_saved >= self.time_part1:
                    cheat_times.append(time_saved)

        return len(cheat_times)

    def part2(self):
        cheat_times = list()
        lookup = set(self.ref)
        options = 0
        for step in self.ref:
            options = self.test_20_cheat(step, lookup)
            a = self.ref.index(step)
            for end, cheat_time in options:
                b = self.ref.index(end)
                #  compensate for time taken for cheat
                time_saved = b - a - cheat_time
                if time_saved >= self.time_part2:
                    cheat_times.append(time_saved)

        return len(cheat_times)

    @staticmethod
    def one_wall_short_cut(path, wall):
        y = wall[0]
        x = wall[1]

        prev = (y + 1, x)
        next = (y + -1, x)
        if next in path and prev in path:
            return True, prev, next

        prev = (y, x - 1)
        next = (y, x + 1)
        if next in path and prev in path:
            return True, prev, next

        return False, None, None

    def plot_nodes(self):  # for visual purposes and debugging only
        plt.figure(figsize=(6, 6))
        pos = {(x, y): (y, -x) for x, y in self.grid.nodes()}
        nx.draw(
            self.grid,
            pos=pos,
            node_color="lightgreen",
            with_labels=True,
            node_size=600,
        )
        plt.show()

    def test_20_cheat(self, point, path):
        collect = list()
        for i in range(-20, 21):
            y = point[0] + i
            e = 20 - abs(i)
            for j in range(-e, e + 1):
                x = point[1] + j
                cheats = abs(i) + abs(j)
                node = (y, x)
                if node in path:
                    collect.append((node, cheats))
        return collect


Puzzle20(EXAMPLE, time_part1=0, time_part2=50)
Puzzle20(INPUT, time_part1=100, time_part2=100)
