def first_bingo(numb, boards):
    for n in numb:
        for i in range(len(boards)):
            boards[i] = [0 if x == n else x for x in boards[i]]
            if check_board(boards[i]):
                # board has won, take sum and multiply with n
                ret = n * sum(boards[i])
                return ret
    return 0


def last_bingo(numb, boards):
    n = 0
    for n in numb:
        boards = [[0 if x == n else x for x in boards[i]] for i in range(len(boards))]
        if len(boards) == 1:
            last_winning = boards[0]
        boards = [i for i in boards if not check_board(i)]
        if len(boards) == 0:
            break
    ret = n * sum(last_winning)
    return ret


def check_board(board):
    for i in range(0, 25, 5):
        if sum(board[i:i+5]) == 0:
            return True
    for i in range(5):
        if sum([board[i] for i in list(range(0 + i, 25 + i, 5))]) == 0:
            return True
    return False


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().split("\n\n")
    numbers = [int(i) for i in d[0].split(",")]
    b = d[1:]
    b = [i.split() for i in b]
    b = [[int(i) for i in x] for x in b]
    print(first_bingo(numbers, b))
    print(last_bingo(numbers, b))
