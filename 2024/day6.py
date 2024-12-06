import time


EXAMPLE = "AoC_inputs/2024/day_6_example.txt"
INPUT = "AoC_inputs/2024/day_6.txt"

"""  x ->
y      1 2 3
|    1   
V    2
     3
"""


class Puzzle6:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()
        self.visited = list()

        self.steps = (-1, 0), (0, 1), (1, 0), (0, -1)

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

    def find_guard(self):
        for y, line in enumerate(self.input):
            for x, _ in enumerate(line):
                if self.input[y][x] == "^":
                    return (y, x)

    def part1(self):
        visited = list()
        visited.append(self.find_guard())
        x = visited[0][1]
        y = visited[0][0]
        way = 0
        while True:
            x += self.steps[way][1]
            y += self.steps[way][0]
            if 0 <= x <= (len(self.input[0]) - 1) and 0 <= y <= (len(self.input) - 1):
                if self.input[y][x] == "#":
                    x -= self.steps[way][1]
                    y -= self.steps[way][0]
                    way = (way + 1) % 4
                elif (y, x) not in visited:  # prevent doubles of same location
                    visited.append((y, x))
            else:
                break

        self.visited = visited
        return len(visited)

    def part2(self):
        valid_obstacle = list()
        printer = 0
        loop_time = time.time()
        for loc in self.visited[1:]:
            if self.is_loop(loc):
                valid_obstacle.append(loc)

            printer += 1
            if printer % 500 == 0:
                print(
                    f"{printer} of {len(self.visited)} done.  {round(time.time() - loop_time, 4)} [sec] last 500 "
                )
                loop_time = time.time()
        return len(valid_obstacle)

    def is_loop(self, obstacle):
        visited = list()
        x = self.visited[0][1]
        y = self.visited[0][0]
        way = 0
        while True:
            x_next = x + self.steps[way][1]
            y_next = y + self.steps[way][0]
            if 0 <= x_next <= (len(self.input[0]) - 1) and 0 <= y_next <= (
                len(self.input) - 1
            ):
                if (
                    x_next == obstacle[1]
                    and y_next == obstacle[0]
                    or self.input[y_next][x_next] == "#"
                ):
                    visited.append((y, x, self.steps[way]))
                    way = (way + 1) % 4
                else:
                    if (y_next, x_next, self.steps[way]) in visited:
                        return True

                    x = x_next
                    y = y_next
            else:
                return False


Puzzle6(EXAMPLE)
Puzzle6(INPUT)
