import math
import numpy as np
from numpy.linalg import norm

np.set_printoptions(precision=4)

def df_central(f, p, k, step=0.01):
    p1 = p.copy()
    p2 = p.copy()
    p1[k] = p[k] + step
    p2[k] = p[k] - step
    return (f(p1) - f(p2)) / (2 * step)

def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df_central(f, p, k, step)
    return gp

# 指數衰減學習率
def lr_exp(i, lr0=0.1, gamma=0.999):
    return lr0 * (gamma ** i)

def gradientDescendent_exp(f, p0, lr0=0.1, gamma=0.999, max_loops=100000, dump_period=1000):
    p = p0.copy()
    for i in range(max_loops):
        fp = f(p)
        gp = grad(f, p)
        glen = norm(gp)

        lr_i = lr_exp(i, lr0=lr0, gamma=gamma)

        if i % dump_period == 0:
            print('{:05d}: f(p)={:.6f} lr={:.6e} p={} gp={} glen={:.6e}'
                  .format(i, fp, lr_i, p, gp, glen))

        if glen < 1e-5:
            break

        p += -lr_i * gp

    print('{:05d}: f(p)={:.6f} lr={:.6e} p={} gp={} glen={:.6e}'
          .format(i, fp, lr_i, p, gp, glen))
    return p

# 測試函數
def f(p):
    x, y = p
    return x**2 + y**2

p0 = np.array([3.0, 4.0])
result = gradientDescendent_exp(f, p0, lr0=0.1, gamma=0.999, dump_period=100)
print("Minimum point:", result)
