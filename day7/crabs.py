def crab1(data):
    med = median(data)
    diffs = [abs(i-med) for i in data]
    return sum(diffs)


def crab2(data):
    m = int(mean(data))
    diffs = [idk(abs(i-m)) for i in data]
    return sum(diffs)


def idk(number):
    ret = 0
    for i in range(number + 1):
        ret += i
    return ret


def median(data):
    data.sort()
    mid = len(data) // 2
    return (data[mid] + data[~mid]) / 2


def mean(data):
    return sum(data) / len(data)


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().split(",")
    d = [int(i) for i in d]
    print(crab1(d))
    print(crab2(d))
