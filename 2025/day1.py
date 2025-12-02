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
                data.append((raw[0], int(raw[1:])))
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

        return counter

    def part2(self):
        dial = 50
        counter = 0

        for turn in self.input:
            match turn[0]:
                case "L":
                    for i in range(turn[1]):
                        dial -= 1
                        dial = dial % 100
                        if dial == 0:
                            counter += 1

                case "R":
                    for i in range(turn[1]):
                        dial += 1
                        dial = dial % 100
                        if dial == 0:
                            counter += 1

        return counter


Puzzle1(EXAMPLE)
Puzzle1(INPUT)
