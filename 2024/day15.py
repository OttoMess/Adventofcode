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

    def part1(self):
        self.read_txt()
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
        return

    def start_position(self):
        for y, line in enumerate(self.map):
            for x, cha in enumerate(line):
                if cha == "@":
                    return (y, x)

    def move_robot(self, robot, d):
        new_robot = [robot[0] + d[0], robot[1] + d[1]]

        if self.map[new_robot[0]][new_robot[1]] == ".":
            self.update_map(robot, ".")
            self.update_map(new_robot, "@")
            return new_robot

        elif self.map[new_robot[0]][new_robot[1]] == "#":
            return robot

        elif self.map[new_robot[0]][new_robot[1]] == "O":
            movable = self.move_boxes(new_robot, d)
            if movable:
                self.update_map(robot, ".")
                self.update_map(new_robot, "@")
                return new_robot
            else:
                return robot

    def move_boxes(self, box, d):
        new_box = [box[0] + d[0], box[1] + d[1]]

        if self.map[new_box[0]][new_box[1]] == ".":
            self.update_map(box, ".")
            self.update_map(new_box, "O")
            return True

        elif self.map[new_box[0]][new_box[1]] == "#":
            return False

        elif self.map[new_box[0]][new_box[1]] == "O":
            movable = self.move_boxes(new_box, d)
            if movable:
                self.update_map(box, ".")
                self.update_map(new_box, "O")
                return True
            else:
                return False

    def update_map(self, n, string="#"):
        self.map[n[0]] = self.map[n[0]][: n[1]] + string + self.map[n[0]][n[1] + 1 :]


Puzzle15(TEST)
Puzzle15(EXAMPLE)
Puzzle15(INPUT)
