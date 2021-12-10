SIZE = 5


class Board:
    def __init__(self):
        self.board: list[list[int]] = []
        self.is_bingoed = False

    def add_row(self, row: list[int]) -> None:
        self.board.append(row)

    def bingo(self) -> bool:
        for i in range(SIZE):
            if all(self.board[i][j] == 0 for j in range(SIZE)) or all(self.board[j][i] == 0 for j in range(SIZE)):
                self.is_bingoed = True
                return True
        return False

    def mark(self, number: int) -> bool:
        for i in range(SIZE):
            for j in range(SIZE):
                if self.board[i][j] == number:
                    self.board[i][j] = 0
                    return True
        return False

    def score(self, number) -> int:
        s = 0
        for i in range(SIZE):
            for j in range(SIZE):
                s += self.board[i][j]
        return s * number


def part1(boards: list[Board], numbers: list[int]) -> int:
    for i, number in enumerate(numbers):
        for board in boards:
            board.mark(number)
            if board.bingo():
                return board.score(number)
    return -1


def part2(boards: list[Board], numbers: list[int]) -> int:
    scores = []
    for i, number in enumerate(numbers):
        for board in boards:
            if board.is_bingoed:
                continue
            board.mark(number)
            if board.bingo():
                scores.append(board.score(number))
    return scores[-1]


boards: list[Board] = []
with open("input", 'r') as file:
    numbers = [int(x) for x in file.readline().split(',') if x]
    file.readline()

    b = Board()
    for line in file:
        line = line.strip()
        if not line:
            boards.append(b)
            b = Board()
            continue

        b.add_row([int(x) for x in line.split(' ') if x])


print(f'{part1(boards, numbers)=}')
print(f'{part2(boards, numbers)=}')
