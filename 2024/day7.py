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
        self.found_part1 = list()
        for i, ans in enumerate(self.answers):
            if self.plus_and_mult(ans, self.values[i]):
                collector += ans
                self.found_part1.append(i)
        return collector

    @staticmethod
    def plus_and_mult(ans, vals):
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
    def plus_and_mult_and_combine(ans, vals):
        """
        There are 3 options. using binary info.
        2 operators will give 3**2 = 9 options.
        2 bits per options set needed
        00 = +
        01 = *
        10 = ||
        11 = nothing
        """

        operators = len(vals) - 1
        int_search = 2 ** (operators * 2)
        # BUG to high for part 2
        # 189207837752840

        # BUG in the current code all operators can be || not just one. Needs to be fixed
        for i in range(int_search):
            test_value = vals[0]
            bin_options = format(i, "b").zfill(operators * 2)

            for j in range(1, len(vals)):
                check = bin_options[-2:]
                bin_options = bin_options[:-2]
                if check == "00":
                    test_value += vals[j]
                elif check == "01":
                    test_value *= vals[j]
                elif check == "10":
                    test_value = int(str(test_value) + str(vals[j]))

            if test_value == ans:
                return True

        return False

    def part2(self):
        collector = 0
        which_to_count = list()
        loop_time = time.time()
        for i, ans in enumerate(self.answers):
            if (i + 1) % 10 == 0:
                print(
                    f"{i + 1} of {len(self.answers)} done {round(time.time() - loop_time, 4)} [sec]"
                )
                loop_time = time.time()
            if self.plus_and_mult(ans, self.values[i]):
                which_to_count.append(i)
                collector += ans
            elif self.plus_and_mult_and_combine(ans, self.values[i]):
                collector += ans
                which_to_count.append(i)
        return collector

        return


Puzzle7(EXAMPLE)
Puzzle7(INPUT)
