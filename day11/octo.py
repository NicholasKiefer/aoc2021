def simu(data):
    steps = 1000
    flashes = 0
    pad = [-int(1e10)] * 12
    data = [[-int(1e10)] + i + [-int(1e10)] for i in data]
    data.insert(0, pad)
    data.append(pad)
    for step in range(steps):
        data = [[i + 1 for i in j] for j in data]
        while any([i >= 10 for y in data for i in y]):
            for j in range(1, len(data) - 1):
                for k in range(1, len(data[0]) - 1):
                    if data[j][k] > 9:
                        data[j][k] = 0
                        flashes += 1
                        data[j - 1][k - 1] += 1 if data[j - 1][k - 1] else 0
                        data[j - 1][k] += 1 if data[j - 1][k] else 0
                        data[j - 1][k + 1] += 1 if data[j - 1][k + 1] else 0
                        data[j][k - 1] += 1 if data[j][k - 1] else 0
                        data[j][k + 1] += 1 if data[j][k + 1] else 0
                        data[j + 1][k - 1] += 1 if data[j + 1][k - 1] else 0
                        data[j + 1][k] += 1 if data[j + 1][k] else 0
                        data[j + 1][k + 1] += 1 if data[j + 1][k + 1] else 0
        if all([i == 0 for y in data for i in y if i >= 0]):
            print("synced", step)
    return flashes


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().splitlines()
    d = [[int(i) for i in j] for j in d]
    print(simu(d))
