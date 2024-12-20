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
        self.walls = list()
        for wall in walls:
            self.grid.remove_node(wall)
            if 0 < wall[0] < depth and 0 < wall[1] < width:
                self.walls.append(wall)

        # plt.figure(figsize=(6, 6))
        # pos = {(x, y): (y, -x) for x, y in self.grid.nodes()}
        # nx.draw(
        #     self.grid, pos=pos, node_color="lightgreen", with_labels=True, node_size=600
        # )
        # plt.show()
        return

    def part1(self):
        ref = nx.shortest_path(self.grid, self.start, self.end)
        cheat_times = list()
        short_cuts = self.next_to_path(ref)
        for wall in self.walls:
            # TODO only check the wall adjacent to shortest path, are there more than 1 shortest path ?
            edges = self.edge_finder(wall)
            self.grid.add_node(wall)
            self.grid.add_edges_from(edges)
            t = nx.shortest_path_length(self.grid, self.start, self.end)
            if t < len(ref) - 100:
                cheat_times.append((len(ref)) - t)
            self.grid.remove_node(wall)
        return len(cheat_times)

    def part2(self):
        return

    def edge_finder(self, node):
        adjacent: list = list()
        y = node[0]
        x = node[1]
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for step in steps:
            next = (y + step[0], x + step[1])
            if next in self.grid.nodes:
                adjacent.append((node, next))
        return adjacent

    def next_to_path(self, path):
        path = set(path)
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        short_cut = list()
        for wall in self.walls:
            count = 0
            y = wall[0]
            x = wall[1]
            for step in steps:
                next = (y + step[0], x + step[1])
                if next in path:
                    count += 1
            if count >= 2:
                short_cut.append(wall)
        return short_cut

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
