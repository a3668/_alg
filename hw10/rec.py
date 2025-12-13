import numpy as np
import random

step = 0.001

def integrate_nd(f, ranges, idx=0, current_point=None):
    if current_point is None:
        current_point = []

    # 如果已經到最後一維，直接計算 f
    if idx == len(ranges):
        return f(*current_point)

    total = 0.0
    r = ranges[idx]

    for v in np.arange(r[0], r[1], step):
        current_point.append(v)
        total += integrate_nd(f, ranges, idx+1, current_point) * step
        current_point.pop()

    return total
def f(x, y):
    return x**2 + 2*y**2

result = integrate_nd(f, [[0, 1], [0, 1]])
print(result)
