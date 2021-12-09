import random


def unique(data):
    data = [i.split("|")[1] for i in data]
    data = [i.strip().split(" ") for i in data]
    count = 0
    for line in data:
        for entry in line:
            length = len(entry)
            if length in [2, 4, 3, 7]:
                count += 1
    return count


def decode_for_real(data):
    data = [i.split(" | ") for i in data]
    data = [i[0] + " " + i[1] for i in data]
    data = [i.split(" ") for i in data]
    ret = 0
    connection = list(range(7))
    valid = [{0, 1, 2, 4, 5, 6}, {2, 5}, {0, 2, 3, 4, 6}, {0, 2, 3, 5, 6}, {1, 2, 3, 5}, {0, 1, 3, 5, 6},
             {0, 1, 3, 4, 5, 6}, {0, 2, 5}, {0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3, 5, 6}]
    translate = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}
    for idx, line in enumerate(data):
        # first get ordering in each line
        # translate characters
        characters = [set(translate[j] for j in i) for i in line]
        while True:
            random.shuffle(connection)
            # and take conn into account
            c = [set(connection.index(j) for j in i) for i in characters]
            if check(c, valid):
                break
        # then decode last 4 with current connection, and add all up
        decoded = line[-4:]
        decoded = [valid.index(set([connection.index(translate[i]) for i in j])) for j in decoded]
        decoded = int("".join([str(i) for i in decoded]))
        ret += decoded
    return ret


def check(characters, valid):
    for number in characters:
        if number not in valid:
            return False
    return True


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().splitlines()
    print(unique(d))
    print(decode_for_real(d))
