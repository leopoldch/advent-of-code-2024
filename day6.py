# Sixth day of the Advent of Code 2024 Challenge
# author : Léopold Chappuis; leopold@lchappuis.fr
# Please acknowledge that this isn't the most efficient
# way to solve the problem.
# This has been done on purpose to keep the code simple
# and to do it as fast as possible.
import os
import time


class Plate:

    def __init__(self, grid) -> None:

        self.plate = grid
        self.width = len(grid[0]) - 1
        self.height = len(grid) - 1
        self.last_guard_position = (0, 0)
        self.path = []

        directions = [">", "<", "^", "v"]
        for y in range(self.height):
            for x in range(self.width):
                if self.plate[y][x] in directions:
                    self.last_guard_position = (x, y)

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.plate])

    def get_guard_position(self):
        return self.last_guard_position

    def get_direction(self):
        return self.plate[self.last_guard_position[1]][self.last_guard_position[0]]

    def is_blocked(self, x, y):
        if x < 0 or x >= self.width + 1 or y < 0 or y >= self.height + 1:
            return False
        return self.plate[y][x] == "#"

    def choose_direction(self, x, y, direction):
        match direction:
            case ">":
                if self.is_blocked(x + 1, y):
                    return self.choose_direction(x, y, "v")
                return ((x + 1, y), ">")
            case "<":
                if self.is_blocked(x - 1, y):
                    return self.choose_direction(x, y, "^")
                return ((x - 1, y), "<")
            case "^":
                if self.is_blocked(x, y - 1):
                    return self.choose_direction(x, y, ">")
                return ((x, y - 1), "^")
            case "v":
                if self.is_blocked(x, y + 1):
                    return self.choose_direction(x, y, "<")
                return ((x, y + 1), "v")
            case _:
                raise Exception("Guard is in an unknown direction")

    def get_next_allowed_move(self):
        x, y = self.get_guard_position()
        direction = self.get_direction()
        return self.choose_direction(x, y, direction)

    def update_guard_position(self, x, y, sign):
        last = self.get_guard_position()
        self.plate[last[1]][last[0]] = "X"
        self.last_guard_position = (x, y)
        self.plate[y][x] = sign
        self.path.append(((x, y), sign))

    def path_has_been_visited_twice(self):
        return len(set(self.path)) != len(self.path)

    def move_guard(self, x, y, sign):
        if (x, y) == self.last_guard_position:
            print("Guard is already here")
            return
        allowed_x = [x - 1, x, x + 1]
        allowed_y = [y - 1, y, y + 1]
        if x < 0 or x >= self.width + 1 or y < 0 or y >= self.height + 1:
            self.last_guard_position = (-1, -1)
            return
        if x not in allowed_x or y not in allowed_y:
            print("Guard can't move to this position")
            return
        self.update_guard_position(x, y, sign)
        # self.print_advancement(40)

    def print_advancement(self, size=20):
        x, y = self.get_guard_position()

        half_size = size // 2
        start_x = max(0, x - half_size)
        end_x = min(self.width + 1, x + half_size + 1)
        start_y = max(0, y - half_size)
        end_y = min(self.height + 1, y + half_size + 1)

        os.system("clear")
        for row in self.plate[start_y:end_y]:
            colored_row = ""
            for char in row[start_x:end_x]:
                if char == "#":
                    colored_row += f"\033[31m{char}\033[0m"
                elif char == "X":
                    colored_row += f"\033[33m{char}\033[0m"
                elif char in "><^v":
                    colored_row += f"\033[32m{char}\033[0m"
                else:
                    colored_row += char
            print(colored_row)

    def get_result(self):
        self.plate[self.last_guard_position[1]][self.last_guard_position[0]] = "X"
        total = sum([row.count("X") for row in self.plate])
        print(f"The guard has visited {total} cells")


def part1(file):
    lines = file.readlines()
    plate = Plate([list(line.strip()) for line in lines])
    while plate.last_guard_position != (-1, -1):
        tup, sign = plate.get_next_allowed_move()
        plate.move_guard(tup[0], tup[1], sign)
    plate.get_result()


def part2(file):
    # NOTE: This is a very inefficient way to solve the problem
    total = 0
    lines = [line.strip() for line in file]
    original = Plate([list(line) for line in lines])
    direction = original.get_direction()
    del original

    for i in range(len(lines) - 1):

        for j in range(len(lines[i]) - 1):
            if lines[i][j] == "#" or lines[i][j] == direction:
                continue

            lines[i] = lines[i][:j] + "#" + lines[i][j + 1 :]
            plate = Plate([list(line) for line in lines])

            while plate.last_guard_position != (-1, -1):
                tup, sign = plate.get_next_allowed_move()
                plate.move_guard(tup[0], tup[1], sign)
                if plate.path_has_been_visited_twice():
                    total += 1
                    print(f"Total of infinite loops : {total}")
                    break

            del plate

            lines[i] = lines[i][:j] + "." + lines[i][j + 1 :]

    print(f"Total of infinite loops : {total}")


file = open("./data-j6.txt", "r")
# part1(file)
part2(file)
