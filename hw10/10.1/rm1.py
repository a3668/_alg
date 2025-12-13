import numpy as np
import random
'''
def integrate(f, rx, ry):
    area = 0.0
    for x in np.arange(rx[0], rx[1], step):
        for y in np.arange(ry[0], ry[1], step):
            area += f(x,y)*step*step
    return area
'''

def f(x,y):
    return x**2+2*y**2

step = 0.001


def integrate_recursive(f, x_index, y_index, xs, ys, step):
    if x_index >= len(xs):
        return 0.0
    
    if y_index >= len(ys):
        return integrate_recursive(f, x_index + 1, 0, xs, ys, step)

    area = f(xs[x_index], ys[y_index]) * step * step
    return area + integrate_recursive(f, x_index, y_index + 1, xs, ys, step)


def rm_n(f, ranges, step):
    rx, ry = ranges
    xs = np.arange(rx[0], rx[1], step)
    ys = np.arange(ry[0], ry[1], step)
    return integrate_recursive(f, 0, 0, xs, ys, step)


print(rm_n(f, [(0,1), (0,1)], step))
