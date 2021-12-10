class Fish:
    def __init__(self, days: int | None = None):
        self.timer = days or 8

    def reset(self):
        self.timer = 6

    def step(self) -> None:
        self.timer -= 1

    def pregnant(self):
        if self.timer == -1:
            return True
        return False


def part1(numbers: list[int]) -> int:
    DAYS = 80
    school = {Fish(n) for n in numbers}
    for _ in range(DAYS):
        new_fish = 0
        for fish in school:
            fish.step()
            if fish.pregnant():
                new_fish += 1
                fish.reset()

        for n in range(new_fish):
            school.add(Fish())

    return len(school)


def part2(numbers: list[int]) -> int:
    DAYS = 256
    school = [0 for _ in range(9)]
    for n in numbers:
        school[n] += 1

    for d in range(DAYS):
        new_school = [0 for _ in range(9)]
        reproducible = school[0]

        for i in range(9):
            new_school[i - 1] = school[i]

        new_school[6] += reproducible
        school = [x for x in new_school]

    return sum(school)


with open('input', 'r') as file:
    n = file.readline()
    numbers = [int(x) for x in n.split(',')]


print(f'{part1(numbers)=}')
print(f'{part2(numbers)=}')
