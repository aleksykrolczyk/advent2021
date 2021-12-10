SCORES_ERRORS = {')': 3, ']': 57, '}': 1197, '>': 25137}
SCORES_AUTOCOMPLETE = {')': 1, ']': 2, '}': 3, '>': 4}
OPENING = {'(', '[', '{', '<'}
CLOSING = {')', ']', '}', '>'}
PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}


def part1(nav: list[str]) -> (int, list[list[str]]):
    illegals: list[str] = []
    incomplete: list[list[str]] = []
    add_to_incomplete = True
    for line in nav:
        history: list[str] = []
        for char in line:
            if char in OPENING:
                history.append(char)
            if char in CLOSING:
                if PAIRS[history.pop()] != char:
                    illegals.append(char)
                    add_to_incomplete = False
                    break
        if add_to_incomplete:
            incomplete.append(history)
        add_to_incomplete = True
    return sum(SCORES_ERRORS[x] for x in illegals), incomplete


def part2(to_complete: list[list[str]]) -> int:
    scores: list[int] = []
    for line in to_complete:
        score = 0
        for char in line[::-1]:
            score *= 5
            score += SCORES_AUTOCOMPLETE[PAIRS[char]]
        scores.append(score)
    scores.sort()
    mid = int((len(scores) - 1)/2)
    return scores[mid]


with open('input', 'r') as file:
    nav = [line.strip() for line in file]

scores_errors, to_complete = part1(nav)
print(to_complete)
print(f'{scores_errors}')
print(f'{part2(to_complete)=}')