def avoid_double(data):
    data = [[a, b, c, d] for [a, b, c, d] in data if (a == c or b == d)]
    size = max([max(i) for i in data]) + 1
    points = {i: [0] * size for i in range(size)}
    for line in data:
        a, b, c, d = line
        if a == c:
            low, high = min((b, d)), max((b, d)) + 1
            for i in range(low, high):
                points[a][i] += 1
        else:
            low, high = min((a, c)), max((a, c)) + 1
            for i in range(low, high):
                points[i][b] += 1
    ret = sum((i > 1 for x in points.values() for i in x))
    return ret


def avoid_with_diag(data):
    size = max([max(i) for i in data]) + 1
    points = {i: [0] * size for i in range(size)}
    for line in data:
        a, b, c, d = line
        if a == c:
            low, high = min((b, d)), max((b, d)) + 1
            for i in range(low, high):
                points[a][i] += 1
        elif b == d:
            low, high = min((a, c)), max((a, c)) + 1
            for i in range(low, high):
                points[i][b] += 1
        else:
            low, high = min((a, c)), max((a, c)) + 1
            low2, high2 = min((b, d)), max((b, d))
            sign = 1 if (c > a and d > b) or (c < a and d < b) else -1
            if sign == 1:
                for i in range(low, high):
                    points[i][low2 + i - low] += 1
            else:
                for i in range(low, high):
                    points[i][high2 - i + low] += 1
    ret = sum((i > 1 for x in points.values() for i in x))
    return ret


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().splitlines()
    d = [[j.split(",") for j in i.split(" -> ")] for i in d]
    d = [[int(x) for y in b for x in y] for b in d]
    print(avoid_double(d))
    print(avoid_with_diag(d))
