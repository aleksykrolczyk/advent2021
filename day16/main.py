from enum import Enum


class PacketType(Enum):
    literal = 4

    sum = 0
    prod = 1
    min = 2
    max = 3
    gt = 5
    lt = 6
    eq = 7


class Reader:
    def __init__(self, s: str) -> None:
        self.s = s
        self.slen = len(s)
        self.index = 0

    @property
    def num_read(self) -> int:
        return self.index

    def read(self, n: int) -> str:
        val = self.s[self.index:self.index + n]
        self.index += n
        return val

    def drained(self) -> bool:
        return self.index >= self.slen

    def subreader(self) -> "Reader":
        return Reader(self.s[self.index:])


def hex2bin(char: str) -> str:
    return bin(int(char, 16))[2:].zfill(4)


def bin2int(number: str) -> int:
    return int(number, 2)


def get_version_and_type(s: str) -> tuple[int, PacketType]:
    version = bin2int(s[:3])
    return version, PacketType(bin2int(s[3:6]))


def part1(r: Reader) -> tuple[int, int]:
    version_sum = 0

    bits = r.read(6)
    version, ptype = get_version_and_type(bits)
    version_sum += version
    if ptype == PacketType.literal:
        reading = True
        num = ''
        while reading:
            bits = r.read(5)
            if bits[0] == "0":
                reading = False
            num += bits[1:]
        return version, r.num_read

    else:
        length_type = r.read(1)
        if length_type == "0":  # bits type
            length = bin2int(r.read(15))
            total_read = 0
            while total_read != length:
                version, num_read = part1(r.subreader())
                r.read(num_read)
                total_read += num_read
                version_sum += version

        if length_type == "1":  # subpackets num type
            subpackets = bin2int(r.read(11))
            for _ in range(subpackets):
                version, num_read = part1(r.subreader())
                r.read(num_read)
                version_sum += version

    return version_sum, r.num_read


def part2(r: Reader) -> tuple[int, int]:
    value = 0
    bits = r.read(6)
    version, ptype = get_version_and_type(bits)

    if ptype == PacketType.literal:
        reading = True
        num = ''
        while reading:
            bits = r.read(5)
            if bits[0] == "0":
                reading = False
            num += bits[1:]

        value = int(num, 2)
        return value, r.num_read

    else:
        length_type = r.read(1)
        values = []
        if length_type == "0":  # bits type
            length = bin2int(r.read(15))
            total_read = 0
            while total_read != length:
                v, num_read = part2(r.subreader())
                r.read(num_read)
                total_read += num_read
                values.append(v)

        if length_type == "1":  # subpackets num type
            subpackets = bin2int(r.read(11))
            for _ in range(subpackets):
                v, num_read = part2(r.subreader())
                r.read(num_read)
                values.append(v)

        match ptype:
            case PacketType.sum:
                value = sum(values)
            case PacketType.prod:
                value = 1
                for v in values:
                    value *= v
            case PacketType.min:
                value = min(values)
            case PacketType.max:
                value = max(values)
            case PacketType.gt:
                value = 1 if values[0] > values[1] else 0
            case PacketType.lt:
                value = 1 if values[0] < values[1] else 0
            case PacketType.eq:
                value = 1 if values[0] == values[1] else 0

    return value, r.num_read


with open('input', 'r') as file:
    encoded_hex = file.readline().strip()

encoded = ''
for char in encoded_hex:
    encoded += hex2bin(char)

print(f'{part1(Reader(encoded))=}')
print(f'{part2(Reader(encoded))=}')
