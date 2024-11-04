import string

# file_path = "day#3_test.txt"
file_path = "2023/data/day#3.txt"

letters = string.ascii_letters

collector_1 = 0
collector_2 = 0
group = str()
with open(file_path) as file:
    for j,line in enumerate(file):
        content = line.replace("\n","")
        n = int(len(content)/2)
        front = set(content[:n])
        rear = set(content[n:])
        item = [i for i in front if i in rear]
        collector_1 += 1 + letters.find(item[0])

        "for the second part of the question"

        if j % 3 == 0:
            elf_1 = "".join(set(content))
        if j % 3 == 1:
            elf_2 = "".join(set(content))
        if j % 3 == 2:
            elf_3 = "".join(set(content))
            badge = [i for i in elf_3 if i in elf_1 and i in elf_2]
            collector_2 += 1 + letters.find(badge[0])

print(f"Value of the unique items = {collector_1}")
print(f"Value of the badges  = {collector_2}")
