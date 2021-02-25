import random

def nested_sum(t):
    total = 0
    for x in t:
        total += sum(x)
    return total


t = [[1, 2], [3], [4, 5, 6]]

total_sum_t = nested_sum(t)

print(total_sum_t)