import sys


def generate_board_direction(input):
    n = 5
    l = []
    for i in range(n):
        if i <= n - 2:
            l.append(list(map(lambda x: int(x.rstrip()), input.readline().split())))
        else: direction = int(input.readline())
    assert 0 <= direction <= 3, 'invalid direction input'
    return l, direction


def rotate_board(board, k):
    assert 1 <= k <= 3, 'k out of range'
    for _ in range(k):
        board = [list(i) for i in zip(*board)][::-1]

    return board


def move_row(row):
    assert len(row) == 4, 'invalid input'
    new_row = [0] * 4
    previous, k = 0, 0

    for x in row:
        if x != 0:
            if previous == 0:
                previous = x
            else:
                if x == previous:
                    new_row[k] = x * 2
                    previous = 0
                else:
                    new_row[k] = previous
                    previous = x
                k += 1
    if previous != 0:
        new_row[k] = previous
    return new_row


def swipe_left(board):
    for i, row in enumerate(board):
        board[i] = move_row(row)


def print_output(board):
    for row in board:
        for x in row:
            print(x, end=' ')
        print()


def main(input):
    board, direction = generate_board_direction(input)
    if direction > 0:
        board = rotate_board(board, direction)
    swipe_left(board)
    if direction > 0:
        board = rotate_board(board, 4 - direction)

    return print_output(board)


if __name__ == '__main__':
    main(sys.stdin)