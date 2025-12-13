https://docs.python.org/3/library/itertools.html

itertools 聊天連結 https://chatgpt.com/share/68da48d6-3168-8006-ab4e-7b2607989eaa

暴力法 https://chatgpt.com/share/68da496b-7194-8006-b646-8a7862467b4e

這張圖其實就是把 **`itertools` 四種常見組合工具**放在一起比較。它們的差異主要在於 **是否考慮順序**、**是否允許重複**：

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

## 1. `product('ABCD', repeat=2)`

- **數學概念**：笛卡爾積
- **順序**：有
- **重複**：允許
- **結果數量**：nʳ（這裡 n=4, r=2 → 16 個）
- **例子**：`AA, AB, ..., DD`
  👉 像雙層迴圈，第一層跑 'ABCD'，第二層也跑 'ABCD'。

---

## 2. `permutations('ABCD', 2)`

- **數學概念**：排列
- **順序**：有
- **重複**：不允許（元素用過一次就不能再用）
- **結果數量**：nPr（這裡 4P2 = 12 個）
- **例子**：`AB, AC, ..., DC`
  👉 適合要考慮「位置不同算不一樣」的情境。

---

## 3. `combinations('ABCD', 2)`

- **數學概念**：組合
- **順序**：無（AB 和 BA 視為同一個組合）
- **重複**：不允許
- **結果數量**：nCr（這裡 4C2 = 6 個）
- **例子**：`AB, AC, AD, BC, BD, CD`
  👉 適合「只在乎選到哪些，不在乎順序」的情境。

---

## 4. `combinations_with_replacement('ABCD', 2)`

- **數學概念**：可重複組合
- **順序**：無（AB = BA）
- **重複**：允許
- **結果數量**：C(n+r-1, r)（這裡 C(4+2-1, 2) = C(5, 2) = 10）
- **例子**：`AA, AB, AC, ..., DD`
  👉 像「抽籤可以放回去」，允許同一元素被選多次。

---

### 總結對照表

| 函數                            | 是否考慮順序 | 是否允許重複 | 數量公式    |
| ------------------------------- | ------------ | ------------ | ----------- |
| `product`                       | ✅ 有        | ✅ 有        | nʳ          |
| `permutations`                  | ✅ 有        | ❌ 無        | nPr         |
| `combinations`                  | ❌ 無        | ❌ 無        | nCr         |
| `combinations_with_replacement` | ❌ 無        | ✅ 有        | C(n+r-1, r) |

---

combinations 是「選哪幾個位置放 1」
product 是「每個位置都自己決定要 0 還是 1」
