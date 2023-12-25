import time
from dataclasses import dataclass
import math
import operator

DATA = "data/day17.txt"
EXAMPLE = "data/day17_example.txt"
TEST = "data/day17_test.txt"


# @dataclass
# class Point:
#     cor: list = None
#     heat_loss: int = None


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

    def dijkstra(self, node_list):
        # node_list = [_ for _ in graph]
        # heat_loss = [math.inf for _ in graph]
        # previous = [None for _ in graph]
        visited = list()
        queue = [_ for _ in node_list]

        node_list[0].heat_lost = 0
        node_list[0].previous = "start"
        # heat_loss[0] = 0
        # previous[0] = "start"
        first = True
        while queue:

            if first:
                new_node = queue[0]
                first = False
            else:
                # new_node, loc_queue = self.next_node(node_list, queue, visited)
                new_node = self.next_node(node_list, queue, visited)

            if not new_node:
                current = queue[0]
            else:
                current = new_node

            loc = node_list.index(current)
            queue.remove(current)
            visited.append(current)
            neighbors = neighbor_search(current, node_list)

            for n in neighbors:
                tentative_heat_loss = node_list[loc].heat_lost + n.heat_loss
                loc_n = node_list.index(n)

                if tentative_heat_loss < node_list[loc_n].heat_lost:
                    node_list[loc_n].heat_lost = tentative_heat_loss
                    node_list[loc_n].previous = loc

        return node_list

    def next_node(self, node_list, queue, visited):
        nodes_heat_sort = sorted(node_list, key=self.get_heat_loss)
        queue_cor = [i.cor for i in queue]

        for j, node in enumerate(nodes_heat_sort):
            if node.heat_lost == math.inf:
                # node = False
                # location = False
                # return node, location
                current = visited[-1]
                break
            if node.cor in queue_cor:
                return node

        neighbors = neighbor_search(current, queue)
        # for neighbor in neighbors:
        #     valid = self.validate_neighbors(current, neighbor, previous)
        #     if not valid:
        #         neighbors.remove(neighbor)

        heat_loss = [i.heat_lost for i in neighbors]
        if len(neighbors) == 0:
            node = False
            location = False
        else:
            node = neighbors[heat_loss.index(min(heat_loss))]
            # location = node_list.index(node)
        # return node, location
        return node
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

    def part1(self):
        self.all_points = self.build_graph(self.data)
        node_list = self.dijkstra(self.all_points)
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


Puzzle17(TEST)
Puzzle17(EXAMPLE)
