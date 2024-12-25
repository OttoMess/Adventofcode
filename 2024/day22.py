import time
from collections import defaultdict

EXAMPLE = "AoC_inputs/2024/day_22_example.txt"
INPUT = "AoC_inputs/2024/day_22.txt"


class Puzzle22:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path

        print(self.file_path)
        self.read_txt()
        answer = self.part1and2()

        print(f"output part one: {next (answer)}")
        print(f"output part two: {next (answer)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(int(line.strip()))
        self.input = data

    def part1and2(self):
        output = list()
        changes = list()
        number_bananas = list()
        for start in self.input:
            number = start
            change = list()
            value = list()
            value.append(number % 10)

            for _ in range(0, 2000):
                a = number % 10
                number = self.new_number(number)
                change.append(number % 10 - a)
                value.append(number % 10)
            output.append(number)
            changes.append(change)
            number_bananas.append(value)

        yield sum(output)

        value = defaultdict(int)
        for j, cha in enumerate(changes):
            seen = set()
            for i in range(len(cha) - 4):
                window = tuple(cha[i : i + 4])
                if window not in seen:
                    value[window] += number_bananas[j][i + 4]
                    seen.add(window)

        e = max(value, key=value.get)
        yield value[e]

    def new_number(self, initial):
        number = initial * 64
        number = self.mix(initial, number)
        number = self.prune(number)

        secret = number // 32
        number = self.mix(secret, number)
        number = self.prune(number)

        secret = number * 2048
        number = self.mix(secret, number)
        number = self.prune(number)
        return number

    @staticmethod
    def mix(secret, number):
        return secret ^ number

    @staticmethod
    def prune(number):
        return number % 16777216


Puzzle22(EXAMPLE)
Puzzle22(INPUT)
