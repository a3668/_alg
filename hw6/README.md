### climb

###### climb1

- $f(x) = -1 (x^{2} + 2x + 1)$
  找最大點
  ![圖](/hw6/pic/climb1.png)
  x 從 0 開始，x 每次移動 0.01，帶入函式
  右移動，如果 f(x+dx)大於目前高度 f(x)，x 就往右走
  左移動，如果 f(x-dx)大於目前高度 f(x)，x 就往左走
  都沒大於就 break

###### climb3

n 維

- neighbor(p, h=0.01)
  對每個維度使用 uniform(-h, h) 產生隨機偏移量
  並將該偏移量加到目前解的對應維度，以產生鄰居解
- def hillClimbing(f, p, h=0.01)
  在迴圈中反覆產生新鄰居，開始局部搜尋
  如果新鄰居的高度比較高，就移動，失敗次數歸零
  如果沒找到就失敗次數+1,繼續找

---

### 梯度

- 利用[中央差分法](https://adamdjellouli.com/articles/numerical_methods/3_differentiation/central_difference)近似計算函數 f 對第 k 個變數的偏導數

```
def df_central(f, p, k, step=0.01):
    p1 = p.copy()
    p2 = p.copy()
    p1[k] = p[k] + step
    p2[k] = p[k] - step
    return (f(p1) - f(p2)) / (2 * step)
```

-

![核心公式](/hw6/pic/gd.png)

- 往逆梯度方向移動

```
gstep = np.multiply(gp, -1*lr)
p += gstep
```

[梯度下降法](https://zh.wikipedia.org/zh-tw/梯度下降法)

---

### 貪婪

在[hw6_gd.py](/hw6/gd/hw6_gd.py)的基礎上增加階段性貪婪去調整學習率
[指數衰減](https://zh.wikipedia.org/zh-tw/指数衰减)
學習率初始為 0.1

- 初期：大步探索(快點靠近正確區域)
- 後期：小步精調(避免跨過最小值)

- 指數衰減學習率函數

```
def lr_exp(i, lr0=0.1, gamma=0.999):
    return lr0 * (gamma ** i)
```

i : 次數
gamma：衰減率
gamma 表示每走一步，保留多少比例的學習率
每一步，學習率都再乘一次 gamma
