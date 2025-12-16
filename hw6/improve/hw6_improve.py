import numpy as np
from numpy.linalg import norm

np.set_printoptions(precision=4)

# 使用解析梯度的梯度下降法尋找函數最低點
# f      : loss function
# grad_f : analytic gradient function
def gradientDescendent_analytic(f, grad_f, p0, lr=0.01, max_loops=100000, dump_period=1000):
    p = np.array(p0, dtype=np.float32).copy()
    fp0 = f(p)

    for i in range(max_loops):
        fp = f(p)
        gp = grad_f(p)            # 計算解析梯度 gp
        glen = norm(gp)           # norm = 梯度的長度 (步伐大小)

        if i % dump_period == 0:
            print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(
                i, fp, str(p), str(gp), glen
            ))

        if glen < 0.00001:        # 如果步伐已經很小了，那麼就停止吧！
            break

        gstep = np.multiply(gp, -1.0 * lr)  # 逆梯度方向的一小步
        p += gstep                           # 向 gstep 方向走一小步
        # fp0 = fp

    print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(
        i, fp, str(p), str(gp), glen
    ))
    return p  # 傳回最低點！


# 測試函數 f(x, y) = x^2 + y^2
def f(p):
    x, y = p
    return x**2 + y**2


# 解析梯度: [2x, 2y]
def grad_f(p):
    x, y = p
    return np.array([2.0 * x, 2.0 * y], dtype=np.float32)


# 初始點 p0
p0 = np.array([3.0, 4.0], dtype=np.float32)

# 呼叫解析梯度版梯度下降法
result = gradientDescendent_analytic(f, grad_f, p0, lr=0.1, dump_period=100)
print("Minimum point:", result)
