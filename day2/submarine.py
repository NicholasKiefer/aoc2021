def calc_pos(inp):
    horizontal = 0
    vertical = 0
    for i in inp:
        if i[0] == "forward":
            horizontal += i[1]
            continue
        elif i[0] == "down":
            vertical += i[1]
            continue
        vertical -= i[1]
    return horizontal * vertical


def calc_pos_aim(inp):
    horizontal = 0
    vertical = 0
    aim = 0
    for i in inp:
        if i[0] == "forward":
            horizontal += i[1]
            vertical += aim * i[1]
            continue
        elif i[0] == "down":
            aim += i[1]
            continue
        aim -= i[1]
    return horizontal * vertical


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        data = file.read().splitlines()
        data = [i.split() for i in data]
        data = [[i[0], int(i[1])] for i in data]
    print(calc_pos(data))
    print(calc_pos_aim(data))
