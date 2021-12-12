from collections import defaultdict, Counter
from pprint import pprint


def part1(connections: dict[str, set[str]]) -> int:
    unique_paths: list[list[str]] = []

    def explore(cave: str, path_so_far: list[str]):
        if cave == 'end':
            unique_paths.append([x for x in path_so_far] + ['end'])
            return

        new_path = [x for x in path_so_far] + [cave]
        for destination in connections[cave]:
            if destination in path_so_far and destination.islower():
                continue

            explore(destination, new_path)

    explore('start', [])
    return len(unique_paths)


def part2(connections: dict[str, set[str]]) -> int:
    unique_paths: list[list[str]] = []

    def explore(cave: str, path_so_far: list[str]):
        if cave == 'end':
            unique_paths.append([x for x in path_so_far] + ['end'])
            return

        new_path = [x for x in path_so_far] + [cave]
        for destination in connections[cave]:
            if destination == "start":
                continue
            c = Counter([x for x in new_path if x.islower()])  # visited smol

            if destination in path_so_far and destination.islower() and c.most_common()[0][1] == 2:
                continue

            explore(destination, new_path)

    explore('start', [])
    # pprint(unique_paths)
    return len(unique_paths)


paths: dict[str, set[str]] = defaultdict(set)
with open('input', 'r') as file:
    for line in file:
        cave_a, cave_b = line.strip().split('-')
        paths[cave_a].add(cave_b)
        paths[cave_b].add(cave_a)

print(f'{part1(paths)=}')
print(f'{part2(paths)=}')