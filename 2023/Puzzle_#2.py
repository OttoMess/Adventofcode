
example = "Data/Puzzle_#2_example.txt"
data = "Data/Puzzle_#2.txt"
# test = "Data/Puzzle_#2_test.txt"


def part1(file_path):
    collector = 0
    with open(file_path) as file:
        for j, line in enumerate(file):
            calibration_value = line.replace("\n", "")