from collections import defaultdict


def get_mcb(nums: list[str]) -> dict:
    mcb = defaultdict(int)
    for num in nums:
        for i, digit in enumerate(num):
            mcb[i] += 1 if digit == '1' else -1

    return mcb


def part1(nums: list[str]) -> int:
    mcb = get_mcb(nums)

    g_rate, e_rate = '', ''
    for v in mcb.values():
        g_rate += '1' if v > 0 else '0'
        e_rate += '1' if v < 0 else '0'

    return int(g_rate, 2) * int(e_rate, 2)


def part2(nums: list[str]) -> int:
    ox_nums = [x for x in nums]
    co2_nums = [x for x in nums]

    digit_length = len(nums[0])

    for i in range(digit_length):
        if len(ox_nums) == 1:
            break
        mcb = get_mcb(ox_nums)
        bit = '1' if mcb[i] >= 0 else '0'
        ox_nums = [x for x in ox_nums if x[i] == bit]

    for i in range(digit_length):
        if len(co2_nums) == 1:
            break
        mcb = get_mcb(co2_nums)
        bit = '1' if mcb[i] < 0 else '0'
        co2_nums = [x for x in co2_nums if x[i] == bit]

    return int(ox_nums[0], 2) * int(co2_nums[0], 2)


with open("input", "r") as file:
    nums = [x.strip() for x in file.readlines()]

print(f'{part1(nums)=}')
print(f'{part2(nums)=}')


