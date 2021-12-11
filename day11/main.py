from pprint import pprint
from typing import Any

STEPS = 100


class Octopus:
    def __init__(self, energy: int) -> None:
        self.energy = energy

    def incr(self) -> bool:
        self.energy += 1
        if self.energy > 9:
            self.energy = 0
            return True
        return False

    def __repr__(self) -> str:
        return f'{self.energy}'


def get_neighbors(grid: list[list[Any]], row: int, col: int) -> list[tuple[int, int]]:
    neighbors = []
    row_length, col_length = len(grid[0]), len(grid)

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if (0 <= row + i <= row_length - 1) and (0 <= col + j <= col_length - 1):
                neighbors.append((row + i, col + j))
    return neighbors


def flash(octopuses: list[list[Octopus]], row: int, col: int, already_flashed: list[list[int]]) -> int:
    if already_flashed[row][col]:
        return 0

    no_flashes = 0
    if octopuses[row][col].incr():
        already_flashed[row][col] = 1
        for i, j in get_neighbors(octopuses, row, col):
            if already_flashed[i][j]:
                continue
            no_flashes += flash(octopuses, i, j, already_flashed)
        return 1 + no_flashes
    return 0


def part1(octopuses: list[list[Octopus]]) -> int:
    num_flashes = 0
    for i in range(STEPS):
        already_flashed = [[0 for _ in octopuses[0]] for _ in octopuses]
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                flashes = flash(octopuses, row, col, already_flashed)
                num_flashes += flashes
    return num_flashes


def part2(octopuses: list[list[Octopus]]) -> int:
    step = 0
    while True:
        num_flashes = 0
        already_flashed = [[0 for _ in octopuses[0]] for _ in octopuses]
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                flashes = flash(octopuses, row, col, already_flashed)
                num_flashes += flashes

        if all(all(x for x in row) for row in already_flashed):
            return step + 1
        step += 1


octopuses: list[list[Octopus]] = []
with open('input', 'r') as file:
    for line in file:
        octopuses.append([Octopus(int(x)) for x in line.strip()])


# print(f'{part1(octopuses)=}')
print(f'{part2(octopuses)=}')