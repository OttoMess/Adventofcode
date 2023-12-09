
from dataclasses import dataclass

EXAMPLE = "Data/Puzzle_#8_example.txt"
DATA = "Data/Puzzle_#8.txt"
TEST = "Data/Puzzle_#8_test.txt"
TEST2 = "Data/Puzzle_#8_test2.txt"


class Puzzle8:

    def __init__(self):
        self.data = None

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        data = [i.split("=") for i in raw]
        self.data = dict
        for d in data:
            self.data.append(Hand(d[0], int(d[1])))