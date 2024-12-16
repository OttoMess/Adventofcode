import time
import networkx as nx

EXAMPLE = "AoC_inputs/2024/day_16_example.txt"
INPUT = "AoC_inputs/2024/day_16.txt"


class Puzzle161:
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
        self.map = data

    def part1and2(self):
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        grid = nx.DiGraph()

        for y, line in enumerate(self.map):
            for x, char in enumerate(line):
                if char == "#":
                    continue
                node = (y, x)
                if char == "S":
                    start = (node, (0, 1))
                if char == "E":
                    end = node
                # node for each point and direction
                for dirs in directions:
                    grid.add_node((node, dirs))

        for node, dirs in grid.nodes:
            # adding edge with weight 1 for each node with same dir are start note
            next_node = (node[0] + dirs[0], node[1] + dirs[1])
            if (next_node, dirs) in grid.nodes:
                grid.add_edge((node, dirs), (next_node, dirs), weight=1)

            # adding the rotation weight
            if dirs[1] == 0:  # moving up and down, switching to left right
                grid.add_edge((node, dirs), (node, (0, 1)), weight=1000)
                grid.add_edge((node, dirs), (node, (0, -1)), weight=1000)
            elif dirs[0] == 0:  # moving left and right, switching to up down
                grid.add_edge((node, dirs), (node, (1, 0)), weight=1000)
                grid.add_edge((node, dirs), (node, (-1, 0)), weight=1000)

        # adding edges for the end point
        for dirs in directions:
            grid.add_edge((end, dirs), "end", weight=0)

        yield nx.shortest_path_length(grid, start, "end", weight="weight")

        paths = [p for p in nx.all_shortest_paths(grid, start, "end", weight="weight")]

        single = list()
        for path in paths:
            for node in path:
                single.append(node[0])
        unique = set(single)
        yield len(unique) - 1  # remove the last point


Puzzle161(EXAMPLE)
Puzzle161(INPUT)
