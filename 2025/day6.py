import time


EXAMPLE = "AoC_inputs/2025/day_6_example.txt"
INPUT = "AoC_inputs/2025/day_6.txt"


class Puzzle6:
    def __init__(self, path) -> None:
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self) -> None:
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line)
        self.input = data

    def part1(self) -> int:
        operator = str()
        collector = 0

        cut = []
        for line in self.input:
            cut.append(line.strip().split())

        for column in range(len(cut[0])):
            values = []
            for row in range(len(cut)):
                a = cut[row][column]
                try:
                    values.append(int(a))
                except:
                    operator = a

            match operator:
                case "+":
                    for v in values:
                        collector += v

                case "*":
                    mul = values[0]
                    for i in range(1, len(values)):
                        mul *= values[i]
                    collector += mul
        return collector

    def part2(self) -> int:
        collector = 0

        ope_loc = [(p, i) for i, p in enumerate(self.input[-1]) if p != " "]

        for pos in range(len(ope_loc)):
            values = []
            begin = ope_loc[pos][1]

            if pos == len(ope_loc)-1:
                end = len(self.input[0])
            else:
                end = ope_loc[pos+1][1]-1

            for j in range(begin, end):
                v = ""
                for i in range(len(self.input)-1):
                    v += str(self.input[i][j])

                try:
                    values.append(int(v))
                except:
                    continue

            match ope_loc[pos][0]:
                case "+":
                    for v in values:
                        collector += v

                case "*":
                    mul = values[0]
                    for i in range(1, len(values)):
                        mul *= values[i]
                    collector += mul

        return collector


Puzzle6(EXAMPLE)
Puzzle6(INPUT)
