# Fifth day of the Advent of Code 2024 Challenge
# author : Léopold Chappuis; leopold@lchappuis.fr
# Please acknowledge that this isn't the most efficient
# way to solve the problem.
# This has been done on purpose to keep the code simple
# and to do it as fast as possible.


def parse_input(file_content):

    lines = file_content.strip().split("\n")
    rules = {}
    updates = []
    is_rule_section = True

    for line in lines:
        if "|" in line and is_rule_section:
            before, after = map(int, line.split("|"))
            if not before in rules:
                rules[before] = []
            rules[before].append(after)
        elif "," in line:
            is_rule_section = False
            updates.append(list(map(int, line.split(","))))
    return rules, updates


def get_last_position(number, tab, rules):
    if number not in rules:
        return len(tab) - 1
    last_index = -1
    for cur in tab:
        if cur not in rules:
            continue
        if number in rules[cur]:
            last_index = tab.index(cur)
    return last_index


def sort_list(rules, tab):
    sorted = []
    for number in tab:
        last_index = get_last_position(number, sorted, rules)
        if last_index == -1:
            sorted.insert(0, number)
            continue
        sorted.insert(last_index + 1, number)
    return sorted


def is_valid(rules, tab):
    for number in tab:
        for cur in tab[tab.index(number) + 1 :]:
            if cur not in rules:
                continue
            if number in rules[cur]:
                return False
    return True


def part1(file):
    total = 0
    content = file.read()
    rules, data = parse_input(content)
    for input in data:
        if is_valid(rules, input):
            total += input[len(input) // 2]
    print(total)


def part2(file):
    total = 0
    content = file.read()
    rules, data = parse_input(content)
    for input in data:
        if is_valid(rules, input):
            continue
        sorted = sort_list(rules, input)
        total += sorted[len(sorted) // 2]
    print(total)


file = open("./data-j5.txt", "r")
# part1(file)
part2(file)
