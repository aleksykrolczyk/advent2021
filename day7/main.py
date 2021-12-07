def part1(positions: list[int]) -> int:
    minimum = float("inf")
    for u in range(max(positions)):
        dist = sum(abs(pos - u) for pos in positions)
        if dist < minimum:
            minimum = dist
    return minimum

def part2(positions: list[int]) -> int:
    minimum = float("inf")
    f_dist = lambda d: int(d*(d+1)/2)
    for u in range(max(positions)):
        dist = sum(f_dist(abs(pos - u)) for pos in positions)
        if dist < minimum:
            minimum = dist
    return minimum


with open('input', 'r') as file:
    line = file.readline()
    positions = [int(x) for x in line.split(',')]

print(f'{part1(positions)=}')
print(f'{part2(positions)=}')