import time

DATA = "2023/data/day15.txt"
EXAMPLE = "2023/data/day15_example.txt"


class Puzzle15:

    def __init__(self, path):
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.data = self.read_txt()

        self.part1()
        self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        for line in self.data:
            line_value = 0
            for char in line:
                line_value += ord(char)
                line_value *= 17
                line_value %= 256
            self.part1_collector += line_value
            # print(f"{line} has value of {line_value}")

    def part2(self):
        boxes = [list() for i in range(256)]
        for line in self.data:

            if line.count("=") > 0:
                label = line.split("=")[0]
                operation = "="
                lens = line.split("=")[1]
            else:
                label = line.split("-")[0]
                operation = "-"

            box = 0
            for char in label:
                box += ord(char)
                box *= 17
                box %= 256

            if operation == "=":
                labels = [i[0] for i in boxes[box]]
                if label in labels:
                    location = labels.index(label)
                    boxes[box][location][1] = lens
                else:
                    boxes[box].append([label, lens])

            elif operation == "-":
                labels = [i[0] for i in boxes[box]]
                # lenses = [i[1] for i in boxes[box]]
                if label in labels:
                    location = labels.index(label)
                    del boxes[box][location]

        total = 0
        for j, box in enumerate(boxes):
            value = 0
            for k, lens in enumerate(box):
                value += (j+1) * (k+1) * int(lens[1])
            print(j, box, value)
            total += value

        self.part2_collector = total

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                raw = line.strip()
        split_list = raw.split(",")
        return split_list


Puzzle15(EXAMPLE)
Puzzle15(DATA)
