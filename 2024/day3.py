import time
import re

EXAMPLE = "AoC_inputs/2024/day_3_example.txt"
INPUT = "AoC_inputs/2024/day_3.txt"


class Puzzle3:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        muls = self.listing_muls()
        muls_dos = self.listing_muls(instructions=True)

        print(f"output part one: {self.multiply(muls)}")
        print(f"output part two: {self.multiply(muls_dos)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        """Building all the inputs lines in to one big string"""
        data = str()
        with open(self.file_path) as file:
            for line in file:
                data += line.strip()
        self.input = data

    def listing_muls(self, instructions=False):
        cache = list()
        m = 0
        pruned = self.input

        if instructions:
            found_dont = True
            while found_dont:
                found_dont, pruned = self.cur_dont_range(pruned)

        while m < len(pruned):
            start, end, found = self.find_mul(pruned[m:])
            if found:
                cache.append(pruned[m:][start:end])
            m += end

        return cache

    @staticmethod
    def multiply(muls):
        collector = 0

        for line in muls:
            q = re.findall(r"\d+", line)
            collector += int(q[0]) * int(q[1])
        return collector

    @staticmethod
    def find_mul(line):
        start = line.find("mul(")

        if start == -1:
            return 0, len(line), False

        for i in range(6, 12):
            cha = line[start + i]
            end = i + start + 1
            if cha == "," or cha.isnumeric():
                continue
            elif cha == ")":
                found = True
                return start, end, found
            else:
                found = False
                return start, end, found

    @staticmethod
    def cur_dont_range(line):
        """
        cut range where don't instruction is valid
        """
        dont = line.find("don't()")
        if dont == -1:
            return False, line

        do = line[dont:].find("do()")
        if do == -1:
            cut_line = line[:dont]
        else:
            cut_line = line[:dont] + line[dont + (do) :]
        return True, cut_line


Puzzle3(EXAMPLE)
Puzzle3(INPUT)
