import time
from matplotlib import pyplot as plt
import numpy as np

TEST = "AoC_inputs/2024/day_17_test.txt"
EXAMPLE = "AoC_inputs/2024/day_17_example.txt"
INPUT = "AoC_inputs/2024/day_17.txt"


class Puzzle17:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                if "A" in line:
                    self.A = int(line.strip().split(":")[1])
                elif "B" in line:
                    self.B = int(line.strip().split(":")[1])
                elif "C" in line:
                    self.C = int(line.strip().split(":")[1])
                elif "Program:" in line:
                    temp = line.strip().split(":")
                    self.program = [int(i) for i in temp[1].split(",")]

    def part1(self):
        out = self.program_runner(self.program, self.A)
        stringer = ",".join([str(i) for i in out])
        return stringer

    def part2(self):
        """
        2,4,1,5,7,5, 4,3,1,6,0,3,5,5,3,0
        B = B^4     2,4
        A = A//B    1,5
        C = A//B    7,5
        B = B^C     4,3
        B = B^6     1,6
        A = A //3   0,3
        out=B%5     5,5
        restart     3,0
        """
        e = self.program_runner(self.program, self.A)
        return

    @staticmethod
    def program_runner(program, a):
        out = list()
        pointer = 0
        b = 0
        c = 0
        while pointer < len(program):
            opcode = program[pointer]
            operand = program[pointer + 1]
            combo = [0, 1, 2, 3, a, b, c][operand]

            match opcode:
                case 0:
                    a = int(a / 2**combo)
                case 1:
                    b = b ^ operand
                case 2:
                    b = combo % 8
                case 3:
                    if a != 0:
                        pointer = operand - 2
                case 4:
                    b = b ^ c
                case 5:
                    out.append(combo % 8)
                case 6:
                    b = int(a / 2**combo)
                case 7:
                    c = int(a / 2**combo)

            pointer += 2
        return out


# from re import findall

# a, b, c, *prog = [
#     int(n) for n in findall("(\d+)", open("AoC_inputs/2024/day_17.txt").read())
# ]


# def run(prog, a):
#     ip, b, c, out = 0, 0, 0, []
#     while ip >= 0 and ip < len(prog):
#         lit, combo = prog[ip + 1], [0, 1, 2, 3, a, b, c, 99999][prog[ip + 1]]
#         match prog[ip]:
#             case 0:
#                 a = int(a / 2**combo)  # adv
#             case 1:
#                 b = b ^ lit  # bxl
#             case 2:
#                 b = combo % 8  # bst
#             case 3:
#                 ip = ip if a == 0 else lit - 2  # jnz
#             case 4:
#                 b = b ^ c  # bxc
#             case 5:
#                 out.append(combo % 8)  # out
#             case 6:
#                 b = int(a / 2**combo)  # bdv
#             case 7:
#                 c = int(a / 2**combo)  # cdv
#         ip += 2
#     return out


# print("Part 1:", ",".join(str(n) for n in run(prog, a)))

# target = prog[::-1]


# def find_a(a=0, depth=0):
#     if depth == len(target):
#         return a
#     for i in range(8):
#         output = run(prog, a * 8 + i)
#         if output and output[0] == target[depth]:
#             if result := find_a((a * 8 + i), depth + 1):
#                 return result
#     return 0


# Puzzle17(TEST)
# Puzzle17(EXAMPLE)
Puzzle17(INPUT)
