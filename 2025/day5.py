import time
import intervaltree

EXAMPLE = "AoC_inputs/2025/day_5_example.txt"
INPUT = "AoC_inputs/2025/day_5.txt"


class Puzzle5:
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
        fresh = list()
        ingredients = list()
        with open(self.file_path) as file:
            next = False
            for line in file:
                if line.strip() == "":
                    next = True
                    continue
                if next:
                    ingredients.append(int(line.strip()))
                else:
                    fresh.append(tuple([int(i)
                                 for i in line.strip().split("-")]))

        self.fresh = tuple(fresh)
        self.ingredients = tuple(ingredients)

    def part1(self):
        counter = 0
        for ingredient in self.ingredients:
            for start, end in self.fresh:
                if ingredient >= start and ingredient <= end:
                    counter += 1
                    break
        return counter

    def part2(self):
        condensed = list()
        full_range = list()
        loop = 0
        # ranger = list()
        intervals = list()
        # tree = intervaltree.IntervalTree()
        for begin, end in self.fresh:
            # ranger.append(range(begin, end))
            intervals.append([begin, end])

        intervals.sort()
        residue = list()
        residue.append(intervals[0])

        for i in range(1, len(intervals)):
            last = residue[-1]
            curr = intervals[i]

            # If current interval overlaps with the last merged
            # interval, merge them
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                residue.append(curr)

        #     if begin != end:
        #         tree[begin: end] = (begin, end)
        #         # tree = it.IntervalTree.from_tuples(self.fresh)
        # tree.merge_overlaps(strict=False)
        # for begin, end in self.fresh:
        #     if loop == 0:
        #         condensed.append([begin, end, True])
        #         full_range = [begin, end]
        #     else:
        #         if begin > full_range[1]:  # expand range positive side
        #             condensed.append([full_range[1]+1, begin-1, False])
        #             full_range[1] = end
        #             condensed.append([begin, end, True])

        #         elif end < full_range[0]:  # expand range negative  side
        #             condensed.append([end, full_range[0]-1, False])
        #             full_range[0] = begin
        #             condensed.append([begin, end, True])

        #         elif full_range[0] >= begin and end <= full_range[1]:
        #             q = 1

        # # fit in range already
        # if a<=begin <=b and a<=end <=b:
        #     continue
        # elif a<begin:
        #     condensed.append([end+1])
        #     condensed.append([begin,end,True])

        loop += 1
        # fresh_set.update(range(start, end+1)) #BUG will not work, way to big
        return


Puzzle5(EXAMPLE)
Puzzle5(INPUT)
