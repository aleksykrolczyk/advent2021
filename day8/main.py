
def part1(patterns: list[list[str]], outputs: list[list[str]]) -> int:
    count = 0
    for o in outputs:
        count += len([i for i in o if len(i) in [2, 3, 4, 7]])
    return count

def part2(patterns: list[list[str]], outputs: list[list[str]]) -> int:
    _sum = 0
    for pattern, output in zip(patterns, outputs):
        pattern_sets = [set(p) for p in pattern]
        d0, d1, d2, d3, d4, d5, d6, d7, d8, d9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        d1 = [p for p in pattern_sets if len(p) == 2][0]
        d4 = [p for p in pattern_sets if len(p) == 4][0]
        d7 = [p for p in pattern_sets if len(p) == 3][0]
        d8 = [p for p in pattern_sets if len(p) == 7][0]

        rest = [p for p in pattern_sets if p not in [d1, d4, d7, d8]]

        for r in rest:
            if len(r) == 5 and len(r - d1) == 3:
                d3 = r
                break
        rest.remove(d3)

        for r in rest:
            if len(r) == 6 and len(r - d3) == 1:
                d9 = r
        rest.remove(d9)

        for r in rest:
            if len(r) != 6:
                continue
            if len(r - d1) == 4:
                d0 = r
            if len(r - d1) == 5:
                d6 = r
        rest.remove(d0)
        rest.remove(d6)

        # 2 and 5 by now
        for r in rest:
            if len(r - d6) == 0:
                d5 = r
            else:
                d2 = r

        digits = {
            frozenset(d0): 0,
            frozenset(d1): 1,
            frozenset(d2): 2,
            frozenset(d3): 3,
            frozenset(d4): 4,
            frozenset(d5): 5,
            frozenset(d6): 6,
            frozenset(d7): 7,
            frozenset(d8): 8,
            frozenset(d9): 9,
        }

        number = 0
        for i, o in enumerate(output):
            number += digits[frozenset(o)] * 10 ** (3 - i)
        _sum += number
    return _sum


patterns: list[list[str]] = []
outputs: list[list[str]] = []
with open('input', 'r') as file:
    for line in file:
        pattern, output = line.split('|')
        patterns.append(pattern.strip().split(' '))
        outputs.append(output.strip().split(' '))

print(f'{part1(patterns, outputs)=}')
print(f'{part2(patterns, outputs)=}')