import numpy as np
import itertools

def riemann_nd_step(f, ranges, step):
    dims = len(ranges)

    axes = []
    for (a, b) in ranges:
        axis = np.arange(a, b, step)
        axes.append(axis)

    dV = step ** dims

    total = 0.0
    for point in itertools.product(*axes):
        total += f(*point) * dV

    return total
def f(x, y):
    return x**2 + 2*y**2

result = riemann_nd_step(f, [(0,1), (0,1)], step=0.001)
print(result)
