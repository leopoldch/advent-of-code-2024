# Third day of the Advent of Code 2024 Challenge
# author : Léopold Chappuis; leopold@lchappuis.fr
# Please acknowledge that this isn't the most efficient
# way to solve the problem.
# This has been done on purpose to keep the code simple
# and to do it as fast as possible.
import re


def part1(file):
    regex = r"mul\([0-9]+,[0-9]+\)"
    content = file.read()
    matches = re.findall(regex, content)
    total = 0
    for match in matches:
        match = match.replace("mul(", "")
        match = match.replace(")", "")
        numbers = match.split(",")
        total += int(numbers[0]) * int(numbers[1])
    print(total)


def part2(file):
    total = 0
    content = file.read()
    regex = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
    matches = re.findall(regex, content)
    mul_enabled = True
    for match in matches:
        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        elif mul_enabled and match.startswith("mul"):
            numbers = list(map(int, re.findall(r"\d+", match)))
            total += numbers[0] * numbers[1]
    print(total)


file = open("./data/d3.txt", "r")
part1(file)
part2(file)
