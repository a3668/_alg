import numpy as np

# Sigmoid 函數與導數
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# XOR 資料集
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])
y = np.array([[0],[1],[1],[0]])

# 初始化權重與學習率
np.random.seed(42)
W1 = np.random.rand(2, 2)
b1 = np.random.rand(1, 2)
W2 = np.random.rand(2, 1)
b2 = np.random.rand(1, 1)
lr = 0.1

# 訓練過程
for epoch in range(10000):
    # Forward
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    y_hat = sigmoid(z2)

    # Loss (均方誤差)
    loss = np.mean((y - y_hat)**2)

    # Backward
    d2 = (y_hat - y) * sigmoid_deriv(y_hat)
    dW2 = np.dot(a1.T, d2)
    db2 = np.sum(d2, axis=0, keepdims=True)

    d1 = np.dot(d2, W2.T) * sigmoid_deriv(a1)
    dW1 = np.dot(X.T, d1)
    db1 = np.sum(d1, axis=0, keepdims=True)

    # 更新權重
    W1 -= lr * dW1
    b1 -= lr * db1
    W2 -= lr * dW2
    b2 -= lr * db2

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss = {loss:.4f}")

# 測試結果
print("\nFinal predictions:")
print(np.round(y_hat, 3))
