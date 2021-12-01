import numpy as np


def calc(depth):
    ret = np.sum(np.greater(depth[1:], depth[:-1]))
    return ret


def calc_sliding(depth):
    # nearly_diag should look like
    # [1, 1, 1, 0, 0, ...]
    # [0, 1, 1, 1, 0, ...]
    # [0, 0, 1, 1, 1, ...]
    l = len(depth)
    nearly_diag = np.diag(np.ones(l)) + np.diag(np.ones(l), 1)[:l, :l] + np.diag(np.ones(l), 2)[:l, :l]
    sum_depth = nearly_diag @ depth
    ret = np.sum(np.greater(sum_depth[1:], sum_depth[:-1]))
    return ret


if __name__ == "__main__":
    d = np.loadtxt("data.txt", dtype=int, delimiter="\n", )
    print(calc(d))
    print(calc_sliding(d))
