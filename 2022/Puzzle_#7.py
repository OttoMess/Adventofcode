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
        dirs = self.build_structure()

        print(f"output part one: {self.find_xSize_dir(dirs, 100000)}")
        # print(f"output part two: {self.find_marker(14)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                data.append(line.strip())
        self.input = data

        # def build_structure(self):
        # dirs = [directory("root", "none", list(), 0, list())]
        # files = list()

        # for line in self.input:
        #     if line == "$ cd /":
        #         depth = [dirs[0].name]
        #     elif line == "$ ls":
        #         continue
        #     elif line == "$ cd ..":
        #         depth.pop()
        #     elif line.startswith("$ cd "):
        #         s = line.split()
        #         depth.append(s[-1])

        #     else:
        #         # cache.append(line)

        #         if "dir" in line:
        #             d = line.split()
        #             name = d[1]
        #             for dir in dirs:
        #                 if dir.name == depth[-1]:
        #                     dir.sub_folders.append(d[1])
        #                     break
        #             dirs.append(
        #                 directory(name, depth[-1], list(), len(depth), depth[:])
        #             )

        #             if len(depth) > self.levels:
        #                 self.levels = len(depth)
        #                 # find the highest level of dir in dirs

        #         else:
        #             temp = line.split()
        #             size = int(temp[0])
        #             if "." in temp[1]:
        #                 x = temp[1].split(".")
        #                 name = x[0]
        #                 file_type = x[1]
        #             else:
        #                 name = temp[1]
        #                 file_type = "none"
        #             files.append(file(size, name, depth[-1], file_type, depth[:]))
        # self.files = files
        # return dirs

    def build_structure(self):
        dirs = {"root": 0}
        depth = ["root"]
        current_dir = "root"
        for line in self.input:
            if line == "$ ls" or line == "$ cd /":
                continue

            elif line == "$ cd ..":
                prev_dir_size = dirs[current_dir]
                temp = ":" + depth.pop()
                q = current_dir.rfind(temp)
                current_dir = current_dir[:q]
                dirs[current_dir] += prev_dir_size

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

        return dirs

    def find_xSize_dir(self, dirs, threshold):
        counter = 0
        for dir in dirs:
            if dirs[dir] < threshold:
                counter += dirs[dir]
        return counter


@dataclass
class directory:
    name: str
    directory: str  # the directory the directory is located
    sub_folders: list  # list of the files and folders in this directory
    level: int
    chain: list
    size: int = 0


@dataclass
class file:
    size: int
    name: str
    directory: str  # the directory the file is located
    type: str
    chain: list


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
puzzle7(INPUT)
