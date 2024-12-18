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
        self.input = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        # self.find_start_len16()
        # self.find_start_len17()
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
        self.out = list()
        self.pointer = 0
        while self.pointer < len(self.program):
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]

            if opcode == 0:
                self.opcode_0(operand)
            elif opcode == 1:
                self.opcode_1(operand)
            elif opcode == 2:
                self.opcode_2(operand)
            elif opcode == 3:
                self.opcode_3(operand)
            elif opcode == 4:
                self.opcode_4()
            elif opcode == 5:
                self.opcode_5(operand)
            elif opcode == 6:
                self.opcode_6(operand)
            elif opcode == 7:
                self.opcode_7(operand)

        value = ",".join([str(i) for i in self.out])
        return value

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
        # TODO reverse program ?


        B = B^4     2,4
        A = A//B^4      1,5
        C =(A//B^4)//B^4    7,5

        B = B^((A//B^4)//B^4)   4,3
        B = (B^((A//B^4)//B^4))^6     1,6
        A = A //3   0,3
        out=B%5     5,5
        restart     3,0


        """
        lower_edge = self.find_start_len16()
        upper_edge = self.find_start_len17()

        search = np.linspace(1.054e14, 1.408e14, 2500)

        output = list()
        second = list()
        third = list()
        input = list()
        A_start = lower_edge
        for A in search:
            # input.append(A)
            self.program_runner(int(A))
            temp = "".join([str(j) for j in self.out])
            output.append(int(temp[-1]))
            second.append(int(temp[-2]))
            third.append(int(temp[-3]))

            # A_start = int(A_start * 1.1)
        plt.plot(search, output)
        plt.plot(search, second)
        plt.plot(search, third)
        plt.show()
        return

    def find_start_len16(self):
        A_low = int(3.5184e13)
        A_high = int(3.51851e13)
        while True:
            A_start = (A_high + A_low) // 2
            self.program_runner(A_start)

            if self.program == self.out:
                print(f"found with A = {A_start }")
                return A_start, self.out, self.program

            if len(self.out) == 15:
                A_low = A_start
            elif len(self.out) == 16:
                A_high = A_start

            if A_high - A_low < 50:
                break

        A_start = A_low
        while True:
            self.program_runner(A_start)

            if len(self.out) == 16:
                print(f"found start of 16 lengths outputs {A_start}")
                break
            else:
                A_start += 1

        return A_start

    def find_start_len17(self):
        A_low = int(2.77e14)
        A_high = int(3e14)
        while True:
            A_start = (A_high + A_low) // 2
            self.program_runner(A_start)

            if self.program == self.out:
                print(f"found with A = {A_start }")
                return A_start, self.out, self.program

            if len(self.out) == 16:
                A_low = A_start
            elif len(self.out) == 17:
                A_high = A_start

            if A_high - A_low < 50:
                break

        A_start = A_low
        while True:
            self.program_runner(A_start)

            if len(self.out) == 17:
                print(f"found end of 16 lengths outputs {A_start-1}")
                break
            else:
                A_start += 1

        return A_start - 1

    def program_runner(self, A_start):
        self.out = list()
        self.pointer = 0
        self.A = A_start
        while self.pointer < len(self.program):
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]

            if opcode == 0:
                self.opcode_0(operand)
            elif opcode == 1:
                self.opcode_1(operand)
            elif opcode == 2:
                self.opcode_2(operand)
            elif opcode == 3:
                self.opcode_3(operand)
            elif opcode == 4:
                self.opcode_4()
            elif opcode == 5:
                self.opcode_5(operand)
            elif opcode == 6:
                self.opcode_6(operand)
            elif opcode == 7:
                self.opcode_7(operand)

    def plot(self, A, outs):
        # size = [len(o) for o in outs]
        plt.plot(A, outs)
        plt.show()

    def combo(self, input):
        if input <= 3:
            return input
        elif input == 4:
            return self.A
        elif input == 5:
            return self.B
        elif input == 6:
            return self.C

    def opcode_0(self, input):
        self.A = self.A // 2 ** self.combo(input)
        self.pointer += 2

    def opcode_1(self, input):
        self.B = self.B ^ input
        self.pointer += 2

    def opcode_2(self, input):
        self.B = self.combo(input) % 8
        self.pointer += 2

    def opcode_3(self, input):
        if self.A == 0:
            self.pointer += 2
        else:
            self.pointer = input

    def opcode_4(self):
        self.B = self.B ^ self.C
        self.pointer += 2

    def opcode_5(self, input):
        self.out.append(self.combo(input) % 8)
        self.pointer += 2

    def opcode_6(self, input):
        self.B = self.A // 2 ** self.combo(input)
        self.pointer += 2

    def opcode_7(self, input):
        self.C = self.A // 2 ** self.combo(input)
        self.pointer += 2


# Puzzle17(TEST)
# Puzzle17(EXAMPLE)
Puzzle17(INPUT)
