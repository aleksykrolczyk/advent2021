from pprint import pprint


def get_neighbours(map: list[list[int]], i: int, j: int) -> list[tuple[int, int]]:
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if i + 1 < len(map):
        neighbours.append((i + 1, j))
    if j + 1 < len(map[0]):
        neighbours.append((i, j + 1))
    return neighbours


def part1(cavern: list[list[int]]) -> int:
    width, height = len(cavern[0]), len(cavern)
    distances = [[float("inf") for _ in range(width)] for _ in range(height)]
    distances[0][0] = 0

    visited: set[tuple[int, int]] = set()

    queue = [[(0, 0), 0]]
    while queue:
        if distances[height - 1][width - 1] != float("inf"):
            return int(distances[height - 1][width - 1])
        queue.sort(key=lambda x: x[1])
        coords, dist = queue.pop(0)
        # print(coords)
        visited.add(coords)

        x, y = coords
        for a, b in get_neighbours(cavern, x, y):
            if (a, b) not in visited:
                new_dist = distances[x][y] + cavern[a][b]
                if new_dist < distances[a][b]:
                    distances[a][b] = new_dist
                    queue.append([(a, b), new_dist])

    return int(distances[height - 1][width - 1])


def part2(cavern: list[list[int]]) -> int:
    width, height = len(cavern[0]), len(cavern)
    distances = [[float("inf") for _ in range(width)] for _ in range(height)]
    distances[0][0] = 0

    visited: set[tuple[int, int]] = set()

    queue = [[(0, 0), 0]]
    while queue:
        if distances[height - 1][width - 1] != float("inf"):
            return int(distances[height - 1][width - 1])
        queue.sort(key=lambda x: x[1])
        coords, dist = queue.pop(0)
        # print(coords)
        visited.add(coords)

        x, y = coords
        for a, b in get_neighbours(cavern, x, y):
            if (a, b) not in visited:
                new_dist = distances[x][y] + cavern[a][b]
                if new_dist < distances[a][b]:
                    distances[a][b] = new_dist
                    queue.append([(a, b), new_dist])

    return int(distances[height - 1][width - 1])


def expand(cavern: list[list[int]]) -> list[list[int]]:
    width, height = len(cavern[0]), len(cavern)
    new_cavern = [[-1 for _ in range(width * 5)] for _ in range(height * 5)]
    for i in range(height):
        for j in range(width):
            for k in range(5):
                for p in range(5):
                    a = cavern[i][j] + k + p
                    x = a if a <= 9 else (a % 10) + 1
                    new_cavern[i + width*k][j + height*p] = x

    # for row in new_cavern:
    #     print(row)
    return new_cavern


cavern: list[list[int]] = []
with open('input', 'r') as file:
    for line in file:
        cavern.append([int(x) for x in line.strip()])

print(cavern)
print(f'{part1(cavern)=}')
print(f'{part2(expand(cavern))=}')
