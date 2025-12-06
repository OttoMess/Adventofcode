import time

EXAMPLE = "AoC_inputs/2025/day_3_example.txt"
INPUT = "AoC_inputs/2025/day_3.txt"


class Puzzle3:
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
                lose = tuple([int(n) for n in line.strip()])
                data.append(lose)
        self.input = data

    def part1(self) -> int:
        collector = 0

        for bank in self.input:
            max_joltage = int()

            for i, left_bat in enumerate(bank):
                left = left_bat
                if left * 10 < max_joltage:
                    continue

                for right_loc in range(i+1, len(bank)):
                    right = bank[right_loc]
                    joltage = left * 10 + right

                    if joltage > max_joltage:
                        max_joltage = joltage

            collector += max_joltage

        return collector

    @staticmethod
    def list_to_joltage(data) -> int:
        joltage = sum([j*10**(len(data)-1 - i) for i, j in enumerate(data)])
        return joltage

    @staticmethod
    def search_best_option(bank, start, end) -> tuple[int, list]:
        best = int()
        locations = []
        for i in range(start, end+1):  # include end location
            if bank[i] > best:
                best = bank[i]
                locations = [i]
            elif bank[i] == best:
                locations.append(i)
        return best, locations

    def recursive_tree_search(self, bank, start, depth) -> None:
        if depth == self.n_bat:
            return
        elif depth == 0:
            self.battery = list()

        end = len(bank)-self.n_bat+depth
        value, locations = self.search_best_option(bank, start, end)

        self.battery.append(value)
        for loc in locations:
            self.recursive_tree_search(bank, loc+1, depth+1)

        if depth == 0:
            return
        else:
            if len(self.battery) == 12:
                self.options.add(self.list_to_joltage(self.battery))
            self.battery.pop(-1)
            return

    def part2(self) -> int:
        collector = 0
        self.n_bat = 12

        for bank in self.input:

            self.options = set()
            self.recursive_tree_search(bank, start=0, depth=0)
            # print(self.options)
            collector += max(self.options)

        return collector


Puzzle3(EXAMPLE)
Puzzle3(INPUT)
