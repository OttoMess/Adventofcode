import time
import networkx as nx

EXAMPLE = "AoC_inputs/2024/day_18_example.txt"
INPUT = "AoC_inputs/2024/day_18.txt"


class Puzzle18:
    def __init__(self, path, size_map, amount):
        start_time = time.time()

        self.file_path = path
        self.map_size = size_map
        self.amount = amount
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
                x, y = line.strip().split(",")
                data.append((int(x), int(y)))
        self.bytes = data

    def part1and2(self):
        self.clean_memory()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        grid = nx.DiGraph()
        for y, line in enumerate(self.memory):
            for x, _ in enumerate(line):
                node = (y, x)
                for dirs in directions:
                    grid.add_node((node, dirs))

        for node, dirs in grid.nodes:
            # adding edge with weight 1 for each node with same dir are start note
            next_node = (node[0] + dirs[0], node[1] + dirs[1])
            if (next_node, dirs) in grid.nodes:
                grid.add_edge((node, dirs), (next_node, dirs), weight=1)
            # adding the rotation weight
            if dirs[1] == 0:  # moving up and down, switching to left right
                grid.add_edge((node, dirs), (node, (0, 1)), weight=0)
                grid.add_edge((node, dirs), (node, (0, -1)), weight=0)
            elif dirs[0] == 0:  # moving left and right, switching to up down
                grid.add_edge((node, dirs), (node, (1, 0)), weight=0)
                grid.add_edge((node, dirs), (node, (-1, 0)), weight=0)

        start = ((0, 0), (0, 1))
        end = (self.map_size - 1, self.map_size - 1)

        # adding edges for the end point
        for dirs in directions:
            grid.add_edge((end, dirs), "end", weight=0)

        for i in range(len(self.bytes)):
            self.update_memory(self.bytes[i], "#")
            for dirs in directions:
                grid.remove_node((self.bytes[i], dirs))

            if i > self.amount:
                try:
                    w = nx.shortest_path_length(grid, start, "end", weight="weight")
                except:
                    yield self.bytes[i]  # part 2
            elif i == self.amount:
                yield nx.shortest_path_length(
                    grid, start, "end", weight="weight"
                )  # part 1

    def update_memory(self, n, string="%"):  # visual purposes only
        self.memory[n[1]] = (
            self.memory[n[1]][: n[0]] + string + self.memory[n[1]][n[0] + 1 :]
        )

    def clean_memory(self):  # only for visual purposes
        self.memory = list()
        for y in range(self.map_size):
            self.memory.append("".join(["." for i in range(self.map_size)]))


Puzzle18(EXAMPLE, 7, 12)
Puzzle18(INPUT, 71, 1024)
