import time


EXAMPLE = "AoC_inputs/2024/day_19_example.txt"
INPUT = "AoC_inputs/2024/day_19.txt"

# https://www.geeksforgeeks.org/number-of-ways-to-form-a-given-string-from-the-given-set-of-strings/


class Puzzle19:
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
        self.patterns = list()
        with open(self.file_path) as file:
            for i, line in enumerate(file):
                if i == 0:
                    self.towels = [i.strip() for i in line.strip().split(",")]
                elif i > 1:
                    self.patterns.append(line.strip())

    def shorten_towels(self, towels: list):
        # sorting by length, longer towels could be made from shorter but not the other way around
        towels.sort(key=lambda s: len(s))
        self.small = len(towels[0])  # used in self.possible
        self.large = len(towels[-1])  # used in self.possible

        pruned = set()
        for towel in towels:
            if self.possible(towel, pruned):
                continue
            else:
                pruned.add(towel)

        lengths = [len(i) for i in pruned]
        self.small = min(lengths)
        self.large = max(lengths)
        return set([i for i in pruned])

    def part1(self):
        towels = self.shorten_towels(self.towels)
        counter = 0
        for i, p in enumerate(self.patterns):
            if self.possible(p, towels):
                counter += 1
        return counter

    def part2(self):
        str = self.patterns[0]
        dictionary = self.towels
        m = 14
        root = Trie()

        # Construct trie
        for i in range(m):
            self.insert(root, dictionary[i][::-1])

        # Function call
        print(self.waysOfFormingString(root, str))
        # way to slow for questions for part 2
        counter = 0
        for i, p in enumerate(self.patterns):
            sub_set = self.towels_in_patterns(p)
            if self.possible(p, sub_set):
                counter += 1
            print(i)
        return counter

    def possible(self, pattern, towels):
        # recursive function which return true of possible combination found
        if len(pattern) == 0:
            return True
        elif len(pattern) >= self.large:
            view = range(self.small, self.large + 1)
        else:
            view = range(self.small, len(pattern) + 1)

        for i in view:
            if pattern[0:i] in towels:
                if self.possible(pattern[i:], towels):
                    return True
        return False

    def towels_in_patterns(self, pattern: str):
        # reduce the set with towels which are possible within pattern
        towels = set()
        for towel in self.towels:
            if pattern.find(towel) != -1:
                towels.add(towel)
        return towels

    # Inserting the strings into trie
    def insert(root, s):
        n = len(s)
        prev = root
        for i in range(n):
            index = ord(s[i]) - ord("a")
            if prev.children[index] is None:
                prev.children[index] = Trie()
            prev = prev.children[index]
        prev.endOfWord = True

    # Function to find number of ways
    # of forming string str
    def waysOfFormingString(root, s):
        n = len(s)

        # Count[] to store the answer
        # of prefix string str[0....i]
        count = [0] * n
        for i in range(n):
            ptr = root
            for j in range(i, -1, -1):
                ch = s[j]

                # If not found, break
                # out from loop
                index = ord(ch) - ord("a")
                if ptr.children[index] is None:
                    break
                ptr = ptr.children[index]

                # String found, update the
                # count(i)
                if ptr.endOfWord:
                    if j > 0:
                        count[i] += count[j - 1]
                    else:
                        count[i] += 1
        return count[n - 1]


class Trie:
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26


Puzzle19(EXAMPLE)
Puzzle19(INPUT)
