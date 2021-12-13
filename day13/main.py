from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

def part1(coordinates: list[tuple[int, int]], folds: list[tuple[str, int]], big_x: int, big_y: int) -> int:
    grid = [[0 for _ in range(big_x + 1)] for _ in range(big_y + 1)]
    for x, y in coordinates:
        grid[y][x] = 1

    for axis, value in folds[:1]:
        if axis == 'y':
            for row in range(value + 1, big_y + 1):
                for col in range(big_x + 1):
                    if grid[row][col] == 1:
                        grid[big_y - row][col] = 1
            grid = [[x for x in row] for row in grid[:value]]
            big_y = value - 1

        if axis == 'x':
            for row in range(big_y + 1):
                for col in range(value + 1, big_x + 1):
                    if grid[row][col] == 1:
                        grid[row][big_x - col] = 1
            grid = [[x for x in row[:value]] for row in grid]
            big_x = value - 1

    _sum = 0
    for row in grid:
        _sum += sum(row)
    return _sum


def part2(coordinates: list[tuple[int, int]], folds: list[tuple[str, int]], big_x: int, big_y: int) -> None:
    grid = [[0 for _ in range(big_x + 1)] for _ in range(big_y + 1)]
    for x, y in coordinates:
        grid[y][x] = 1

    for axis, value in folds:
        if axis == 'y':
            for row in range(value + 1, big_y + 1):
                for col in range(big_x + 1):
                    if grid[row][col] == 1:
                        grid[big_y - row][col] = 1
            grid = [[x for x in row] for row in grid[:value]]
            big_y = value - 1

        if axis == 'x':
            for row in range(big_y + 1):
                for col in range(value + 1, big_x + 1):
                    if grid[row][col] == 1:
                        grid[row][big_x - col] = 1
            grid = [[x for x in row[:value]] for row in grid]
            big_x = value - 1

    plt.imshow(np.array(grid))
    plt.show()


coordinates: list[tuple[int, int]] = []
folds: list[tuple[str, int]] = []
big_x = -1
big_y = -1
with open('input', 'r') as file:
    read_coordinates = True
    for line in file:
        line = line.strip()
        if read_coordinates and line:
            x, y = line.split(',')
            if int(x) > big_x:
                big_x = int(x)
            if int(y) > big_y:
                big_y = int(y)
            coordinates.append((int(x), int(y)))
            continue

        if not line:
            read_coordinates = False
            continue

        if not read_coordinates:
            axis, value = line.split('=')
            folds.append((axis[-1], int(value)))

print(f'{part1(coordinates, folds, big_x, big_y)=}')
print(f'{part2(coordinates, folds, big_x, big_y)=}')
