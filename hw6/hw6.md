### 爬山

<!--
###### climb1

- $f(x) = -1 (x^{2} + 2x + 1)$
  找最大點
  ![圖](/hw6/pic/climb1.png)
  x 從 0 開始，x 每次移動 0.01，帶入函式
  右移動，如果 f(x+dx)大於目前高度 f(x)，x 就往右走
  左移動，如果 f(x-dx)大於目前高度 f(x)，x 就往左走
  都沒大於就 break
-->

##### [hc.py](/hw6/climb/hc.py) : 通用爬山法最佳化器

- neighbor(p, h=0.01)
  對每個維度使用 uniform(-h, h) 產生隨機偏移量
  並將該偏移量加到目前解的對應維度，以產生鄰居解
- def hillClimbing(f, p, h=0.01)
  在迴圈中反覆產生新鄰居，開始局部搜尋
  如果新鄰居的 loss 較小，就移動，失敗次數歸零
  如果沒找到就失敗次數+1,繼續找

###### [climb.py](/hw6/climb/climb.py) : 線性回歸應用

- 定義資料 x,y、模型 predict(a,x)、損失 MSE(a,x,y)，把 loss(p) 丟進 hc.hillClimbing() 去找最佳參數 a=[b,w]，最後畫出原始點與擬合直線。

- def predict(a, xt)
  功能：用目前的參數 a，對單一 x 值算出預測的 y 值
- def MSE(a, x, y)
  功能：用同一組參數 a，對全部 x,y 算總誤差

[MSE](https://zh.wikipedia.org/zh-tw/均方误差)

---

### 梯度

##### [hw6_gd.py](/hw6/gd/hw6_gd.py) : 通用梯度下降優化器模組

- 提供數值微分（central difference）、梯度計算 grad() 與梯度下降主流程 gradientDescendent()

##### [hw6_gdRegression.py](/hw6/gd/hw6_gdRegression.py) : 作為線性回歸的應用端

- def predict(a, xt)
  功能：用目前的參數 a，對單一 x 值算出預測的 y 值
- def MSE(a, x, y)
  功能：用同一組參數 a，對全部 x,y 算總誤差

- 定義資料 x,y、模型 predict(a, x)、損失函數 MSE(a, x, y)，再把 loss(p) 丟給 hw6_gd.gradientDescendent() 去最小化，最後用 matplotlib 畫出資料點與擬合直線。

- 利用[中央差分法](https://adamdjellouli.com/articles/numerical_methods/3_differentiation/central_difference)近似計算函數 f 對第 k 個變數的偏導數

```
def df_central(f, p, k, step=0.01):
    p1 = p.copy()
    p2 = p.copy()
    p1[k] = p[k] + step
    p2[k] = p[k] - step
    return (f(p1) - f(p2)) / (2 * step)
```

![核心公式](/hw6/pic/gd.png)

- 往逆梯度方向移動

```
gstep = np.multiply(gp, -1*lr)
p += gstep
```

[梯度下降法](https://zh.wikipedia.org/zh-tw/梯度下降法)
[MSE](https://zh.wikipedia.org/zh-tw/均方误差)

---

### 貪婪

在[hw6_gd.py](/hw6/gd/hw6_gd.py)基礎上加入「學習率的階段式收斂策略（指數衰減）」，使前期更新較大、後期更新較小。

##### [hw6_greedy.py](/hw6/greedy/hw6_greedy.py) : 通用梯度下降加指數衰減優化器模組

- def predict(a, xt)
  功能：用目前的參數 a，對單一 x 值算出預測的 y 值
- def MSE(a, x, y)
  功能：用同一組參數 a，對全部 x,y 算總誤差

[MSE](https://zh.wikipedia.org/zh-tw/均方误差)

- [指數衰減](https://zh.wikipedia.org/zh-tw/指数衰减)
  學習率初始為 0.1

- 初期：大步探索(快點靠近正確區域)
- 後期：小步精調(避免跨過最小值)

- 指數衰減學習率函數

```
def lr_exp(i, lr0=0.1, gamma=0.999):
    return lr0 * (gamma ** i)
```

- i : 次數
- gamma：衰減率
- gamma 表示每走一步，保留多少比例的學習率
- 每一步，學習率都再乘一次 gamma

- gradientDescendent_exp : 梯度下降主流程
  每次迭代先計算當前梯度 gp = grad(f, p) 與梯度長度 glen
  再計算當前學習率 lr_i = lr_exp(i, lr0, gamma)

用以下更新式更新參數

```
p += -lr_i * gp
```

glen < 1e-5 停止

##### [greedy.py](/hw6/greedy/greedy.py) : 作為線性回歸的應用端

- 定義資料 x, y、線性模型 predict(a, x) 與損失函數 MSE(a, x, y)，並將 loss(p) 傳入 hw6_greedy.gradientDescendent_exp()，使用指數衰減學習率的梯度下降尋找最佳參數。
- 訓練完成後，用學到的參數計算預測值 y_predicted，並用 matplotlib 畫出原始資料點與回歸直線，用來觀察擬合結果。

---

### 改良法

使用 adam 從[hw6_gd.py](/hw6/gd/hw6_gd.py)改良

##### [hw6_improve.py](/hw6/improve/hw6_improve.py) : Adam 梯度下降優化器模組

-

##### [improve.py](/hw6/improve/improve.py) : 使用 Adam 的線性回歸應用端

- def predict(a, xt)
  功能：用目前的參數 a，對單一 x 值算出預測的 y 值
- def MSE(a, x, y)
  功能：用同一組參數 a，對全部 x,y 算總誤差

[MSE](https://zh.wikipedia.org/zh-tw/均方误差)

- Adam = Momentum + RMSProp + Bias Correction
  核心改良點

1. Momentum - 慣性方向：

- 原理： 紀錄過去梯度的加權平均方向。
- 目的： 減少搜尋過程中的震盪，並在坡度平緩處加速前進，有助於通過鞍點，並提升在複雜地形中的收斂穩定性。

2. RMSProp - 自適應步長 ：

- 原理： 根據梯度平方的移動平均，自動縮放每個參數的學習率。
- 目的： 對於坡度劇烈的參數自動「縮小步長」防止暴衝；對於坡度平緩的參數自動「放大步長」加速收斂。

3. Bias Correction - 偏差修正：

- 原理：由於一階與二階動量在初始時刻為零，前幾步的估計會產生偏小的現象，因此 Adam 透過偏差修正使動量估計更接近真實值。
- 目的：提升訓練初期的更新準確度與穩定性。

[adam 參考](https://arxiv.org/pdf/1412.6980)
