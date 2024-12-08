import time

TEST = "AoC_inputs/2024/day_4_test.txt"
EXAMPLE = "AoC_inputs/2024/day_4_example.txt"
INPUT = "AoC_inputs/2024/day_4.txt"


class Puzzle4:
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
                data.append(line.strip())
        self.input = data

    def part1(self):
        directions = (
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, -1),
            (0, -1),
            (-1, 0),
            (1, -1),
            (-1, 1),
        )
        x_index = list()
        for i in range(len(self.input)):
            x_index.append([i, self.find_index(self.input[i], "X")])

        words = list()
        data = self.input
        y_lim = len(data)
        x_lim = len(data[0])
        for index in x_index:
            y = index[0]
            for i in index[1]:
                x = i
                for step in directions:
                    word = data[y][x]
                    for j in range(1, 4):
                        next_y = y + (j * step[0])
                        next_x = x + (j * step[1])
                        if 0 <= next_x < x_lim and 0 <= next_y < y_lim:
                            word += data[next_y][next_x]
                        else:
                            break
                    if word == "XMAS":
                        words.append(word)

        return len(words)

    def part2(self):
        a_index = list()
        for i in range(1, len(self.input) - 1):
            a_index.append([i, self.find_index(self.input[i], "A")])
        data = self.input
        crosses = 0
        y_lim = len(data)
        x_lim = len(data[0])
        for line in a_index:
            y = line[0]
            if 1 <= y < y_lim - 1:
                for i in line[1]:
                    x = i
                    if 1 <= x < x_lim - 1:
                        one = data[y - 1][x - 1] + data[y][x] + data[y + 1][x + 1]
                        two = data[y + 1][x - 1] + data[y][x] + data[y - 1][x + 1]
                        if one in ["MAS", "SAM"] and two in ["MAS", "SAM"]:
                            crosses += 1
        return crosses

    @staticmethod
    def find_index(line, string):
        return [i for i in range(len(line)) if line[i] == string]


# Puzzle4(TEST)
Puzzle4(EXAMPLE)
Puzzle4(INPUT)
