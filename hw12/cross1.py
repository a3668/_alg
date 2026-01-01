import math

#純 Python,math 模組 + for 迴圈,log2 (以 2 為底),Bits (位元)

# --- 1. 函數定義 (保持不變) ---

def log2(x):
    return math.log(max(x, 1e-15), 2)

def cross_entropy(p, q):
    r = 0
    for i in range(len(p)):
        r += p[i] * log2(1 / q[i])
    return r

def entropy(p):
    return cross_entropy(p, p)

# --- 2. 準備數據 ---

p = [0.5, 0.25, 0.25]
q = [1/3, 1/3, 1/3]

print(f"目標 P = {p}")
print(f"初始 Q = {[round(x, 4) for x in q]}")
print(f"P 的 Entropy (理論最小值) = {entropy(p):.5f}")
print("-" * 30)

# --- 3. 優化算法: 指數梯度下降 (Exponentiated Gradient Descent) ---
# 這種方法專門用於「機率分佈」的優化，比加法更穩定

learning_rate = 0.1  # 學習率
iterations = 1000

for k in range(iterations):
    # A. 計算梯度 (Gradient)
    # H(p,q) 對 q_i 的偏微分仍然是 -p[i]/q[i] (忽略常數)
    grad = []
    for i in range(len(q)):
        grad.append(-p[i] / q[i])
    
    # B. 更新 q 值 (使用乘法/指數更新)
    # 核心公式: q_new = q_old * exp(-learning_rate * gradient)
    # 這是資訊幾何中讓機率分佈移動的正確方式
    new_q_unnormalized = []
    for i in range(len(q)):
        # 這裡我們把梯度放在指數上
        factor = math.exp(-learning_rate * grad[i])
        new_q_unnormalized.append(q[i] * factor)
    
    # C. 歸一化 (Normalization)
    # 算出新的總和，然後除以它
    total = sum(new_q_unnormalized)
    q = [x / total for x in new_q_unnormalized]

    if (k+1) % 200 == 0:
        ce = cross_entropy(p, q)
        print(f"Iter {k+1}: CE = {ce:.5f}, Q = {[round(x, 4) for x in q]}")

print("-" * 30)

# --- 4. 驗證結果 ---

print("【最終驗證】")
print(f"優化後的 Q: {[round(x, 4) for x in q]}")
print(f"目標 P    : {p}")
print(f"最終 Cross Entropy: {cross_entropy(p, q):.5f}")
print(f"Entropy(p)        : {entropy(p):.5f}")

# 檢查誤差 (容許一點點浮點數誤差)
diff_q = sum([abs(p[i] - q[i]) for i in range(len(p))])
if diff_q < 1e-3:
    print("\n 驗證成功：Q 收斂至 P")
else:
    print("\n 驗證失敗：Q 未收斂至 P")

diff_ce = abs(cross_entropy(p, q) - entropy(p))
if diff_ce < 1e-4:
    print(" 驗證成功：Cross Entropy 達到最小值 (等於 Entropy)")
else:
    print(" 驗證失敗：Cross Entropy 未達最小值")