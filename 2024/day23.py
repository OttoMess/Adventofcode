import time


EXAMPLE = "AoC_inputs/2024/day_23_example.txt"
INPUT = "AoC_inputs/2024/day_23.txt"

"""
3 way = 
a-b
b-c
c-a
2 pairs in total
"""


class Puzzle23:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        computers = set()
        links = set()
        with open(self.file_path) as file:
            for line in file:
                a, b = line.strip().split("-")
                computers.update([a, b])
                links.update([(a, b), (b, a)])
                data.append((a, b))
        self.links = data
        return computers, links

    def part1(self):
        queue = [i for i in self.links]
        three_way = list()
        ts = list()
        while len(queue) > 0:
            a, b = queue.pop()
            possible_c = list()

            for c in queue:
                if c[0] == a:
                    possible_c.append(c[1])
                elif c[1] == a:
                    possible_c.append(c[0])
            # found a-b link and possible a-c links

            # looking for the b-c link
            for c in possible_c:
                for k in queue:
                    if k[0] == c and k[1] == b or k[0] == b and k[1] == c:
                        three_way.append(a + "," + b + "," + c)
                        ts.append(a[0] + b[0] + c[0])
        counter = 0
        for k in ts:
            if "t" in k:
                counter += 1
        return counter

    def part2(self):
        computers, connections = self.read_txt()
        networks = [{c} for c in computers]  # start network search for each computer
        for net in networks:
            for com in computers:
                # check if for new  computer if connection is there to all other computers in network
                # if so add computer to network
                tester = [(com, d) in connections for d in net]
                if all(tester):
                    net.add(com)

        # networks has doubles, just need to find the largest
        largest = list(sorted(networks, key=lambda s: len(s))[-1])
        # arrange the PC is correct order
        largest.sort()
        return ",".join(i for i in largest)


Puzzle23(EXAMPLE)
Puzzle23(INPUT)
