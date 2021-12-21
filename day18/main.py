from math import floor, ceil
from typing import Union, Optional
from copy import deepcopy

class SnailfishNumber:
    def __init__(
            self,
            values: list[Union["SnailfishNumber", list, int]] = [],
            padre: Optional["SnailfishNumber"] = None,
            value: int | None = None,
    ) -> None:
        self.left: SnailfishNumber | None = None
        self.right: SnailfishNumber | None = None
        self.value = None
        self.padre = padre

        if value is not None:
            self.value = value
            return

        else:
            left, right = values
            if isinstance(left, list):
                left = SnailfishNumber(left, self)
            if isinstance(right, list):
                right = SnailfishNumber(right, self)

            if isinstance(left, int):
                left = SnailfishNumber(padre=padre, value=left)
            if isinstance(right, int):
                right = SnailfishNumber(padre=padre, value=right)

            self.left = left
            self.right = right
            left.padre = self
            right.padre = self

            self.value = None

    def __repr__(self) -> str:
        return f'[{self.left}, {self.right}]' if not self.is_terminal else str(self.value)

    @property
    def depth(self) -> int:
        d = 0 if self.padre is None else self.padre.depth + 1
        return d

    @property
    def is_terminal(self) -> bool:
        return self.value is not None

    @property
    def sibling(self) -> "SnailfishNumber":
        return self.padre.right if self.is_left else self.padre.left

    @property
    def is_left(self) -> bool:
        if self.padre is None:
            raise Exception("Hamuj sie")
        return self.padre.left is self

    @property
    def is_right(self) -> bool:
        return not self.is_left

    def __add__(self, other: "SnailfishNumber") -> "SnailfishNumber":
        s = SnailfishNumber([self, other])
        s.reduce()
        return s

    def reduce(self) -> None:
        while True:
            self.explode()
            a = 5
            if not self.split():
                return

    def explode(self):
        if self.depth == 4:
            self.add_to_closest_regular_left(self.left.value)
            self.add_to_closest_regular_right(self.right.value)
            if self.is_left:
                self.padre.left.value = 0
            else:
                self.padre.right.value = 0
        else:
            if self.left and not self.left.is_terminal:
                self.left.explode()
            if self.right and not self.right.is_terminal:
                self.right.explode()

    def add_to_closest_regular_left(self, x: int) -> None:
        if self.is_right:
            if self.sibling.is_terminal:
                self.sibling.value += x
                return
            padre = self.sibling
            while not padre.right.is_terminal:
                padre = padre.right
            padre.right.value += x
            return

        padre = self.padre
        while padre.is_left:
            padre = padre.padre
            if padre.padre is None:
                return
        padre = padre.sibling

        if padre.is_terminal:
            padre.value += x
            return

        while not padre.right.is_terminal:
            padre = padre.right
        padre.right.value += x

    def add_to_closest_regular_right(self, x: int) -> None:
        if self.is_left:
            if self.sibling.is_terminal:
                self.sibling.value += x
                return
            padre = self.sibling
            while not padre.left.is_terminal:
                padre = padre.left
            padre.left.value += x
            return
        padre = self.padre
        while padre.is_right:
            padre = padre.padre
            if padre.padre is None:
                return
        padre = padre.sibling

        if padre.is_terminal:
            padre.value += x
            return

        while not padre.left.is_terminal:
            padre = padre.left
        padre.left.value += x

    def split(self) -> bool:
        if self.is_terminal:
            if self.value >= 10:
                if self.is_left:
                    self.padre.left = SnailfishNumber([floor(self.value / 2), ceil(self.value / 2)])
                    self.padre.left.padre = self.padre
                    return True
                self.padre.right = SnailfishNumber([floor(self.value / 2), ceil(self.value / 2)])
                self.padre.right.padre = self.padre
                return True
            return False

        return self.left.split() or self.right.split()

    def magnitude(self) -> int:
        if self.is_terminal:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def part1(numbers: list[SnailfishNumber]) -> int:
    _sum = numbers[0]
    for n in numbers[1:]:
        _sum = _sum + n
    return _sum.magnitude()


def part2(numbers: list[SnailfishNumber]) -> int:
    biggest_magnitude = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if i == j:
                continue
            m = (deepcopy(numbers[i]) + deepcopy(numbers[j])).magnitude()
            if m > biggest_magnitude:
                biggest_magnitude = m
            m = (deepcopy(numbers[j]) + deepcopy(numbers[i])).magnitude()
            if m > biggest_magnitude:
                biggest_magnitude = m
    return biggest_magnitude



numbers: list[SnailfishNumber] = []
with open('input', 'r') as file:
    for line in file:
        x = eval(line.strip())
        numbers.append(SnailfishNumber(x))

# print(f'{part1(numbers)=}')
print(f'{part2(numbers)=}')
