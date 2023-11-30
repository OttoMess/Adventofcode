
example = "Data/Puzzle_#1_example.txt"
data = "Data/Puzzle_#1.txt"
# test = "Data/Puzzle_#4_test.txt"


def part1(file_path):
    collector = 0
    with open(file_path) as file:
        for j,line in enumerate(file):
            planned = line.replace("\n","")
            first = planned.split(",")[0].split("-")
            second = planned.split(",")[1].split("-")

            if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
                print("first in second")
                print(first, second)
                collector += 1
                continue

            if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
                print("second in first")
                print(first, second)
                collector += 1

    print(collector)


part1(example)
