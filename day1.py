# First day of the Advent of Code 2024 Challenge
# author : Léopold Chappuis; leopold@lchappuis.fr
# Please acknowledge that this isn't the most efficient
# way to solve the problem.
# This has been done on purpose to keep the code simple
# and to do it as fast as possible.


def part1(file):
    tab_left = []
    tab_right = []
    total = 0

    for line in file:
        i1, i2 = line.split()
        tab_left.append(i1)
        tab_right.append(i2)

    tab_left.sort()
    tab_right.sort()

    for i in range(len(tab_left)):
        total += abs(int(tab_right[i]) - int(tab_left[i]))

    print(total)


def part2(file):
    tab_left = []
    tab_right = []
    total = 0

    for line in file:
        i1, i2 = line.split()
        tab_left.append(i1)
        tab_right.append(i2)

    for number in tab_left:
        total += int(number) * tab_right.count(number)

    print(total)


file = open("./data-j1.txt", "r")
#part1(file)
part2(file)
