from itertools import product

# Seventh day of the Advent of Code 2024 Challenge
# author : Léopold Chappuis; leopold@lchappuis.fr
# Please acknowledge that this isn't the most efficient
# way to solve the problem.
# This has been done on purpose to keep the code simple
# and to do it as fast as possible.


def left_to_right_eval(expression):
    total = 0
    current = ""
    operator = "+"
    expression = expression.replace("||", "|")

    for char in expression:
        if char.isdigit():
            current += char
        else:
            if current:
                if operator == "+":
                    total += int(current)
                elif operator == "*":
                    total *= int(current)
                elif operator == "|":
                    total = int(str(total) + current)

            operator = char
            current = ""

    if current:
        if operator == "+":
            total += int(current)
        elif operator == "*":
            total *= int(current)
        elif operator == "|":
            total = int(str(total) + current)

    return total


def proceed_calculus(file, operators):
    lines = file.readlines()
    added = set()
    total = 0
    for line in lines:
        tab = line.split(":")
        result = int(tab[0])
        tab[1] = tab[1].replace("\n", "")
        numbers = tab[1].split(" ")
        numbers = [num for num in numbers if num]
        combinations = product(operators, repeat=len(numbers) - 1)
        for combo in combinations:
            expression = numbers[0]
            for i in range(len(combo)):
                expression += combo[i] + numbers[i + 1]
            calcul = left_to_right_eval(expression)
            if calcul == result and (line, result) not in added:
                added.add((line, result))
                total += result
    print(total)


def part1(file):
    operators = ["+", "*"]
    proceed_calculus(file, operators)


def part2(file):
    operators = ["*", "+", "||"]
    proceed_calculus(file, operators)


file = open("./data/d7.txt", "r")

#part1(file)
part2(file)
