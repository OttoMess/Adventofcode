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
        self.clean_memory()  # only for visual purposes

        grid = nx.grid_2d_graph(self.map_size, self.map_size)

        start = (0, 0)
        end = (self.map_size - 1, self.map_size - 1)

        for i in range(len(self.bytes)):
            self.update_memory(self.bytes[i])  # only for visual purposes
            grid.remove_node(self.bytes[i])

            if i > self.amount:
                try:
                    w = nx.shortest_path_length(grid, start, end)
                except:
                    yield self.bytes[i]  # part 2
                    break
            elif i == self.amount - 1:
                yield nx.shortest_path_length(grid, start, end)  # part 1

    def update_memory(self, n, string="#"):  # visual purposes only
        self.memory[n[1]] = (
            self.memory[n[1]][: n[0]] + string + self.memory[n[1]][n[0] + 1 :]
        )

    def clean_memory(self):  # only for visual purposes
        self.memory = list()
        for y in range(self.map_size):
            self.memory.append("".join(["." for i in range(self.map_size)]))


Puzzle18(EXAMPLE, 7, 12)
Puzzle18(INPUT, 71, 1024)
