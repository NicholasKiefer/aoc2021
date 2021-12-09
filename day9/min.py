def find_min(data):
    risk = 0
    pos = []
    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):
            here = data[i][j]
            if here < data[i + 1][j] and here < data[i][j + 1] and here < data[i - 1][j] and here < data[i][j - 1]:
                # save min
                pos.append([i, j])
                risk += 1 + here
    return risk, pos


def find_basin(data):
    _, pos = find_min(data)
    basins = []
    for minimum in pos:
        size = 1
        # start from index and expand, either stop by boundary (10) or 9 or lower point than now
        x, y = minimum
        indices_to_check = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
        checked_ones = []
        while len(indices_to_check) > 0:
            x, y = indices_to_check[0]
            here = data[x][y]
            if here < 9 and [x, y] not in checked_ones:
                size += 1
                if data[x + 1][y] > here:
                    indices_to_check.append([x + 1, y])
                if data[x - 1][y] > here:
                    indices_to_check.append([x - 1, y])
                if data[x][y + 1] > here:
                    indices_to_check.append([x, y + 1])
                if data[x][y - 1] > here:
                    indices_to_check.append([x, y - 1])
            checked_ones.append([x, y])
            indices_to_check = indices_to_check[1:]
        basins.append(size)
    s = sorted(basins, reverse=True)
    return s[0] * s[1] * s[2]


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().splitlines()
    padding = [10] * 102
    d = [[10] + [int(i) for i in j] + [10] for j in d]
    d.insert(0, padding)
    d.append(padding)
    print(find_min(d)[0])
    print(find_basin(d))
