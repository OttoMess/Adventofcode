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
        stringer = []
        for k in range(len(self.input)):
            i = 0
            q = []
            # BUG not all numbers are 3 digits long can not use fixed window
            # possible use the location of the operators signs
            while i < len(self.input[k]) - 3:
                section = self.input[k][i:i+3]
                q.append(section)
                i += 4
            stringer.append(q)
        return 0


Puzzle6(EXAMPLE)
Puzzle6(INPUT)
