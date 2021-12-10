def find_illegal(data):
    belongs_to = {"]": "[", "}": "{", ")": "(", ">": "<"}
    closed = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    ret_lines = []
    for line in data:
        bras = []
        done = False
        for char in line:
            if done:
                continue
            if char in belongs_to.values():
                bras.append(char)
            else:
                if bras[-1] != belongs_to[char]:
                    score += closed[char]
                    done = True
                    break
                else:
                    bras.pop()
        if not done:
            ret_lines.append(line)
    return score, ret_lines


def corrupt(data):
    _, data = find_illegal(data)
    closed = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in data:
        bras = []
        score = []
        for char in line:
            if char in closed.keys():
                bras.append(char)
            else:
                bras.pop()
        for char in bras[::-1]:
            score.append(closed[char])
        s = 0
        for i in score:
            s *= 5
            s += i
        scores.append(s)
    return sorted(scores)[int(len(scores)/2)]


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().splitlines()
    print(find_illegal(d)[0])
    print(corrupt(d))

# 802107 too high
