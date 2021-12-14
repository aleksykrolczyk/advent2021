from collections import Counter, defaultdict


def part1(chain: str, rules: dict[str, str]) -> int:
    for STEP in range(10):
        new_chain = ""
        for i in range(0, len(chain) - 1):
            pair = chain[i:i + 2]
            if i == 0:
                new_chain += pair[0] + rules[pair] + pair[1]
            else:
                new_chain += rules[pair] + pair[1]
        chain = new_chain

    most_common = [x[1] for x in Counter(chain).most_common()]
    # print(len(chain))
    # print(Counter(chain).most_common())
    return most_common[0] - most_common[-1]


def part2(chain: str, rules: dict[str, str]) -> int:
    pair_count = defaultdict(int)
    single_count = defaultdict(int)

    for i in range(0, len(chain) - 1):
        pair_count[chain[i:i + 2]] += 1

    for c in chain:
        single_count[c] += 1

    for STEP in range(40):

        new_pair_count = defaultdict(int)

        for pair in pair_count.keys():
            between = rules[pair]
            new_pair_count[pair[0] + between] += pair_count[pair]
            new_pair_count[between + pair[1]] += pair_count[pair]

            single_count[between] += pair_count[pair]

        pair_count = new_pair_count

    most_common = [x[1] for x in Counter(single_count).most_common()]
    return most_common[0] - most_common[-1]


starting: str
rules: dict[str, str] = {}
with open('input', 'r') as file:
    starting = file.readline().strip()
    file.readline()
    for line in file:
        a, b = line.strip().split(' -> ')
        rules[a] = b

print(f'{part1(starting, rules)=}')
print(f'{part2(starting, rules)=}')
