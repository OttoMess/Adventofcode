import time
import itertools

EXAMPLE = "AoC_inputs/2025/day_8_example.txt"
INPUT = "AoC_inputs/2025/day_8.txt"


class Puzzle8:
    def __init__(self, path, times) -> None:
        start_time = time.time()

        self.times = times
        self.min_set = []

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
                data.append(tuple([int(i) for i in line.strip().split(",")]))
        self.input = tuple(data)

    @staticmethod
    def euclidean_distance(a, b) -> int:
        d_x = (a[0]-b[0])**2
        d_y = (a[1]-b[1])**2
        d_z = (a[2]-b[2])**2
        return (d_x+d_y+d_z)**0.5

    def part1(self) -> int:
        """
        https://en.wikipedia.org/wiki/Euclidean_distance

        """
        # make list of all shortest combinations

        comb = [list(x) for x in itertools.combinations(self.input, 2)]

        self.min_set = [[a, b, self.euclidean_distance(
            a, b)] for a, b in comb]

        self.min_set.sort(key=lambda k: k[2])

        circuits = []
        for i in range(self.times):
            a, b, _ = self.min_set[i]

            if i == 0:
                circuits.append(set([a, b]))

                continue

            for k, j in enumerate(circuits):

                if a not in j and b in j:
                    circuits[k].add(a)
                    break

                elif a in j and b not in j:
                    circuits[k].add(b)
                    break

                elif a in j and b in j:
                    break

                elif k == len(circuits)-1:  # and a not in j and b not in j:
                    circuits.append(set([a, b]))
                    break

        # merge section

        a = len(circuits)
        b = 0
        while b < a:
            a = len(circuits)
            for i, c in enumerate(circuits):
                to_remove = []

                for j in range(i+1, len(circuits)):
                    tester = circuits[j]

                    if tester & c and tester not in to_remove:
                        c.update(tester)
                        to_remove.append(tester)

                for item in to_remove:
                    circuits.remove(item)
            b = len(circuits)

        circuits.sort(key=lambda k: len(k), reverse=True)

        collector = 1
        for i in range(3):
            collector *= len(circuits[i])
        return collector

    def part2(self) -> int:
        target = len(self.input)
        circuits = []
        run = True
        i_loop = 0
        while run:
            a, b, _ = self.min_set[i_loop]

            if i_loop == 0:
                circuits.append(set([a, b]))
                i_loop += 1
                continue

            for k, j in enumerate(circuits):

                if a not in j and b in j:
                    circuits[k].add(a)
                    break

                elif a in j and b not in j:
                    circuits[k].add(b)
                    break

                elif a in j and b in j:
                    break

                elif k == len(circuits)-1:  # and a not in j and b not in j:
                    circuits.append(set([a, b]))
                    break

            d = 1
            e = 0
            while e < d:
                d = len(circuits)
                for i, c in enumerate(circuits):
                    to_remove = []

                    for j in range(i+1, len(circuits)):
                        tester = circuits[j]

                        if tester & c and tester not in to_remove:
                            c.update(tester)
                            to_remove.append(tester)

                    for item in to_remove:
                        circuits.remove(item)
                e = len(circuits)

            i_loop += 1
            if len(circuits[0]) == target:
                run = False

        return a[0] * b[0]

# 4896 to low
# 1323540 to high
# 81216 not correct


Puzzle8(EXAMPLE, 10)
Puzzle8(INPUT, 1000)
