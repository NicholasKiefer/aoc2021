def expo_first(data):
    return sum((project(i, 80) for i in data))


def expo_second(data):
    return sum((project(i, 256) for i in data))


def project(init, days):
    # at days - init we have two with counter 8 and 6
    # afterwards its the same for every fish
    days_left = days - init
    if days_left <= 0:
        return 1
    return project(9, days_left) + project(7, days_left)


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().split(",")
    d = [int(i) for i in d]
    print(expo_first([4]))
    # print(expo_second([1]))
