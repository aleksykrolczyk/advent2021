def part1(commands: list[tuple[str, float]]) -> int:
    h_pos, depth = 0, 0
    for cmd, val in commands:
        match cmd:
            case "forward":
                h_pos += val
            case "down":
                depth += val
            case "up":
                depth -= val
    return h_pos * depth


def part2(commands: list[tuple[str, float]]) -> int:
    h_pos, depth, aim = 0, 0, 0
    for cmd, val in commands:
        match cmd:
            case "forward":
                h_pos += val
                depth += val * aim
            case "down":
                aim += val
            case "up":
                aim -= val
    return h_pos * depth


commands: list[tuple[str, int]] = []
with open("input", "r") as file:
    for line in file:
        cmd, val = line.split()
        commands.append((cmd, int(val)))

print(f'{part1(commands)=}')
print(f'{part2(commands)=}')

