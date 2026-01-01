import numpy as np
from itertools import product

def rm_n_loop(f, ranges, step):
    # 每一維的取樣點，例如 [array([0,0.1,0.2]), array([0,0.1,0.2])]
    # axes = [np.arange(r[0], r[1], step) for r in ranges]
    axes = []
    for r in ranges:
        start = r[0]
        end = r[1]
        axis_points = np.arange(start, end, step)
        axes.append(axis_points)

    total = 0.0
    cell_volume = step ** len(axes)   # n 維體積
    
    # product 會產生所有組合，例如 2 維時 (x,y), (x,y), ...
    for point in product(*axes):
        total += f(*point) * cell_volume
    
    return total
def f2(x, y):
    return x**2 + 2*y**2

print(rm_n_loop(f2, [(0,1), (0,1)], 0.01))
def f3(x, y, z):
    return x**2 + y*z + 1

print(rm_n_loop(f3, [(0,1), (0,1), (0,1)], 0.1))
