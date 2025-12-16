import matplotlib.pyplot as plt
import numpy as np
import hw6_improve

# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)


def predict(a, xt):
    return a[0] + a[1] * xt


def MSE(a, x, y):
    total = 0.0
    for i in range(len(x)):
        total += (y[i] - predict(a, x[i]))**2
    return total / len(x)


def loss(p):
    return MSE(p, x, y)


# MSE 的解析梯度（改良法 核心）
# p = [b, w]
def grad_loss(p):
    b = p[0]
    w = p[1]
    n = len(x)

    db = 0.0
    dw = 0.0

    for i in range(n):
        r = (b + w * x[i] - y[i])
        db += r
        dw += r * x[i]

    db *= (2.0 / n)
    dw *= (2.0 / n)

    return np.array([db, dw], dtype=np.float32)


# 初始參數
p0 = np.array([0.0, 0.0], dtype=np.float32)

plearn = hw6_improve.gradientDescendent_analytic(
    loss,
    grad_loss,
    p0,
    lr=0.01,
    max_loops=3000,
    dump_period=1
)

# Plot the graph
y_predicted = list(map(lambda t: plearn[0] + plearn[1] * t, x))
print('y_predicted=', y_predicted)

plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()
