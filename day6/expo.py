def expo_first(data):
    return sum((project(i, 80) for i in data))


def expo_second(data):
    fishcount = [0] * 10
    for i in range(8):
        fishcount[i] = sum([j == i for j in data])
    for _ in range(256):
        fishcount[9] = fishcount[0]
        for i in range(6):
            fishcount[i] = fishcount[i + 1]
        fishcount[6] = fishcount[7] + fishcount[9]
        fishcount[7] = fishcount[8]
        fishcount[8] = fishcount[9]
    ret = sum(fishcount[:9])
    return ret


def project(init, days):
    days_left = days - init
    if days_left <= 0:
        return 1
    return project(9, days_left) + project(7, days_left)


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().split(",")
    d = [int(i) for i in d]
    print(expo_first(d))
    print(expo_second(d))
