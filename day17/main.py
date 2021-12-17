def part1(xmin: int, xmax: int, ymin: int, ymax: int) -> int:
    return ymin * (ymin + 1) // 2


def part2(xmin: int, xmax: int, ymin: int, ymax: int) -> int:
    sols = 0
    for xspeed in range(xmax + 1):
        for yspeed in range(ymin, -ymin + 1):
            xs, ys = xspeed, yspeed
            x, y, = 0, 0
            while x < xmax + 1 and y > ymin - 1:
                x, y = x + xs, y + ys
                xs, ys = xs - 1, ys - 1
                xs = xs if xs > 0 else 0
                if xmin <= x <= xmax and ymin <= y <= ymax:
                    sols += 1
                    break
    return sols


with open('input', 'r') as file:
    s = file.readline().strip()[13:]
    xpart, ypart = s.split(', ')
    xpart, ypart = xpart[2:], ypart[2:]

    a, b = xpart.split("..")
    xmin, xmax = int(a), int(b)

    a, b = ypart.split("..")
    ymin, ymax = int(a), int(b)


print(f'{part1(xmin, xmax, ymin, ymax)=}')
print(f'{part2(xmin, xmax, ymin, ymax)=}')
