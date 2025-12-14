import math
import numpy as np
from numpy.linalg import norm

np.set_printoptions(precision=4)

# 函數 f 對變數 k 的偏微分: df / dk
def df(f, p, k, step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, step=0.01, max_loops=100000, dump_period=1000):# p0:start point
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
        gstep = np.multiply(gp, -1*step) # gstep = 逆梯度方向的一小步
        p +=  gstep # 向 gstep 方向走一小步
        fp0 = fp
    print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
    return p # 傳回最低點！



def f_to_minimize(p):
    # p 是一個 numpy array，我們只取第一個元素作為 x
    x = p[0]
    # f(x) = x*x - 2*x + 1
    return x**2 - 2*x + 1

# ===============================================
# 步驟 2: 設置初始參數 p0 (單變數)
# ===============================================
# 理論最低點在 x=1 (因為 f(x) = (x-1)^2)，f(1)=0
p0 = np.array([5.0]) # 從 x=5.0 開始找

# ===============================================
# 步驟 3: 呼叫梯度下降函數
# ===============================================
print("--- 梯度下降開始 ---")
lowest_point = gradientDescendent(f_to_minimize, p0, step=0.01) 
print("--- 梯度下降結束 ---")
print("找到的最低點位置:", lowest_point) 
print("該點的函數值:", f_to_minimize(lowest_point))

# https://chatgpt.com/share/6909b5cb-1414-8006-9116-e66af4cb9128