from functools import cache

with open("data/day12.txt", "r") as f: inputString = f.read().splitlines()


@cache
def checkPattern(pattern, amountsLeft, endOfDamaged=False):
    # if we have any amounts left, we fail else we pass
    if len(pattern) == 0: return 0 if len(amountsLeft) > 0 else 1

    # if there are any known #'s left, we fail else we pass
    if len(amountsLeft) == 0: return 0 if any(c == "#" for c in pattern) else 1

    # pattern starts with a . so we can ignore it
    if pattern[0] == ".": checkPattern(pattern[1:], amountsLeft)

    # we're supposed to end the group of damaged parts. If not we fail
    if endOfDamaged: return checkPattern(pattern[1:], amountsLeft) if pattern[0] != "#" else 0

    numberOfResults, currentAmount = 0, amountsLeft[0]
    # add the case if we're in the group of damaged parts
    if all(c != "." for c in pattern[:currentAmount]) and len(pattern) >= currentAmount:
        numberOfResults += checkPattern(pattern[currentAmount:], amountsLeft[1:], True)

    # add the case if we're not in the group of damaged parts
    if pattern[0] != "#":
        numberOfResults += checkPattern(pattern[1:], amountsLeft)

    return numberOfResults


def findSprings():
    inputs = []
    for line in inputString:
        pattern, amounts = line.split(" ")
        amounts = tuple([int(x) for x in amounts.split(",")])
        inputs.append([pattern, amounts])
    print(sum([checkPattern(pattern, amounts) for pattern, amounts in inputs]))

    bigInputs = []
    for i in inputs:
        pattern = "?".join([i[0]] * 5)
        amounts = i[1] * 5
        bigInputs.append([pattern, amounts])
    print(sum([checkPattern(pattern, amounts) for pattern, amounts in bigInputs]))


findSprings()