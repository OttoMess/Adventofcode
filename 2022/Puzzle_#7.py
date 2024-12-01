import time
from dataclasses import dataclass

EXAMPLE = "AoC_inputs/2022/day_7_example.txt"
INPUT = "AoC_inputs/2022/day_7.txt"


class puzzle7:
    def __init__(self, path):
        self.file_path = path
        self.input = list()
        self.total_size = 70000000
        self.needed_free = 30000000

        print(self.file_path)

        start_time = time.time()
        self.read_txt()
        dirs = self.build_structure()

        print(f"output part one: {self.find_xSize_dir(dirs, 100000)}")
        print(f"output part two: {self.find_dir_to_remove(dirs)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.input = data

    def build_structure(self):
        """
        using a string in dictionary to capture the directory location
        Tried pointing back to previous level so root/a/e include in e it is in a and a is in root. However this resulted in many nested loops.
        the Key of the dictionary is string with the structure of the folders. ":" is added for human readability
        """

        dirs = {"root": 0}
        depth = ["root"]
        current_dir = "root"
        for line in self.input:
            if line == "$ ls" or line == "$ cd /":
                continue

            elif line == "$ cd ..":
                dirs, current_dir, depth = self.step_back(dirs, current_dir, depth)

            elif line.startswith("$ cd "):
                s = line.split()
                depth.append(s[-1])
                current_dir += ":" + s[-1]

            elif "dir" in line:
                d = line.split()
                name = d[1]
                dirs[current_dir + ":" + name] = 0

            else:
                temp = line.split()
                file_size = int(temp[0])
                dirs[current_dir] += file_size

        while current_dir != "root":  # end of input back to root
            dirs, current_dir, depth = self.step_back(dirs, current_dir, depth)

        return dirs

    @staticmethod
    def step_back(dirs, current_dir, depth):
        prev_dir_size = dirs[current_dir]
        temp = ":" + depth.pop()
        q = current_dir.rfind(
            temp
        )  # could be multiply folder with same name, assure last folder is cut not on in the middle of the structure string.
        current_dir = current_dir[:q]
        dirs[current_dir] += prev_dir_size
        return dirs, current_dir, depth

    def find_xSize_dir(self, dirs, threshold):
        counter = 0
        for dir in dirs:
            if dirs[dir] < threshold:
                counter += dirs[dir]
        return counter

    def find_dir_to_remove(self, dirs):
        space_needed = dirs["root"] - (self.total_size - self.needed_free)
        smallest = "root"
        for dir in dirs:
            if dirs[dir] >= space_needed and dirs[dir] < dirs[smallest]:
                smallest = dir
        return dirs[smallest]


puzzle7(EXAMPLE)
puzzle7(INPUT)
