import time
import networkx as nx
from matplotlib import pyplot as plt
from functools import cache


EXAMPLE = "AoC_inputs/2024/day_21_example.txt"
INPUT = "AoC_inputs/2024/day_21.txt"


"""
(y,X)
7 = (0,0)
A = (3,2)
    x ->
 y  +---+---+---+
 |  | 7 | 8 | 9 |
 V  +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
Start on A
    
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

part 2
97227250560186 to low
107258143797068 to low
112698726110005 wrong
"""


class Puzzle21:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.input = data

    def part1(self):
        num, dirs = self.build_grids()
        # self.plot_nodes(num) # for visuals of the nx grids
        # self.plot_nodes(dirs) # for visuals of the nx grids
        collector = 0
        for line in self.input:
            arm = "A"
            key_1_arm = "A"
            key_2_arm = "A"
            output_1 = list()
            output_2 = list()
            output_num = list()
            for number in line:
                pos_num = nx.shortest_path(num, self.numeric(arm), self.numeric(number))
                num_steps = self.path_to_steps(pos_num, self.num_nodes)
                for step in num_steps:
                    output_num.append(step)

                for dir_1 in num_steps:
                    pos_key_1 = nx.shortest_path(
                        dirs, self.directional(key_1_arm), self.directional(dir_1)
                    )
                    key_1 = self.path_to_steps(pos_key_1, self.dirs_nodes)
                    for step in key_1:
                        output_1.append(step)

                    for dir_2 in key_1:
                        pos_key_2 = nx.shortest_path(
                            dirs, self.directional(key_2_arm), self.directional(dir_2)
                        )
                        key_2 = self.path_to_steps(pos_key_2, self.dirs_nodes)
                        for step in key_2:
                            output_2.append(step)

                        key_2_arm = dir_2

                    key_1_arm = dir_1

                arm = number
            # print(f"{line}: {"".join([i for i in output_2])}")
            collector += len(output_2) * int(line[:-1])
        return collector

    def part2(self):
        num, self.dirs = self.build_grids()
        self.depth = 25
        self.lookup_set()
        # self.plot_nodes(num)
        # self.plot_nodes(dirs)
        collector = 0
        collector_1 = 0
        count = 0
        # find length of operations for each of the 5 options
        options = "<>^vA"
        book = dict()
        for o in options:
            book[o] = self.directional_pad(o, 1, "A")
        for line in self.input:
            arm = "A"
            self.out = list()
            self.length = 0
            count = 0
            for number in line:
                pos_num = nx.shortest_path(num, self.numeric(arm), self.numeric(number))
                num_steps = self.path_to_steps(pos_num, self.num_nodes)

                for step in num_steps:
                    self.length += book[step]

                count += self.directional_pad(num_steps, 1, "A")

                arm = number
            # print(f"{line}: {"".join([i for i in self.out])}")
            # print(line)
            collector_1 += self.length * int(line[:-1])
            collector += count * int(line[:-1])
        return collector

    def lookup_set(self):
        self.lookup = {
            "A<": "v<<A",
            "A^": "<A",
            "A>": "vA",
            "Av": "v<A",
            "<>": ">>A",
            "<^": ">^A",
            "<v": ">A",
            "<A": ">>^A",
            "><": "<<A",
            ">A": "^A",
            ">v": "<A",
            ">^": "<^A",
            "^A": ">A",
            "^>": "v>A",
            "^<": "v<A",
            "^v": "vA",
            "v<": "<A",
            "v>": ">A",
            "v^": "^A",
            "vA": ">^A",
        }
        return self.lookup

    @cache
    def directional_pad(self, path, depth, position):
        if depth == self.depth:
            # for step in path:
            #     self.out.append(step)
            # self.length += len(path)
            return len(path)

        total = 0
        for step in path:
            if step == position:
                sub_path = "A"
            else:
                check = position + step
                sub_path = self.lookup[check]
            length = self.directional_pad(sub_path, depth + 1, "A")
            total += length
            position = step
        return total

    def build_grids(self):
        num = nx.grid_2d_graph(4, 3)
        num.remove_node((3, 0))

        dirs = nx.grid_2d_graph(2, 3)
        dirs.remove_node((0, 0))

        self.num_nodes = set(num.nodes())
        self.dirs_nodes = set(dirs.nodes())

        return num, dirs

    @staticmethod
    def path_to_steps(path, check):
        steps = list()
        for i in range(len(path) - 1):
            steps.append((path[i][0] - path[i + 1][0], path[i][1] - path[i + 1][1]))

        if len(steps) > 1:
            one = sorted(steps)
            two = one[::-1]
            tester = path[0]
            one_valid = True
            for step in one:
                tester = (tester[0] - step[0], tester[1] - step[1])
                if tester not in check:
                    one_valid = False
                    break

            if one_valid:
                steps = one
            else:
                tester = path[0]
                for step in two:
                    tester = (tester[0] - step[0], tester[1] - step[1])
                    if tester not in check:
                        break
                steps = two

        directions = str()
        for e in steps:
            match e:
                case (0, 1):
                    directions += "<"
                case (0, -1):
                    directions += ">"
                case (1, 0):
                    directions += "^"
                case (-1, 0):
                    directions += "v"
        directions += "A"  # need to press button
        return directions

    @staticmethod
    def numeric(key):
        match key:
            case "0":
                return (3, 1)
            case "1":
                return (2, 0)
            case "2":
                return (2, 1)
            case "3":
                return (2, 2)
            case "4":
                return (1, 0)
            case "5":
                return (1, 1)
            case "6":
                return (1, 2)
            case "7":
                return (0, 0)
            case "8":
                return (0, 1)
            case "9":
                return (0, 2)
            case "A":
                return (3, 2)

    @staticmethod
    def directional(key):
        match key:
            case "<":
                return (1, 0)
            case ">":
                return (1, 2)
            case "^":
                return (0, 1)
            case "v":
                return (1, 1)
            case "A":
                return (0, 2)

    @staticmethod
    def plot_nodes(grid):  # for visual purposes and debugging only
        plt.figure(figsize=(6, 6))
        pos = {(x, y): (y, -x) for x, y in grid.nodes()}
        nx.draw(
            grid,
            pos=pos,
            node_color="lightgreen",
            with_labels=True,
            node_size=600,
        )
        plt.show()


def lookup_set():
    lookup = {
        "A<": "v<<A",
        "A^": "<A",
        "A>": "vA",
        "Av": "v<A",
        "<>": ">>A",
        "<^": ">^A",
        "<v": ">A",
        "<A": ">>^A",
        "><": "<<A",
        ">A": "^A",
        ">v": "<A",
        ">^": "<^A",
        "^A": ">A",
        "^>": "v>A",
        "^<": "v<A",
        "^v": "vA",
        "v<": "<A",
        "v>": ">A",
        "v^": "^A",
        "vA": ">^A",
    }
    return lookup


@cache
def directional_pad(path, depth, position, target=25):
    lookup = lookup_set()

    if depth == target:
        # for step in path:
        #     self.out.append(step)
        # self.length += len(path)
        return len(path)

    total = 0
    for step in path:
        if step == position:
            sub_path = "A"
        else:
            check = position + step
            sub_path = lookup[check]
        length = directional_pad(sub_path, depth + 1, "A")
        total += length
        position = step
    return total


Puzzle21(EXAMPLE)
Puzzle21(INPUT)
