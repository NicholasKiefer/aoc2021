def foldone(data, foldings):
    for fold in foldings[:1]:
        for coord in range(len(data)):
            if fold[0] == "x":
                if data[coord][0] > fold[1]:
                    new_data = [data[coord][0] - 2*(data[coord][0] - fold[1]), data[coord][1]]
                    data[coord] = new_data
            else:
                if data[coord][1] > fold[1]:
                    new_data = [data[coord][0], data[coord][1] - 2*(data[coord][1] - fold[1])]
                    data[coord] = new_data
    # get unique coords
    unique = []
    for coord in data:
        if coord not in unique:
            unique.append(coord)
    return len(unique)


def foldtwo(data, foldings):
    for fold in foldings:
        for coord in range(len(data)):
            if fold[0] == "x":
                if data[coord][0] > fold[1]:
                    new_data = [data[coord][0] - 2*(data[coord][0] - fold[1]), data[coord][1]]
                    data[coord] = new_data
            else:
                if data[coord][1] > fold[1]:
                    new_data = [data[coord][0], data[coord][1] - 2*(data[coord][1] - fold[1])]
                    data[coord] = new_data
    # this time print coords and recognise code
    # print ascii style?
    size = max([max(i) for i in data]) + 1
    field = [["X" if [i, j] in data else "." for i in range(size)] for j in range(size)]
    for line in field:
        print(line)


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read()
    d = d.split("\n\n")
    coords = d[0].split("\n")
    coords = [i.split(",") for i in coords]
    coords = [[int(i[0]), int(i[1])] for i in coords]
    folds = [i.split("=") for i in d[1].split("\n")]
    folds = [[i[0], int(i[1])] for i in folds]
    print(foldone(coords, folds))
    print(foldtwo(coords, folds))
