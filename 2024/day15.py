import time

TEST = "AoC_inputs/2024/day_15_test.txt"
EXAMPLE = "AoC_inputs/2024/day_15_example.txt"
INPUT = "AoC_inputs/2024/day_15.txt"


class Puzzle15:
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
        moves = list()
        with open(self.file_path) as file:
            for line in file:
                if "#" in line:
                    data.append(line.strip())
                else:
                    moves.append(line.strip())
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.moves = "".join([i for i in moves])
        self.map = data
        self.wide_map = self.double_width()

    def part1(self):
        robot = self.start_position()
        for move in self.moves:
            if move == "<":
                d = (0, -1)
            elif move == "^":
                d = (-1, 0)
            elif move == ">":
                d = (0, 1)
            elif move == "v":
                d = (1, 0)

            robot = self.move_robot(robot, d)

        counter = 0
        for y, line in enumerate(self.map):
            for x, cha in enumerate(line):
                if cha == "O":
                    counter += y * 100 + x
        return counter

    def part2(self):
        self.map = self.wide_map
        robot = self.start_position()
        for move in self.moves:
            if move == "<":
                d = (0, -1)
            elif move == "^":
                d = (-1, 0)
            elif move == ">":
                d = (0, 1)
            elif move == "v":
                d = (1, 0)

            robot = self.move_robot(robot, d)

        counter = 0
        for y, line in enumerate(self.map):
            for x, cha in enumerate(line):
                if cha == "[":
                    counter += y * 100 + x
        return counter

    def start_position(self):
        for y, line in enumerate(self.map):
            for x, cha in enumerate(line):
                if cha == "@":
                    return (y, x)

    def move_robot(self, robot, d):
        new_robot = [robot[0] + d[0], robot[1] + d[1]]
        tester = self.map[new_robot[0]][new_robot[1]]

        box_markers = {"[", "]"}
        sideways = {(0, 1), (0, -1)}

        if tester == ".":
            self.update_map(robot)
            self.update_map(new_robot, "@")
            return new_robot

        elif tester == "#":
            return robot

        elif tester == "O" or tester in box_markers and d in sideways:
            movable = self.move_boxes(new_robot, d)
            if movable:
                self.update_map(robot)
                self.update_map(new_robot, "@")
                return new_robot
            else:
                return robot

        elif tester in box_markers and d not in sideways:
            movable = self.check_wide_box_movable(new_robot, d)
            if movable:
                self.move_wide_boxes_up_down(new_robot, d)
                self.update_map(robot)
                self.update_map(new_robot, "@")
                return new_robot
            else:
                return robot

    def move_boxes(self, box, d):
        box_marker = self.map[box[0]][box[1]]
        new_box = [box[0] + d[0], box[1] + d[1]]
        tester = self.map[new_box[0]][new_box[1]]

        if tester == ".":
            self.update_map(box)
            self.update_map(new_box, box_marker)
            return True

        elif tester == "#":
            return False

        else:
            movable = self.move_boxes(new_box, d)
            if movable:
                self.update_map(box)
                self.update_map(new_box, box_marker)
                return True
            else:
                return False

    def update_map(self, n, string="."):
        self.map[n[0]] = self.map[n[0]][: n[1]] + string + self.map[n[0]][n[1] + 1 :]

    def double_width(self):
        wide_map = list()
        for y, line in enumerate(self.map):
            wide_map.append("")
            for cha in line:
                if cha == "@":
                    wide_map[y] += "@."
                elif cha == "#":
                    wide_map[y] += "##"
                elif cha == "O":
                    wide_map[y] += "[]"
                elif cha == ".":
                    wide_map[y] += ".."
        return wide_map

    def move_wide_boxes_up_down(self, box, d):
        node = self.map[box[0]][box[1]]
        new_one = [box[0] + d[0], box[1] + d[1]]
        move = [box[0] - d[0], box[1] - d[1]]
        move_char = self.map[move[0]][move[1]]
        if node == "]":
            two = [box[0], box[1] - 1]
            new_two = [two[0] + d[0], two[1] + d[1]]
            two_char = "["
        elif node == "[":
            two = [box[0], box[1] + 1]
            new_two = [two[0] + d[0], two[1] + d[1]]
            two_char = "]"

        elif node == ".":
            return

        self.move_wide_boxes_up_down(new_one, d)
        self.move_wide_boxes_up_down(new_two, d)

        self.update_map(box)
        self.update_map(new_one, node)

        self.update_map(two)
        self.update_map(new_two, two_char)
        return

    def check_wide_box_movable(self, box, d):
        node = self.map[box[0]][box[1]]
        new_one = [box[0] + d[0], box[1] + d[1]]

        if node == "]":
            two = [box[0], box[1] - 1]
            new_two = [two[0] + d[0], two[1] + d[1]]
        elif node == "[":
            two = [box[0], box[1] + 1]
            new_two = [two[0] + d[0], two[1] + d[1]]

        elif node == ".":
            return True

        elif node == "#":
            return False

        one_check = self.check_wide_box_movable(new_one, d)
        two_check = self.check_wide_box_movable(new_two, d)
        if one_check and two_check:
            return True
        else:
            return False


# Puzzle15(TEST)
Puzzle15(EXAMPLE)
Puzzle15(INPUT)
