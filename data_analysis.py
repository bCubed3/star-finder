import math
import numpy as np


def avg(values):
    return sum(values) / len(values)


def sigma(values):
    x = avg(values)
    s_d = 0
    for v in values:
        s_d += (x - v)**2
    return math.sqrt(s_d / len(values))


def sort(sets, function):
    s_values = [[sset, function(sset)] for sset in sets]
    s_values = np.array(s_values)
    print(s_values)
    return np.flip(np.sort(s_values, axis=0), 0)


print(sort([[1, 3, 4, 7], [1, 1, 1, 1], [1, 2, 2, 1]], sigma))
