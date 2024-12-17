import time

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
        # TODO reverse program ?
        return

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
Puzzle17(EXAMPLE)
Puzzle17(INPUT)
