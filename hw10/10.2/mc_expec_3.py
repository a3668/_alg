import random

def f(x, y, z):
    return x**2 + 2*y**2 + 3*z**2  

def mcInt_expectation_3d(f, rx, ry, rz, n=100000):
    total = 0.0
    for _ in range(n):
        x = random.uniform(rx[0], rx[1])
        y = random.uniform(ry[0], ry[1])
        z = random.uniform(rz[0], rz[1])
        total += f(x, y, z)
        # total 就是取很多個隨機點的「高度(值)總和」

    volume = (rx[1] - rx[0]) * (ry[1] - ry[0]) * (rz[1] - rz[0])
    return volume * (total / n)
    # total/n 就是這些高度的平均

print(mcInt_expectation_3d(f, [0,1], [0,1], [0,1]))
