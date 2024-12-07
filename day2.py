# Second day of the Advent of Code 2024 Challenge
# author : Léopold Chappuis; leopold@lchappuis.fr
# Please acknowledge that this isn't the most efficient
# way to solve the problem.
# This has been done on purpose to keep the code simple
# and to do it as fast as possible.


def is_line_safe(numbers):
    signs = []
    while len(numbers) > 1:
        number1 = numbers[0]
        number2 = numbers[1]
        numbers = numbers[1:]
        if number1 - number2 > 0:
            signs.append(">")
            if "<" in signs:
                return False
        elif number1 - number2 < 0:
            signs.append("<")
            if ">" in signs:
                return False
        else:
            return False
        if abs(number1 - number2) > 3 or abs(number1 - number2) < 1:
            return False
    return True


def try_remove(tab):
    for i in range(len(tab)):
        new_tab = tab.copy()
        new_tab.pop(i)
        if is_line_safe(new_tab):
            return True
    return False


def part1(file):
    number_of_safe = 0
    for line in file:
        numbers = line.split()
        numbers = [int(i) for i in numbers]
        if is_line_safe(numbers):
            number_of_safe += 1
    print(number_of_safe)


def part2(file):
    number_of_safe = 0
    for line in file:
        numbers = line.split()
        numbers = [int(i) for i in numbers]
        if is_line_safe(numbers):
            number_of_safe += 1
        else:
            if try_remove(numbers):
                number_of_safe += 1
    print(number_of_safe)


file = open("./data/d2.txt", "r")
# part1(file)
part2(file)
