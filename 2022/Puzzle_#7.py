import time
from dataclasses import dataclass

EXAMPLE = "AoC_inputs/2022/day_7_example.txt"
INPUT = "AoC_inputs/2022/day_7.txt"


class puzzle7:
    def __init__(self, path):
        self.file_path = path
        self.input = list()

        print(self.file_path)

        start_time = time.time()
        self.read_txt()
        self.build_structure()

        # print(f"output part one: {self.find_marker(4)}")
        # print(f"output part two: {self.find_marker(14)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.input = data

    def build_structure(self):
        structure = list()
        collect = False
        for line in self.input:
            if collect:
                if "dir" in line:
                    cache.append(data(True, current_dir))
                else:
                    cache.append(data(False, current_dir))

            if line == "$ cd /":
                current_dir = "root"
            if line == "$ ls":
                collect = True
                cache = list()


@dataclass
class data:
    # name: str
    folder: bool
    lower_level: str = "none"
    size: int = 0


"""
command to read 
$ cd .. move back one directory
$ cd x  move into directory x
$ cd /  move to root directory

$ ls    creates a list with the current directory

build up data. needs to be able to nest dir in dir. 
possible use type ? file or dir 
if file store the size of the file 
dir should point toward lower level dir (or root) and have list of all files and dirs within the dir

"""
puzzle7(EXAMPLE)
