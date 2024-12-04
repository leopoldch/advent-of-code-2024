# Fourth day of the Advent of Code 2024 Challenge
# author : Léopold Chappuis; leopold@lchappuis.fr
# Please acknowledge that this isn't the most efficient
# way to solve the problem.
# This has been done on purpose to keep the code simple
# and to do it as fast as possible.


def verify_line(line: str):
    nb = 0
    s = "XMAS"
    nb += line.count(s)
    nb += line[::-1].count(s)
    return nb


def part1(file):
    nb = 0
    tab = [line.strip() for line in file.readlines()]
    rows = len(tab)
    cols = len(tab[0])

    for line in tab:
        nb += verify_line(line)

    for i in range(cols):
        col = "".join(row[i] for row in tab)  #
        nb += verify_line(col)

    for k in range(-rows + 1, cols):
        diagonal = "".join(
            tab[i][i + k] for i in range(max(0, -k), min(rows, cols - k))
        )
        nb += verify_line(diagonal)

    for k in range(rows + cols - 1):
        diagonal = "".join(
            tab[i][k - i] for i in range(max(0, k - cols + 1), min(rows, k + 1))
        )
        nb += verify_line(diagonal)

    print(nb)


def check_sub_matrix(matrix):
    if (
        matrix[0][0] == "M"
        and matrix[0][2] == "S"
        and matrix[1][1] == "A"
        and matrix[2][2] == "S"
        and matrix[2][0] == "M"
    ):
        return True
    return False


def rotate(matrix):
    return ["".join(row) for row in zip(*matrix[::-1])]


def flip_horizontal(matrix):
    return [row[::-1] for row in matrix]


def flip_vertical(matrix):
    return matrix[::-1]


def extract_sub_matrix(tab, x, y, size):
    if x + size > len(tab) or y + size > len(tab[0]):
        return
    return [line[y : y + size] for line in tab[x : x + size]]


def part2(file):
    tab = [line.strip() for line in file.readlines()]

    rows = len(tab)
    cols = len(tab[0])
    nb = 0

    for i in range(rows - 1):
        for j in range(cols - 1):
            sub_matrix = extract_sub_matrix(tab, i, j, 3)
            if sub_matrix is None:
                continue

            transformations = []
            current_matrix = sub_matrix
            for _ in range(4):
                transformations.append(current_matrix)
                transformations.append(flip_horizontal(current_matrix))
                transformations.append(flip_vertical(current_matrix))
                current_matrix = rotate(current_matrix)

            unique_transformations = set()
            for t in transformations:
                unique_transformations.add(tuple(map(tuple, t)))

            for transformed_matrix in unique_transformations:
                if check_sub_matrix(transformed_matrix):
                    nb += 1
                    break

    print(nb)


file = open("./data-j4.txt", "r")
part1(file)
part2(file)
