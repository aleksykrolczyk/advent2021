from dataclasses import dataclass
from pprint import pprint


@dataclass
class Point:
    x: int
    y: int


def part1(points: list[tuple[Point, Point]], maxx: int, maxy: int) -> int:
    grid = [[0 for x in range(maxx + 1)] for y in range(maxy + 1)]
    for p1, p2 in points:
        if p1.x == p2.x:
            bigger, smaller = max(p1.y, p2.y), min(p1.y, p2.y)
            diff = bigger - smaller
            for i in range(diff + 1):
                grid[p1.x][smaller + i] += 1
            continue

        elif p1.y == p2.y:
            bigger, smaller = max(p1.x, p2.x), min(p1.x, p2.x)
            diff = bigger - smaller
            for i in range(diff + 1):
                grid[smaller + i][p1.y] += 1
            continue

    # pprint([*zip(*grid)])

    c = 0
    for row in grid:
        for elem in row:
            if elem >= 2:
                c += 1
    return c


def part2(points: list[tuple[Point, Point]], maxx: int, maxy: int) -> int:
    grid = [[0 for x in range(maxx + 1)] for y in range(maxy + 1)]
    for p1, p2 in points:
        if p1.x == p2.x:
            bigger, smaller = max(p1.y, p2.y), min(p1.y, p2.y)
            diff = bigger - smaller
            for i in range(diff + 1):
                grid[p1.x][smaller + i] += 1
            continue

        elif p1.y == p2.y:
            bigger, smaller = max(p1.x, p2.x), min(p1.x, p2.x)
            diff = bigger - smaller
            for i in range(diff + 1):
                grid[smaller + i][p1.y] += 1

        else:
            diff = abs(p1.x - p2.x)
            smallerx = min(p1.x, p2.x)
            line = lambda x: (p1.y - p2.y) / (p1.x - p2.x) * x + (p1.y - (p1.y - p2.y) / (p1.x - p2.x) * p1.x)
            for i in range(diff + 1):
                grid[smallerx + i][int(line(smallerx + i))] += 1

    c = 0
    for row in grid:
        for elem in row:
            if elem >= 2:
                c += 1
    return c


points: list[tuple[Point, Point]] = []
maxx, maxy = -1, -1
with open('input', 'r') as file:
    for line in file:
        p1, p2 = line.strip().split('->')
        p1x, p1y = p1.split(',')
        p2x, p2y = p2.split(',')
        p1x, p1y = int(p1x), int(p1y)
        p2x, p2y = int(p2x), int(p2y)

        if p1x > maxx: maxx = p1x
        if p2x > maxx: maxx = p2x
        if p1y > maxy: maxy = p1y
        if p2y > maxy: maxy = p2y

        points.append((Point(x=p1x, y=p1y), Point(x=p2x, y=p2y)))

print(f'{part1(points, maxx, maxy)=}')
print(f'{part2(points, maxx, maxy)=}')
