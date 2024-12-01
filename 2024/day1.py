import time
from collections import Counter

EXAMPLE = "AoC_inputs/2024/day_1_example.txt"
INPUT = "AoC_inputs/2024/day_1.txt"


class Puzzle1:
    def __init__(self, path):
        self.file_path = path
        self.input = list()

        print(self.file_path)

        start_time = time.time()
        self.read_txt()
        list1, list2 = self.split_sort()

        print(f"output part one: {self.find_diff_part1(list1, list2)}")
        print(f"output part two: {self.appearance_part2(list1, list2)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                line.strip()
                data.append(line.split())
        self.input = data

    def split_sort(self):
        list1 = [int(line[0]) for line in self.input]
        list2 = [int(line[1]) for line in self.input]

        list1.sort()
        list2.sort()

        return list1, list2

    def find_diff_part1(self, list1, list2):
        counter = 0
        for i, _ in enumerate(list1):
            difference = list1[i] - list2[i]
            counter += abs(difference)
        return counter

    def appearance_part2(self, list1, list2):
        collect = 0
        appearances = Counter(list2)
        present = appearances.keys()
        for i in list1:
            if i in present:
                collect += i * appearances[i]
        return collect


Puzzle1(EXAMPLE)
Puzzle1(INPUT)
