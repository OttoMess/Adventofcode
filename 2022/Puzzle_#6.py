import time
from collections import Counter

EXAMPLE = "AoC_inputs/2022/day_6_example.txt"
INPUT = "AoC_inputs/2022/day_6.txt"


class puzzle6:
    def __init__(self, path):
        self.file_path = path
        self.inputs = list()

        print(self.file_path)

        start_time = time.time()
        self.read_txt()

        print(f"output part one: {self.find_marker(4)}")
        print(f"output part two: {self.find_marker(14)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.inputs = data

    def find_marker(self, window_size):
        marker_loc = list()
        for input in self.inputs:  # loop only needed for example with multiply lines
            # marker loc start at 1, python index at 0. the [0:x] is used where x is not included. This resolves the mismatch in the index starts
            marker = window_size
            for _ in input:
                cache = input[marker - window_size : marker]
                freq = Counter(cache)
                if len(cache) == len(freq):
                    marker_loc.append(marker)
                    break
                else:
                    marker += 1
        return marker_loc


puzzle6(EXAMPLE)
puzzle6(INPUT)
