import matplotlib.pyplot as plt
import numpy as np
import hw6_improve  # 假設你已經把 adam_optimizer 加進這個檔案了

# 1. 準備數據
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

# 2. 定義模型與 Loss 函數 (完全不用動)
def predict(a, xt):
    return a[0] + a[1] * xt

def MSE(a, x, y):
    total = 0
    for i in range(len(x)):
        total += (y[i] - predict(a, x[i]))**2
    return total / len(x)

def loss(p):
    return MSE(p, x, y)

# 3. 設定初始參數與執行優化
# --- 修改點 A: 必須使用 np.array，不能用 list [0.0, 0.0] ---
p = np.array([0.0, 0.0], dtype=np.float32)

print("Start training...")

# --- 修改點 B: 呼叫 Adam，這裡學習率 lr=0.1 對 Adam 來說算大，但在這個簡單問題上收斂會很快 ---
# 注意：確保 hw6_gd 裡面有 adam_optimizer 函式
plearn = hw6_improve.adam_optimizer(loss, p, lr=0.1, max_loops=3000, dump_period=100)

print('y_predicted=', list(map(lambda t: plearn[0] + plearn[1] * t, x)))

# 4. 繪圖 (不用動)
y_predicted = list(map(lambda t: plearn[0] + plearn[1] * t, x))
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.title(f"Linear Regression with Adam\nSlope: {plearn[1]:.2f}, Intercept: {plearn[0]:.2f}")
plt.legend()
plt.show()