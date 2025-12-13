import random

def f(x, y):
    return x**2 + 2*y**2

def mcInt_expectation(f, rx, ry, n=100000):
    total = 0.0
    for _ in range(n):
        x = random.uniform(rx[0], rx[1])
        y = random.uniform(ry[0], ry[1])
        total += f(x, y)
        # total 就是取很多個隨機點的「高度總和」

    area = (rx[1] - rx[0]) * (ry[1] - ry[0])
    return area * (total / n)
    # total/n 就是這些高度的平均

print(mcInt_expectation(f, [0,1], [0,1]))
