import numpy as np
import matplotlib.pyplot as plt

def get_neighbours(map: list[list[int]], i: int, j: int) -> list[tuple[int, tuple[int, int]]]:
    neighbours = []
    if i > 0:
        neighbours.append((map[i - 1][j], (i - 1, j)))
    if j > 0:
        neighbours.append((map[i][j - 1], (i, j - 1)))
    if i + 1 < len(map):
        neighbours.append((map[i + 1][j], (i + 1, j)))
    if j + 1 < len(map[0]):
        neighbours.append((map[i][j + 1], (i, j + 1)))
    return neighbours


def part1(heatmap: list[list[int]]) -> int:
    _sum = 0
    for i in range(len(heatmap)):
        for j in range(len(heatmap[0])):
            neighbours = get_neighbours(heatmap, i, j)
            current = heatmap[i][j]
            if all(n[0] > current for n in neighbours):
                _sum += current + 1
    return _sum


def part2(heatmap: list[list[int]]) -> int:
    ALREADY_VISITED: list[tuple[int, int]] = []
    ABC = [[0 for _ in range(len(heatmap[0]))] for _ in range(len(heatmap))]

    def get_basin_size(heatmap: list[list[int]], i: int, j: int) -> int:
        current = heatmap[i][j]
        ABC[i][j] += current
        neighbours = get_neighbours(heatmap, i, j)

        if (i, j) in ALREADY_VISITED:
            return 0

        ALREADY_VISITED.append((i, j))
        visitable = [
            n for n in neighbours if n[0] - current >= 1 and n[0] != 9 and (n[1][0], n[1][1])
        ]

        if not visitable:
            return 1

        return 1 + sum(get_basin_size(heatmap, n[1][0], n[1][1]) for n in visitable)

    basins: list[int] = []
    for i in range(len(heatmap)):
        for j in range(len(heatmap[0])):
            neighbours = get_neighbours(heatmap, i, j)
            current = heatmap[i][j]
            if all(n[0] > current for n in neighbours):
                basins.append(get_basin_size(heatmap, i, j))
                ABC[i][j] = 9

    basins.sort(reverse=True)
    # print(basins)
    # for row in ABC:
    #     print(row)
    # plt.imshow(np.array(ABC))
    # plt.show()
    return basins[0] * basins[1] * basins[2]


heatmap: list[list[int]] = []
with open('input', 'r') as file:
    for line in file:
        heatmap.append([int(x) for x in line.strip()])


print(f'{part1(heatmap)=}')
print(f'{part2(heatmap)=}')
