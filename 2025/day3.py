import time

EXAMPLE = "AoC_inputs/2025/day_3_example.txt"
INPUT = "AoC_inputs/2025/day_3.txt"


class Puzzle3:
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
                lose = tuple([int(n) for n in line.strip()])
                data.append(lose)
        self.input = data

    def part1(self):
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
    def list_to_joltage(data):
        joltage = sum([j[0]*10**(len(data)-1 - i) for i, j in enumerate(data)])
        return joltage

    @staticmethod
    def search_best_option(bank, start, end):
        best = int()
        locations = [int()]
        for i in range(start, end+1):  # include end location
            if bank[i] > best:
                best = bank[i]
                locations = [i]
            elif bank[i] == best:
                locations.append(i)
        return best, locations

    def recursive_tree_search(self, bank, start, depth):
        if depth == self.n_bat:
            return self.volt
        # possible option to use append and pop. not store value but list
        end = len(bank)-self.n_bat+depth
        value, locations = self.search_best_option(bank, start, end)
        col_list = list()
        for loc in locations:
            v = value * 10**(self.n_bat-1-depth)
            self.volt += v
            volts = self.recursive_tree_search(bank, loc+1, depth+1)
            if depth == 0:
                col_list.append(volts)
                self.volt = 0

        if depth == 0:
            return col_list
        else:
            return volts

    def part2(self):
        collector = 0
        self.n_bat = 12

        positions = [i for i in range(self.n_bat)]
        joltage = list()
        for bank in self.input:
            """ #TODO make system to build list with value en position in the battery bank
             [9 (joltage), 3 (location of battery in bank)] 
             location is used, can only add battery's after selected battery"""

            # start joltage for first set of battery's in the bank
            start = [[bank[i], i] for i in positions]
            self.volt = 0
            w = self.recursive_tree_search(bank, start=0, depth=0)
            print(w)
            collector += max(w)

        return collector


Puzzle3(EXAMPLE)
# Puzzle3(INPUT)

# 232610322220956 to high for part 2
