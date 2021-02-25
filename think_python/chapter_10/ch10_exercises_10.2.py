import random


def cumsum(t):
    x = sum(t)
    t.append(x)
    return t




t = [1, 2, 3]

cumsum_t = cumsum(t)

print(cumsum_t)