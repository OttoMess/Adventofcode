import time


EXAMPLE = "AoC_inputs/2025/day_1_example.txt"
INPUT = "AoC_inputs/2025/day_1.txt"


class Puzzle1:
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
                raw = line.strip()
                data.append([raw[0], int(raw[1:])])
        self.input = data

    def part1(self):
        dial = 50
        counter = 0
        for turn in self.input:
            match turn[0]:
                case "L":
                    dial = (dial - turn[1]) % 100
                case "R":
                    dial = (dial + turn[1]) % 100
            if dial == 0:
                counter += 1
            # print(turn, dial)
        return counter

    def part2(self):
        dial = 50
        counter = 0
        print(dial, counter)
        for turn in self.input:
            # if turn[1] >= 100:
            #     counter += turn[1]//100

            match turn[0]:
                case "L":
                    for i in enumerate((turn[1])):
                        temp = (dial - turn[1])
                case "R":
                    temp = (dial + turn[1])

            dial_n = dial

            dial = temp % 100

            if dial == 0:
                counter += 1
            elif dial_n != 0 and temp < 0 or dial_n != 0 and temp > 99:
                counter += 1
            # print(turn, dial, counter)
        return counter
# TODO fails for large number like R1000
# Be careful: if the dial were pointing at 50,
# a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!
# 2197 to low for part 2
# 6143 to high


Puzzle1(EXAMPLE)
Puzzle1(INPUT)
