def compute_power(data):
    length = len(data)
    gamma = 0
    eps = 0
    num_len = len(data[0])
    for digit in range(0, num_len):
        int_sum = sum([int(i[digit]) for i in data])
        most_common = int(round(int_sum / length))
        gamma += most_common * 2 ** (num_len - digit - 1)
        eps += int(not most_common) * 2 ** (num_len - digit - 1)
    return eps * gamma


def more_diagnostic(data):
    filter_list = data
    num_len = len(data[0])
    for digit in range(0, num_len):
        int_sum = sum([int(i[digit]) for i in filter_list])
        ratio = int_sum / len(filter_list) + 0.00001  # hacky stuff
        most_common = int(round(ratio))
        filter_list = list(filter(lambda x: int(x[digit]) == most_common, filter_list))
        if len(filter_list) == 1:
            oxy = filter_list[0]
            break

    filter_list = data
    for digit in range(0, num_len):
        int_sum = sum([int(i[digit]) for i in filter_list])
        ratio = int_sum / len(filter_list) + 0.000001
        most_common = int(round(ratio))
        filter_list = list(filter(lambda x: int(x[digit]) != most_common, filter_list))
        if len(filter_list) == 1:
            co = filter_list[0]
            break
    oxy = sum([(int(oxy[i]) * 2 ** (len(oxy) - i - 1)) for i in range(len(oxy))])
    co = sum([(int(co[i]) * 2 ** (len(co) - i - 1)) for i in range(len(co))])
    return oxy * co


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        d = file.read().splitlines()
    print(compute_power(d))
    print(more_diagnostic(d))
