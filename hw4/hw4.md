[python 工具](https://docs.python.org/3/library/itertools.html)

[itertools 聊天連結](https://chatgpt.com/share/68da48d6-3168-8006-ab4e-7b2607989eaa)

---

# 1 Truth_combinations.py

不重複，沒順序
itertools.combinations(iterable, r)
會從給定的 iterable（這裡是 range(n)，也就是 [0, 1, 2]）裡，取出所有「長度為 r 的組合」。
r = 2
combo =
(0, 1) 0 和 1 位置放 1
(0, 2)
(1, 2)

## 1. `product([0, 1], repeat=n)`

- 代碼[Truth_product.py](/hw4/Truth_product.py)
- **數學概念**：笛卡爾積（Cartesian Product）
- **順序**：有
- **重複**：允許
- **結果數量**：2ⁿ（每個變數只有 0 / 1 兩種可能）
- **結果**（n = 3）：

  ```
  (0, 0, 0)
  (0, 0, 1)
  (0, 1, 0)
  (0, 1, 1)
  (1, 0, 0)
  (1, 0, 1)
  (1, 1, 0)
  (1, 1, 1)
  ```

  像 n 層巢狀迴圈，每一層都跑 `[0, 1]`，用來列出 n 個布林變數的所有組合（真值表）。

---

## 2. `permutations('ABCD', 2)`

- 代碼[permutations_ex.py](/hw4/permutations_ex.py)
- **數學概念**：排列
- **順序**：有
- **重複**：不允許（元素用過一次就不能再用）
- **結果數量**：nPr（這裡 4P2 = 12 個）
- **結果**：
  ```
  ('A', 'B')
  ('A', 'C')
  ('A', 'D')
  ('B', 'A')
  ('B', 'C')
  ('B', 'D')
  ('C', 'A')
  ('C', 'B')
  ('C', 'D')
  ('D', 'A')
  ('D', 'B')
  ('D', 'C')
  ```
  適合情境：位置不同算不一樣（例如先後順序、角色分配、座位安排）

---

## 3. `combinations('ABCD', 2)`

- **數學概念**：組合
- **順序**：無（AB 和 BA 視為同一個組合）
- **重複**：不允許
- **結果數量**：nCr（這裡 4C2 = 6 個）
- **例子**：`AB, AC, AD, BC, BD, CD`
  適合「只在乎選到哪些，不在乎順序」的情境。

---

## 4. `combinations_with_replacement('ABCD', 2)`

- **數學概念**：可重複組合
- **順序**：無（AB = BA）
- **重複**：允許
- **結果數量**：C(n+r-1, r)（這裡 C(4+2-1, 2) = C(5, 2) = 10）
- **例子**：`AA, AB, AC, ..., DD`
  像「抽籤可以放回去」，允許同一元素被選多次。

---

### 總結對照表

## ![對照表](/pic/hw4/對照表.png)

這張表其實就是把 **`itertools` 四種常見組合工具**放在一起比較。它們的差異主要在於 **是否考慮順序**、**是否允許重複**：

combinations 是「選哪幾個位置放 1」
product 是「每個位置都自己決定要 0 還是 1」
