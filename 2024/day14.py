import time


EXAMPLE = "AoC_inputs/2024/day_14_example.txt"
INPUT = "AoC_inputs/2024/day_14.txt"

""" 
mapping used for the coordinates
     x ->
y      0 1 2
|    0 . . . 
V    1 . . .
     2 . . .
So get x,y point from data[y][x]
input is [x,y]


quadrants 

one   |  two
------------
three |  four

"""


class Puzzle14:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                temp = line.split()
                pos = [int(i) for i in temp[0][2:].split(",")]  # [2:] cut p= and v=
                vel = [int(i) for i in temp[1][2:].split(",")]
                data.append({"pos": pos, "vel": vel})
        self.input = data

    def part1(self):
        width = 101
        height = 103
        quadrants = {"one": list(), "two": list(), "three": list(), "four": list()}
        mid = [(width - 1) // 2, (height - 1) // 2]

        for robot in self.input:
            next = robot["pos"]
            x_vel = robot["vel"][0]
            y_vel = robot["vel"][1]
            for _ in range(100):
                next = [(next[0] + x_vel) % width, (next[1] + y_vel) % height]

            if next[0] < mid[0] and next[1] < mid[1]:
                quadrants["one"].append(next)
            elif next[0] > mid[0] and next[1] < mid[1]:
                quadrants["two"].append(next)
            elif next[0] < mid[0] and next[1] > mid[1]:
                quadrants["three"].append(next)
            elif next[0] > mid[0] and next[1] > mid[1]:
                quadrants["four"].append(next)

        counter = 1
        for key in quadrants.keys():
            counter *= len(quadrants[key])

        return counter

    def part2(self):
        width = 101
        height = 103
        robots = [i for i in self.input]
        j = 0
        while True:
            for robot in robots:
                start = robot["pos"]
                x_vel = robot["vel"][0]
                y_vel = robot["vel"][1]
                robot["pos"] = [(start[0] + x_vel) % width, (start[1] + y_vel) % height]
            j += 1
            block = self.check_9block(robots)
            if block:
                self.print_map(robots)
                # stopper = input(f"step {j} continue ? ")
                # if stopper == "n":
                break
        return j

    def print_map(self, robots):
        view = self.clean_map(101, 103)
        for robot in robots:
            self.update_map(view, robot["pos"])
        for line in view:
            print(line)
        print()

    def check_9block(self, robots):
        pos = [i["pos"] for i in robots]
        for p in pos:
            if [p[0] + 1, p[1] + 1] not in pos:
                continue
            elif [p[0], p[1] + 1] not in pos:
                continue
            elif [p[0] + 1, p[1]] not in pos:
                continue
            elif [p[0] - 1, p[1]] not in pos:
                continue
            elif [p[0], p[1] - 1] not in pos:
                continue
            elif [p[0] - 1, p[1] - 1] not in pos:
                continue
            elif [p[0] + 1, p[1] - 1] not in pos:
                continue
            elif [p[0] - 1, p[1] + 1] not in pos:
                return True
        return False

    @staticmethod
    def clean_map(width, height):  # only for visual purposes
        duplicate = list()
        for i in range(height):
            duplicate.append("".join(["." for i in range(width)]))
        return duplicate

    @staticmethod
    def update_map(maps, node, string="#"):  # only for visual purposes
        maps[node[1]] = maps[node[1]][: node[0]] + string + maps[node[1]][node[0] + 1 :]
        return maps

    # @staticmethod
    # def in_grid(point, x_lim, y_lim):
    #     if 0 <= point[1] < y_lim and 0 <= point[0] < x_lim:
    #         return True
    #     return False


# Puzzle14(EXAMPLE)
Puzzle14(INPUT)
