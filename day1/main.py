def part1(m: list[float]) -> int:
    incr_no = 0
    for i in range(1, len(m)):
        if m[i] > m[i - 1]:
            incr_no += 1
    return incr_no


def part2(m: list[float]) -> int:
    incr_no = 0
    for i in range(3, len(m)):
        if m[i] > m[i - 3]:
            incr_no += 1
    return incr_no


with open("input.txt", 'r') as file:
    measurements = [float(x) for x in file.readlines()]

print(f'{part1(measurements)=}')
print(f'{part2(measurements)=}')