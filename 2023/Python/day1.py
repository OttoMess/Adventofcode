
example = "2023/data/day1_example.txt"
data = "2023/data/day1.txt"
test = "2023/data/day1_test.txt"


def part1(file_path):
    collector = 0
    with open(file_path) as file:
        for j, line in enumerate(file):
            calibration_value = line.replace("\n", "")
            number_list = [c for c in calibration_value if c.isdigit()]
            number = number_list[0] + number_list[-1]
            collector += int(number)

    print(collector)


lookup = {'one': '1',
          'two': '2',
          "three": '3',
          "four": '4',
          "five": '5',
          "six": '6',
          "seven": '7',
          "eight": '8',
          "nine": '9'}

words = ['one', 'two', "three", "four", "five", "six", "seven", "eight", "nine"]


def part2(file_path):
    collector = 0
    with open(file_path) as file:
        for j, line in enumerate(file):
            calibration_value = line.replace("\n", "")
            length = len(calibration_value)
            number_value = None
            numbers = None
            breaker = False
            for i in words:
                for e in range(2, length):
                    test_section = calibration_value[0: e]
                    if i in test_section:
                        number_value = calibration_value.replace(i, lookup[i])
                        breaker = True
                        break
                    if breaker:
                        break
                if breaker:
                    break

            if number_value is None:
                number_value = calibration_value

            breaker = False
            for i in words:
                for e in range(2, len(number_value)):
                    test_section = number_value[-e:]
                    if i in test_section:
                        numbers = number_value.replace(i, lookup[i])
                        breaker = True
                        break
                    if breaker:
                        break
                if breaker:
                    break

            if numbers is None:
                numbers = number_value

            number_list = [c for c in numbers if c.isdigit()]
            number = number_list[0] + number_list[-1]
            print(calibration_value, number)
            collector += int(number)

    print(collector)


def part2_v1(file_path):
    collector_sum = 0
    with open(file_path) as file:
        for j, line in enumerate(file):
            value = line.replace("\n", "")
            pre_value = value
            collector = list()

            for e in range(0, len(value)):
                test_section = value[0: e+1]
                if value[e].isdigit():
                    collector.append(value[e])
                for i in words:
                    if i in test_section:
                        value = value[:e-2] + "_" + value[e-1:]
                        collector.append(lookup[i])

            number = collector[0] + collector[-1]
            print(pre_value, number)
            collector_sum += int(number)
    print(collector_sum)


part1(example)
part1(data)

part2_v1(test)
part2_v1(data)

# part2(test)
# part2(data)
