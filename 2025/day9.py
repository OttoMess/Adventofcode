import time
import itertools

EXAMPLE = "AoC_inputs/2025/day_9_example.txt"
INPUT = "AoC_inputs/2025/day_9.txt"


class Puzzle9:
    def __init__(self, path) -> None:
        start_time = time.time()

        self.file_path = path
        self.input = []
        self.combinations = []
        self.lines = []
        self.areas = []

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self) -> None:
        data = list()
        with open(self.file_path) as file:
            for line in file:
                x, y = line.strip().split(",")
                data.append((int(x), int(y)))
        self.input = tuple(data)

    def part1(self) -> int:
        self.combinations = tuple([tuple(list(x))
                                   for x in itertools.combinations(self.input, 2)])
        area_list = []
        for i, [a, b] in enumerate(self.combinations):
            height = abs(a[0] - b[0]) + 1
            length = abs(a[1]-b[1]) + 1
            area_list.append([height * length, i])

        self.areas = sorted(area_list, reverse=True)
        return self.areas[0][0]

    def valid_area(self, index) -> bool:
        a, b = self.combinations[index]
        x_high = max(a[0], b[0])
        y_high = max(a[1], b[1])
        x_low = min(a[0], b[0])
        y_low = min(a[1], b[1])

        for start, end in self.lines:
            # if there is a point of the contour within the area, the area is invalid.
            # excluding the edges. A point of the contour on the edge is possible.
            # only start since all points are also a start in self.lines
            if x_low < start[0] < x_high and y_low < start[1] < y_high:
                return False

            # start is outside, but ends on the other side of areas edge, the area is invalid
            elif start[0] <= x_low and y_low < start[1] < y_high:
                if end[0] > x_low:
                    return False

            elif start[0] >= x_high and y_low < start[1] < y_high:
                if end[0] < x_high:
                    return False

            elif start[1] >= y_high and x_low < start[0] < x_high:
                if end[1] < y_high:
                    return False

            elif start[1] <= y_low and x_low < start[0] < x_high:
                if end[1] > y_low:
                    return False

        return True

    def part2(self) -> int:
        self.lines = []
        for i, _ in enumerate(self.input):
            j = (i+1) % len(self.input)
            self.lines.append((self.input[i], self.input[j]))

        for area, index in self.areas:

            valid = self.valid_area(index)
            if valid:
                return area

        return 0


Puzzle9(EXAMPLE)
Puzzle9(INPUT)
