import time
# from functools import cache
import itertools

DATA = "2023/data/day12.txt"
EXAMPLE = "2023/data/day12_example.txt"
TEST = "2023/data/day12_test.txt"


class Puzzle12:

    def __init__(self, path):
        self.fold_groups = None
        self.springs = None
        self.vents = None
        self.groups = None
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.part1()
        # self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        # print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        self.read_txt()
        for j, _ in enumerate(self.vents):
            self.part1_collector += self.search(self.vents[j], self.groups[j])

    def part2(self):
        self.read_txt()
        self.unfold()
        for j, _ in enumerate(self.springs):
            self.part1_collector += self.search(self.springs[j], self.fold_groups[j])

    def search(self, vent, group):
        q = [pos for pos, char in enumerate(vent) if char == "?"]

        group = [int(g) for g in group]
        sets = sum(group) - vent.count("#")
        # w = [s for s in itertools.combinations(q, sets)]
        # e = [list(i) for i in w]
        ans = 0
        # print(f"start loop with lenth of set : {sets}")
        for s in itertools.combinations(q, sets):
            test = list(vent.replace("?", "."))
            for c in s:
                test[c] = "#"
            valid = self.is_valid("".join(i for i in test), group)
            if valid:
                # print("".join(i for i in test))
                ans += 1

        print(vent, group, ans)
        return ans

    @staticmethod
    def is_valid(vent: str, group: list):
        vents = [v for v in vent.split(".") if v != ""]

        if len(group) != len(vents):
            return False
        elif sum(group) != vent.count("#"):
            return False

        for j, i in enumerate(vents):
            if not i.count("#") == group[j]:
                return False
        return True

    def read_txt(self):
        raw = list()
        groups = list()
        vents = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
                groups.append(line.split(" ")[1].strip().split(","))
                vents.append(line.split(" ")[0].strip())
        self.data = raw
        self.groups = groups
        self.vents = vents

    def unfold(self):
        vents = [(i.split(" ")[0] + "?") * 4 + i.split(" ")[0] for i in self.data]
        groups = [(i.split(" ")[1]+",") * 4 + i.split(" ")[1]for i in self.data]

        self.springs = vents
        self.fold_groups = [i.split(",") for i in groups]


Puzzle12(EXAMPLE)
Puzzle12(DATA)
