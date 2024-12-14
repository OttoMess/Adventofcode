import shutil
import os

day_number = input(f"type day number to add: \n")

try:
    val = int(day_number)
except ValueError:
    print("That's not an int, exiting script")
    exit()


base = "AoC_inputs/2024/"
day = base + "day_" + day_number + ".txt"
example = base + "day_" + day_number + "_example.txt"
python = "./2024/day" + day_number + ".py"

if not os.path.exists(day):
    open(day, "a").close()
    print(f"made: {day}")
else:
    print(f"already exists: {day}")

if not os.path.exists(example):
    open(example, "a").close()
    print(f"made: {example}")
else:
    print(f"already exists: {example}")

if not os.path.exists(python):
    shutil.copyfile("./2024/blank.txt", python)
    print(f"made: {"/2024/day" + day_number + ".py"}")

    with open(r"2024/day" + day_number + ".py", "r") as file:
        data = file.read()

        for _ in range(5):
            w = data.index("q")
            data = data[:w] + day_number + data[w + 1 :]

    with open(r"2024/day" + day_number + ".py", "w") as file:
        file.write(data)
else:
    print(f"already exists: {python}")
