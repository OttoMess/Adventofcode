"""
test on the working of a recursive function /script
"""

data = "......#"


def finder(loc):
    print(data[loc])
    if data[loc] == "#":
        return loc
    else:
        return finder(loc + 1)


e = finder(0)

print(e, data[e])
