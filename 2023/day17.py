import time
from dataclasses import dataclass
import math
# import operator

DATA = "data/day17.txt"
EXAMPLE = "data/day17_example.txt"
TEST = "data/day17_test.txt"


@dataclass
class Node:
    # distance: int = math.inf
    previous: list = None
    heat_lost: int = math.inf
    cor: list = None
    heat_loss: int = None


class Puzzle17:

    def __init__(self, path):

        self.all_points = None
        self.grid_row = None
        self.grid_col = None
        self.file_path = path
        self.data = list()

        self.part1_collector = int
        self.part2_collector = 0

        start_time = time.time()

        self.read_txt()

        self.part1()
        # self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    @staticmethod
    def get_heat_loss(node):
        return node.heat_lost

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        self.grid_col = len(raw[0])
        self.grid_row = len(raw)
        self.data = raw

    def draw_path(self, node_list):
        grid = [["." for _ in range(self.grid_col)] for _ in range(self.grid_row)]
        end_index = node_list.index(node_list[-1])
        step = end_index
        path = list()
        while step != "start":
            path.append(step)
            step = node_list[step].previous

        for step in path:
            row = node_list[step].cor[0]
            col = node_list[step].cor[1]
            grid[row][col] = "#"

        for line in grid:
            print("".join(i for i in line))

    @staticmethod
    def build_graph(data):
        all_points = list()
        for j, line in enumerate(data):
            for k, c in enumerate(line):
                all_points.append(Node(cor=[j, k], heat_loss=int(data[j][k])))
        return all_points

    def dijkstra(self, node_list, target: list):
        visited = list()
        queue = [_ for _ in node_list]

        node_list[0].heat_lost = 0
        node_list[0].previous = "start"

        while queue:
            queue.sort(key=self.get_heat_loss)
            current = queue[0]
            queue.remove(current)

            if current.cor == target:
                for node in node_list:
                    if node.previous is None:
                        node_list.remove(node)
                return node_list

            loc = node_list.index(current)
            visited.append(current)

            neighbors = neighbor_search(current, node_list)
            for n in neighbors:  # check if the neighbors are not 3 in a row
                valid = self.validate_neighbors(current, n, node_list)
                if not valid:
                    neighbors.remove(n)

            for n in neighbors:
                tentative_heat_loss = node_list[loc].heat_lost + n.heat_loss
                loc_n = node_list.index(n)

                if tentative_heat_loss < node_list[loc_n].heat_lost:
                    node_list[loc_n].heat_lost = tentative_heat_loss
                    node_list[loc_n].previous = loc
                    if n in queue:
                        pos = queue.index(n)
                        queue[pos].heat_loss = tentative_heat_loss
                        queue[pos].previous = loc

        return node_list

    @staticmethod
    def validate_neighbors(current, neighbor, node_list):
        step = node_list.index(current)
        path = list()
        k = 0
        while step != "start" and k < 4:
            path.append(step)
            step = node_list[step].previous
            k += 1

        if len(path) < 4:
            return True

        # todo does not work need to be fixed better way to find if 3 in a row
        n_row = neighbor.cor[0]
        n_col = neighbor.cor[1]

        p0_row = node_list[path[0]].cor[0]
        p1_row = node_list[path[1]].cor[0]
        p2_row = node_list[path[2]].cor[0]
        p3_row = node_list[path[3]].cor[0]

        p0_col = node_list[path[0]].cor[1]
        p1_col = node_list[path[1]].cor[1]
        p2_col = node_list[path[2]].cor[1]
        p3_col = node_list[path[3]].cor[1]

        if p0_row == p1_row == p2_row == p3_row == n_row:
            return False
        elif p0_col == p1_col == p2_col == p3_col == n_col:
            return False
        else:
            return True

    def part1(self):
        self.all_points = self.build_graph(self.data)
        node_list = self.dijkstra(self.all_points, self.all_points[-1].cor)
        self.part1_collector = node_list[-1].heat_lost
        self.draw_path(node_list)
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


# Puzzle17(TEST)
Puzzle17(EXAMPLE)
