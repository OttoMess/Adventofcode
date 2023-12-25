import time
from dataclasses import dataclass
import math

DATA = "data/day17.txt"
EXAMPLE = "data/day17_example.txt"
TEST = "data/day17_test.txt"


@dataclass
class Point:
    cor: list = None
    heat_loss: int = None


class Puzzle17:

    def __init__(self, path):

        self.all_points = None
        self.grid_row = None
        self.grid_col = None
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.read_txt()

        self.part1()
        # self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        self.grid_col = len(raw[0])
        self.grid_row = len(raw)
        self.data = raw

    def draw_path(self, previous, graph):
        grid = [["." for _ in range(self.grid_col)] for _ in range(self.grid_row)]
        end_index = graph.index(graph[-1])
        step = end_index
        path = list()
        while step != "start":
            path.append(step)
            step = previous[step]

        for step in path:
            row = graph[step].cor[0]
            col = graph[step].cor[1]
            grid[row][col] = "#"

        for line in grid:
            print("".join(i for i in line))

    @staticmethod
    def build_graph(data):
        all_points = list()
        for j, line in enumerate(data):
            for k, c in enumerate(line):
                all_points.append(Point([j, k], int(data[j][k])))
        return all_points

    def dijkstra(self, graph):
        distances = [math.inf for _ in graph]
        previous = [None for _ in graph]
        visited = list()
        queue = [i for i in graph]

        distances[0] = 0
        previous[0] = "start"
        first = True
        while queue:

            if first:
                new_node = queue[0]
                first = False
            else:
                new_node, loc_queue = self.lowest_heat_neighbor(current, queue, previous)

            if not new_node:
                current = queue[0]
            else:
                current = new_node

            loc = graph.index(current)
            queue.remove(current)
            visited.append(current)
            neighbors = neighbor_search(current, graph)

            for n in neighbors:
                tentative_distance = distances[loc] + n.heat_loss
                loc_n = graph.index(n)

                if tentative_distance < distances[loc_n]:
                    distances[loc_n] = tentative_distance
                    previous[loc_n] = loc

        return distances, previous

    def lowest_heat_neighbor(self, current, queue, previous):
        neighbors = neighbor_search(current, queue)
        for neighbor in neighbors:
            valid = self.validate_neighbors(current, neighbor, previous)
            if not valid:
                neighbors.remove(neighbor)

        heat_loss = [i.heat_loss for i in neighbors]
        if len(neighbors) == 0:
            node = False
            location = False
        else:
            node = neighbors[heat_loss.index(min(heat_loss))]
            location = queue.index(node)
        return node, location

    def validate_neighbors(self, current, neighbor, previous):
        # todo check if last 3 steps where not in line
        step = self.all_points.index(current)
        path = list()
        k = 0
        while step != "start" and k < 3:
            path.append(step)
            step = previous[step]
            k += 1

        if len(path) < 3:
            return True
        row = neighbor.cor[0]
        col = neighbor.cor[1]



        # return valid


    def part1(self):
        self.all_points = self.build_graph(self.data)
        heat_loss, previous = self.dijkstra(self.all_points)
        self.part1_collector = heat_loss[-1]
        self.draw_path(previous, self.all_points)
        pass

    def part2(self):
        pass


def neighbor_search(current, graph):
    row = current.cor[0]
    col = current.cor[1]

    output = list()

    for i in graph:
        if i.cor[0] == row + 1 and i.cor[1] == col:
            output.append(i)
        elif i.cor[0] == row - 1 and i.cor[1] == col:
            output.append(i)
        elif i.cor[1] == col + 1 and i.cor[0] == row:
            output.append(i)
        elif i.cor[1] == col - 1 and i.cor[0] == row:
            output.append(i)

        if len(output) == 4:
            return output

    return output





Puzzle17(TEST)
Puzzle17(EXAMPLE)
