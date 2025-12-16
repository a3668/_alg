import math
import numpy as np
from numpy.linalg import norm

np.set_printoptions(precision=4, suppress=True)

# --- 數值梯度計算部分 (保持不變) ---

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

# --- 核心修改：Adam 優化器 ---

def adam_optimizer(f, p0, lr=0.1, beta1=0.9, beta2=0.999, epsilon=1e-8, max_loops=100000, dump_period=1000):
    p = p0.copy()
    
    # 1. 初始化 Adam 需要的變數
    # m: 一階動矩 (Momentum)，紀錄梯度的平均方向
    # v: 二階動矩 (Variance)，紀錄梯度的震盪幅度 (平方和)
    m = np.zeros_like(p)
    v = np.zeros_like(p)
    
    fp = f(p)
    
    # t 用來做偏差修正 (Bias Correction)，從 1 開始計算
    for t in range(1, max_loops + 1):
        fp = f(p)
        gp = grad(f, p)        # 計算當前梯度
        glen = norm(gp)
        
        # 輸出日誌
        if t % dump_period == 0: 
            print('{:05d}:f(p)={:.3f} p={} gp={} glen={:.5f}'.format(t, fp, str(p), str(gp), glen))
        
        # 停止條件
        if glen < 0.00001:
            break
            
        # --- Adam 的核心公式 ---
        
        # 2. 更新動量 m (類似慣性，保留之前的方向)
        m = beta1 * m + (1 - beta1) * gp
        
        # 3. 更新 RMSProp 部分 v (梯度的平方，用來衡量地形平緩程度)
        # gp**2 是 numpy 的元素平方運算
        v = beta2 * v + (1 - beta2) * (gp ** 2)
        
        # 4. 偏差修正 (Bias Correction)
        # 因為 m 和 v 初始為 0，前幾步會偏向 0，這裡把它校正回來
        m_hat = m / (1 - beta1 ** t)
        v_hat = v / (1 - beta2 ** t)
        
        # 5. 更新參數 p
        # 這裡的步長是「自適應」的：lr / (sqrt(v) + epsilon)
        # 震盪大的方向 v 大 -> 步長變小；平緩的方向 v 小 -> 步長變大
        p = p - lr * m_hat / (np.sqrt(v_hat) + epsilon)

    print('Final: {:05d}:f(p)={:.3f} p={} gp={} glen={:.5f}'.format(t, fp, str(p), str(gp), glen))
    return p

# --- 測試部分 ---

# 測試函數 f(x, y) = x² + y²
def f(p):
    x, y = p
    return x**2 + y**2

# 初始點 p0
p0 = np.array([3.0, 4.0])

print("--- Start Adam Optimization ---")
# 呼叫 Adam
# 注意：lr 設為 0.1 對 Adam 來說通常很大，但在簡單函數 ok。實務上 Adam 常用 0.001
result = adam_optimizer(f, p0, lr=0.1, dump_period=10)
print("Minimum point:", result)