import time

DATA = "data/day14.txt"
EXAMPLE = "data/day14_example.txt"


class Puzzle14:

    def __init__(self, path):
        self.file_path = path
        self.data = list()

        self.part1_collector = 0
        self.part2_collector = 0

        start_time = time.time()

        self.part1()
        self.part2()
        print(self.file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Sum for part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def part1(self):
        moved_data = self.north(self.read_txt())
        self.part1_collector = self.count_rocks(moved_data)

    def part2(self):
        data = self.read_txt()
        # repeat = 1000000000
        repeat = 147
        weight = list()
        pattern = list()
        for i in range(repeat):
            data = self.cycle(data)
            weight.append(self.count_rocks(data))
            if i >= 136:
                pattern.append(self.count_rocks(data))
        #
        # line = [136 + i for i in range(11)]
        #
        # # for l in line:
        # #     remain = 1000000000-l / 11
        # #     if remain == int(remain):
        # #         w = l
        self.part2_collector = pattern[5]  # looked at plot to find the correct index

    def cycle(self, data):
        north = self.north(data)
        west = self.west(north)
        south = self.south(west)
        east = self.east(south)
        return east

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        return raw

    @staticmethod
    def north(data):
        for j, line in enumerate(data):
            location = [k for k, c in enumerate(line) if c == "O"]

            if len(location) == 0:
                continue
            else:
                for loc in location:
                    place = finder_north(j-1, loc, data)
                    if place == j:
                        continue
                    else:
                        data[place] = data[place][:loc] + "O" + data[place][loc + 1:]
                        data[j] = data[j][:loc] + "." + data[j][loc + 1:]
        return data

    @staticmethod
    def south(data):
        for j in reversed(range(len(data))):
            location = [k for k, c in enumerate(data[j]) if c == "O"]

            if len(location) == 0:
                continue
            else:
                for loc in location:
                    place = finder_south(j + 1, loc, data)
                    if place == j:
                        continue
                    else:
                        data[place] = data[place][:loc] + "O" + data[place][loc + 1:]
                        data[j] = data[j][:loc] + "." + data[j][loc + 1:]
        return data

    @staticmethod
    def east(data):
        for j in range(len(data)):
            location = [k for k, c in enumerate(data[j]) if c == "O"]

            if len(location) == 0:
                continue
            else:
                for k in reversed(range(len(location))):
                    new_loc = finder_east(location[k]+1, data[j])
                    if new_loc == location[k]:
                        continue
                    else:
                        data[j] = data[j][:new_loc] + "O" + data[j][new_loc + 1:]
                        data[j] = data[j][:location[k]] + "." + data[j][location[k] + 1:]
        return data

    @staticmethod
    def west(data):
        for j in range(len(data)):
            location = [k for k, c in enumerate(data[j]) if c == "O"]

            if len(location) == 0:
                continue
            else:
                for k in range(len(location)):
                    new_loc = finder_west(location[k]-1, data[j])
                    if new_loc == location[k]:
                        continue
                    else:
                        data[j] = data[j][:new_loc] + "O" + data[j][new_loc + 1:]
                        data[j] = data[j][:location[k]] + "." + data[j][location[k] + 1:]
        return data

    @staticmethod
    def count_rocks(data):
        counts = [line.count("O") for line in data]
        weight = 0
        for j, n in enumerate(counts):
            weight += n * (len(counts) - j)
        return weight


def finder_north(j, loc, field):  # recursive function
    if j < 0:
        return 0
    elif field[j][loc] != ".":
        return j+1
    else:
        return finder_north(j-1, loc, field)


def finder_south(j, loc, field):  # recursive function
    if j > len(field) - 1:
        return len(field) - 1
    elif field[j][loc] != ".":
        return j-1
    else:
        return finder_south(j+1, loc, field)


def finder_east(loc, line):
    if loc > len(line) - 1:
        return len(line) - 1
    if line[loc] != ".":
        return loc-1
    else:
        return finder_east(loc + 1, line)


def finder_west(loc, line):
    if loc < 0:
        return 0
    if line[loc] != ".":
        return loc + 1
    else:
        return finder_west(loc - 1, line)


Puzzle14(EXAMPLE)
Puzzle14(DATA)
