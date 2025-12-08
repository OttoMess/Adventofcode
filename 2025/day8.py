import time
import itertools

EXAMPLE = "AoC_inputs/2025/day_8_example.txt"
INPUT = "AoC_inputs/2025/day_8.txt"


class Puzzle8:
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
        min_set = []

        combinations = [list(x) for x in itertools.combinations(self.input, 2)]

        min_set = [[a, b, self.euclidean_distance(
            a, b)] for a, b in combinations]

        # for a, b in combinations:
        #     min_set.append(a, b, self.euclidean_distance(a, b))

        min_set.sort(key=lambda k: k[2])

        circuits = []
        end = 1000
        i = 0
        while i < end:
            a, b, _ = min_set[i]

            if i == 0:
                circuits.append(set([a, b]))
                i += 1
                continue  # good to here

            for k, j in enumerate(circuits):

                if a not in j and b in j:
                    circuits[k].add(a)
                    i += 1
                    break

                elif a in j and b not in j:
                    circuits[k].add(b)
                    i += 1
                    break

                elif a in j and b in j:
                    end += 1  # no connection is made so extra element needs to be checked
                    i += 1
                    break

                if k == len(circuits)-1 and a not in j and b not in j:
                    circuits.append(set([a, b]))
                    i += 1
                    break

        # run = True
        # while run:
        #     for i in range(len()):

        circuits.sort(key=lambda k: len(k), reverse=True)

        # TODO merge circuits is there is an overlap

        collector = 1
        for i in range(3):
            collector *= len(circuits[i])
        return collector

    def part2(self) -> int:
        return 0

# 4896 to low


# Puzzle8(EXAMPLE)
Puzzle8(INPUT)
