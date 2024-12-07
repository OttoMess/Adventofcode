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

    @staticmethod
    def plus_and_mul(ans, vals):
        """
        since there are 2 options. using binary info. if there are 3 values there are 2 operator.
        2 operators will give 2**2 = 4 options. Every option is present in the binary form of a int from range(0,4)
        0 is used to represent + and 1 is used for *.
        """
        options = 2 ** (len(vals) - 1)

        for i in range(options):
            test_value = vals[0]
            bin_options = format(i, "b").zfill(options - 1)

            for j in range(1, len(vals)):
                if bin_options[-j] == "0":
                    test_value += vals[j]
                elif bin_options[-j] == "1":
                    test_value *= vals[j]

            if test_value == ans:
                return True
        return False

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

    def part2(self):
        collector = 0
        which_to_count = list()
        loop_time = time.time()
        for i, ans in enumerate(self.answers):
            if (i + 1) % 50 == 0:
                print(
                    f"{i + 1} of {len(self.answers)} done {round(time.time() - loop_time, 4)} [sec]"
                )
                loop_time = time.time()
            if self.plus_and_mul(ans, self.values[i]):
                which_to_count.append(i)
                collector += ans
            elif self.runner(ans, self.values[i]):
                collector += ans
                which_to_count.append(i)
        return collector

        return


def test(number):
    for i in range(number):
        print(i, i % 2, i % 3)


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


Puzzle7(EXAMPLE)
Puzzle7(INPUT)
