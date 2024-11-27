import time
from dataclasses import dataclass
import threading

DATA = "2023/data/day16.txt"
EXAMPLE = "2023/data/day16_example.txt"


@dataclass
class Cell:
    coordinates: list = None
    direction: list = None


class Puzzle16:

    def __init__(self, path):
        self.west_field = list()
        self.south_field = list()
        self.east_field = list()
        self.north_field = list()
        self.status = None
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        self.lookup = {"|": ["up", "down"],
                       "-": ["left", "right"]}

        start_time = time.time()

        self.data = self.read_txt()

        self.part1()
        self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        start_field = [0, 0]
        start_direction = 'right'
        first_reflection = self.mirror(self.data[start_field[0]][start_field[1]], start_direction)
        self.status = [Cell(start_field, first_reflection)]

        for cell in self.status:
            new_cell = self.find_next(cell, self.status)
            [self.status.append(i) for i in new_cell]

        high = self.draw_energised()
        self.part1_collector = self.count_energy(high)

    def part2(self):

        self.build_start_lines()

        # n_thread = threading.Thread(target=self.search_start_line, args=(self.north_field, "north"))
        # s_thread = threading.Thread(target=self.search_start_line, args=(self.south_field, "south"))
        # w_thread = threading.Thread(target=self.search_start_line, args=(self.west_field," west"))
        # e_thread = threading.Thread(target=self.search_start_line, args=(self.east_field, "east"))
        # #
        north = self.search_start_line(self.north_field, "north")
        south = self.search_start_line(self.south_field, "south")
        west = self.search_start_line(self.west_field, "west")
        east = self.search_start_line(self.east_field, "east")
        #
        # n_thread.start()
        # s_thread.start()
        # w_thread.start()
        # e_thread.start()
        #
        # xx = n_thread.join()

        all_lines = list()
        all_lines.extend(north)
        all_lines.extend(south)
        all_lines.extend(east)
        all_lines.extend(west)
        self.part2_collector = max(all_lines)

    def search_start_line(self, start_line, name):
        amount = list()
        for j, start in enumerate(start_line):
            print(f"start position {j+1} of {len(start_line)} of {name}")
            row = start.coordinates[0]
            column = start.coordinates[1]
            direction = start.direction
            first_reflection = self.mirror(self.data[row][column], direction)
            paths = [Cell([row, column], first_reflection)]

            for cell in paths:
                new_cell = self.find_next(cell, paths)
                [paths.append(i) for i in new_cell]

            amount.append(self.amount_energised(paths))

        return amount

    def build_start_lines(self):
        rows = len(self.data)
        columns = len(self.data[0])
        for i in range(rows):
            self.east_field.append(Cell([i, 0], "right"))
            self.west_field.append(Cell([i, columns-1], "up"))
        for i in range(columns):
            self.north_field.append(Cell([0, i], "down"))
            self.south_field.append(Cell([rows - 1, i], "up"))

    @staticmethod
    def reflection_finder(start_list):
        pass

    @staticmethod
    def count_energy(field):
        total = 0
        for i in field:
            total += i.count("#")
        return total

    @staticmethod
    def amount_energised(status):
        cors = [i.coordinates for i in status]
        unique = list()
        for i in cors:
            if i not in unique:
                unique.append(i)
        return len(unique)

    def draw_energised(self):
        energy_field = [["." for _ in self.data[0]] for _ in self.data]

        for cell in self.status:
            row = cell.coordinates[0]
            column = cell.coordinates[1]
            if energy_field[row][column] != "#":
                energy_field[row][column] = "#"

        for line in energy_field:
            print("".join(c for c in line))

        return energy_field

    def find_next(self, element: Cell, status):
        dirs = element.direction
        row = element.coordinates[0]
        column = element.coordinates[1]

        output = list()

        if "right" in dirs and column < len(self.data[0])-1:
            target = self.data[row][column+1]
            new_direction = self.mirror(target, "right")
            new_cell = Cell([row, column+1], new_direction)
            if new_cell not in status:
                output.append(new_cell)

        if "left" in dirs and column > 0:
            target = self.data[row][column-1]
            new_direction = self.mirror(target, "left")
            new_cell = Cell([row, column-1], new_direction)
            if new_cell not in status:
                output.append(new_cell)

        if "up" in dirs and row > 0:
            target = self.data[row-1][column]
            new_direction = self.mirror(target, "up")
            new_cell = Cell([row-1, column], new_direction)
            if new_cell not in status:
                output.append(new_cell)

        if "down" in dirs and row < len(self.data)-1:
            target = self.data[row+1][column]
            new_direction = self.mirror(target, "down")
            new_cell = Cell([row+1, column], new_direction)
            if new_cell not in status:
                output.append(new_cell)

        return output

    @staticmethod
    def mirror(mirror, in_direction):
        if mirror == "/":
            if in_direction == "left":
                outputs = ["down"]
            elif in_direction == "down":
                outputs = ["left"]
            elif in_direction == "right":
                outputs = ["up"]
            elif in_direction == "up":
                outputs = ["right"]

        elif mirror == "\\":
            if in_direction == "left":
                outputs = ["up"]
            elif in_direction == "up":
                outputs = ["left"]
            elif in_direction == "right":
                outputs = ["down"]
            elif in_direction == "down":
                outputs = ["right"]

        elif mirror == "-":
            if in_direction == "up" or in_direction == "down":
                outputs = ["left", "right"]
            else:
                outputs = [in_direction]

        elif mirror == "|":
            if in_direction == "left" or in_direction == "right":
                outputs = ["up", "down"]
            else:
                outputs = [in_direction]

        elif mirror == ".":
            outputs = [in_direction]

        return outputs

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        return raw


# Puzzle16(EXAMPLE)
Puzzle16(DATA)
