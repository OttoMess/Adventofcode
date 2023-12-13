
EXAMPLE = "data/day2_example.txt"
DATA = "data/day2.txt"
# test = "data/day2_test.txt"


def part1(file_path):
    collector = 0
    with open(file_path) as file:
        for j, line in enumerate(file):
            game = line.replace("\n", "").split(":")
            game_id = game[0].replace("Game ", "")
            shows = [s.split(",") for s in game[1].split(";")]

            e = check_plays(shows)

            collector += int(game_id) * e
    print(collector)


def check_plays(s):

    for i in s:
        for k in i:
            amount, color = k[1:].split(" ")
            amount = int(amount)
            if amount < 12:
                continue
            elif color == "blue" and amount > 14:
                return 0
            elif color == "green" and amount > 13:
                return 0
            elif color == "red" and amount > 12:
                return 0

    return 1


part1(EXAMPLE)
part1(DATA)


def part2(file_path):
    collector = 0
    with open(file_path) as file:
        for j, line in enumerate(file):
            game = line.replace("\n", "").split(":")
            shows = [s.split(",") for s in game[1].split(";")]

            b, r, g = amount_of_cubes(shows)
            print(f"Blue: {b}, Red: {r}, Green: {g}")
            collector += b * r * g
    print(collector)


def amount_of_cubes(s):
    b, r, g = 0, 0, 0
    for i in s:
        for k in i:
            amount, color = k[1:].split(" ")
            amount = int(amount)
            if color == "blue" and amount > b:
                b = amount
            elif color == "green" and amount > g:
                g = amount
            elif color == "red" and amount > r:
                r = amount
    return b, r, g


part2(EXAMPLE)
part2(DATA)
