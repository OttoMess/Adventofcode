import time

EXAMPLE = "Data/Puzzle_#9_example.txt"
DATA = "Data/Puzzle_#9.txt"
TEST = "Data/Puzzle_#9_test.txt"
TEST2 = "Data/Puzzle_#9_test2.txt"


class Puzzle9:

    def __init__(self, file_path):
        self.data = list()
        self.file_path = file_path

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()
        self.read_txt()
        self.part1()
        self.part2()
        print(file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Number of steps part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        data_str = [i.split(" ") for i in raw]
        for j, _ in enumerate(data_str):
            self.data.append([int(i) for i in data_str[j]])

    def part1(self):
        for i in self.data:
            self.part1_collector += self.positive_extrapolate(i)

    def part2(self):
        for i in self.data:
            self.part2_collector += self.negative_extrapolate(i)

    def positive_extrapolate(self, row:list):
        output = int()
        tree = self.tree(row)
        for i in tree:
            output += i[-1]
        return output

    def negative_extrapolate(self, row:list):
        tree = self.tree(row)
        a = tree[-2][0]
        for i in range(len(tree)-2):
            b = tree[-i-3][0] - a
            a = b
        return a

    @staticmethod
    def tree(row:list):
        tree = [row]
        while True:
            test = tree[-1]
            x = [test[j + 1] - test[j] for j in range(len(test)-1)]
            tree.append(x)
            if x.count(0) == len(x):
                break

        return tree


Puzzle9(EXAMPLE)
Puzzle9(DATA)
