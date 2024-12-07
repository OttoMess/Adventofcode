import time
import itertools

EXAMPLE = "AoC_inputs/2024/day_7_example.txt"
INPUT = "AoC_inputs/2024/day_7.txt"


class Puzzle7:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.values: list
        self.answers: list

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        values = list()
        answers = list()
        with open(self.file_path) as file:
            for line in file:
                ans, vals = line.strip().split(":")
                answers.append(int(ans))
                val = [int(i) for i in vals.strip().split()]
                values.append(val)
        self.values = values
        self.answers = answers

    def part1(self):
        collector = 0
        for i, ans in enumerate(self.answers):
            if self.runner(ans, self.values[i]):
                collector += ans
        return collector

    def part2(self):
        collector = 0
        loop_time = time.time()
        for i, ans in enumerate(self.answers):
            if (i + 1) % 50 == 0:
                print(
                    f"{i + 1} of {len(self.answers)} done {round(time.time() - loop_time, 4)} [sec]"
                )
                loop_time = time.time()
            if self.runner(ans, self.values[i]):
                collector += ans
            elif self.runner(ans, self.values[i], True):
                collector += ans
        return collector

    @staticmethod
    def cal(a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "*":
            return a * b
        elif operator == "||":
            return int(str(a) + str(b))

    def runner(self, ans, vals, combine=False):
        operators = ["+", "*"]
        if combine:
            operators.append("||")
        product = list(itertools.product(operators, repeat=len(vals) - 1))
        for operator_set in product:
            check = vals[0]
            for i in range(1, len(vals)):
                check = self.cal(check, vals[i], operator_set[i - 1])
            if check == ans:
                return True
        return False


Puzzle7(EXAMPLE)
Puzzle7(INPUT)
