import time
import networkx as nx
from matplotlib import pyplot as plt
from collections import Counter

EXAMPLE = "AoC_inputs/2024/day_20_example.txt"
INPUT = "AoC_inputs/2024/day_20.txt"


class Puzzle20:
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
        return

    def part1(self):
        ref = nx.shortest_path(self.grid, self.start, self.end)  # only 1 shortest path
        cheat_times = list()
        lookup = set(ref)
        for wall in self.inner_walls:
            possible, next, prev = self.short_cut_possible(lookup, wall)
            if possible:
                a = ref.index(next)
                b = ref.index(prev)
                time_saved = abs(a - b) - 2  # for steps taken in shortcut

                if time_saved >= 100:
                    cheat_times.append(time_saved)

        return len(cheat_times)

    def part2(self):
        return

    @staticmethod
    def short_cut_possible(path, wall):
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

    def plot_nodes(self):
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


# Puzzle20(EXAMPLE)
Puzzle20(INPUT)
