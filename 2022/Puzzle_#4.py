"""
https://adventofcode.com/2022/day/4
"""

example = "2023/data/day#4_example.txt"
data = "2023/data/day4.txt"
test = "2023/data/day4_test.txt"


def part1(file_path):
    collector = 0
    group = str()
    with open(file_path) as file:
        for j, line in enumerate(file):
            planned = line.replace("\n", "")
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


def part2(file_path):
    collector = 0
    with open(file_path) as file:
        for j, line in enumerate(file):
            planned = line.replace("\n", "")
            first = planned.split(",")[0].split("-")
            second = planned.split(",")[1].split("-")

            if int(first[1]) < int(second[0]) or int(first[0]) > int(second[1]):
                print("No Overlap")
                print(first, second)
                continue
            else:
                print("Overlap")
                print(first, second)
                collector += 1
    print(f"Output part two : {collector}")


part2(data)
