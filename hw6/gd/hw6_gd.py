import math
import numpy as np
from numpy.linalg import norm

np.set_printoptions(precision=4)

# 函數 f 對變數 k 的偏微分: df / dk
'''
def df(f, p, k, step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step
'''
def df_central(f, p, k, step=0.01):
    p1 = p.copy()
    p2 = p.copy()
    p1[k] = p[k] + step
    p2[k] = p[k] - step
    return (f(p1) - f(p2)) / (2 * step)


# 函數 f 在點 p 上的梯度
def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df_central(f, p, k, step)
    return gp

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, lr=0.01, max_loops=100000, dump_period=1000):
    p = p0.copy()
    fp0 = f(p)
    for i in range(max_loops):
        fp = f(p)
        gp = grad(f, p) # 計算梯度 gp
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        if i%dump_period == 0: 
            print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
        if glen < 0.00001: # or fp0 < fp:  # 如果步伐已經很小了，或者 f(p) 變大了，那麼就停止吧！
            break
        gstep = np.multiply(gp, -1*lr) # gstep = 逆梯度方向的一小步 [6 * 0.01,8 * 0.01]
        p +=  gstep # 向 gstep 方向走一小步
        # fp0 = fp
    print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
    return p # 傳回最低點！
# 測試函數 f(x, y) = x² + y²
def f(p):
    x, y = p
    return x**2 + y**2

# 初始點 p0
p0 = np.array([3.0, 4.0])

# 呼叫梯度下降法
result = gradientDescendent(f, p0, lr=0.1, dump_period=100)
print("Minimum point:", result)
