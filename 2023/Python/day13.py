import time

# from functools import cache
# import itertools

DATA = "2023/data/day13.txt"
EXAMPLE = "2023/data/day13_example.txt"
TEST = "2023/data/day13_test.txt"


class Puzzle13:

    def __init__(self, path):
        self.groups = list()
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.read_txt()
        self.group_patches()

        # self.part1()
        self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        # print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        for patch in self.groups:
            h = self.horizontal_mirror(patch)
            v = self.vertical_mirror(patch)
            print(f" \nhorizontal line: {h}\nvertical line: {v}")
            for i in patch:
                print(i)
            self.part1_collector += h * 100 + v

    def part2(self):
        for patch in self.groups:
            dif = self.difference(patch)
            if dif is False:
                continue
            else:
                h = self.horizontal_mirror(patch)
                v = self.vertical_mirror(patch)
        pass

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        self.data = raw

    def group_patches(self):
        patch = list()
        for d in self.data:
            if d != "":
                patch.append(d)
            else:
                self.groups.append(patch)
                patch = list()
        self.groups.append(patch)

    @staticmethod
    def rotate(patch):
        rotated = list()
        for j, _ in enumerate(patch[0]):
            collector = str()
            for i in patch:
                collector += i[j]
            rotated.append(collector)
        return rotated

    def vertical_mirror(self, patch):
        return self.horizontal_mirror(self.rotate(patch))

    @staticmethod
    def horizontal_mirror(patch):
        search_lines = list()
        for j in range(len(patch) - 1):
            a = patch[j]
            b = patch[j + 1]
            if a != b:
                continue
            else:
                search_lines.append(j)

        if len(search_lines) == 0:
            return 0

        for s in search_lines:
            lower = s + 1
            upper = len(patch) - s - 1
            r = min(lower, upper)
            match = 0
            for i in range(r):
                a = patch[s - i]
                b = patch[s + 1 + i]
                if a == b:
                    match += 1
            if match == r:
                return s + 1
        return 0

    @staticmethod
    def difference(patch):
        near_same = False
        for j in range(len(patch) - 1):
            delta = 0
            a = patch[j]
            b = patch[j + 1]
            k = 0
            while k < len(a):
                # for k, _ in enumerate(a):
                if delta > 1:
                    k = len(a) + 1

                elif a[k] != b[k]:
                    delta += 1
                    if delta == 1:
                        temp = k
                    k += 1

                else:
                    k += 1

            if delta == 1:
                near_same = j
                location = temp

        if near_same is not False:
            if patch[near_same][location] == ".":
                patch[near_same] = patch[near_same][:location] + "#" + patch[near_same][location+1:]

            elif patch[near_same][location] == "#":
                print(patch[near_same])
                patch[near_same] = patch[near_same][:location] + "." + patch[near_same][location+1:]
                print(patch[near_same])

            return patch

        else:
            return False


Puzzle13(EXAMPLE)
# Puzzle13(DATA)
