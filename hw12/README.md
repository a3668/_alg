[exp](https://en.wikipedia.org/wiki/Multiplicative_weight_update_method)
[mirror](https://en.wikipedia.org/wiki/Mirror_descent)

grad = - p / q
![partial_derivati](/pic/hw12/partial_derivative.png)

### 使用指數梯度下降（Exponentiated Gradient / 一種 Mirror Descent）更新 q ，驗證 cross_entropy(p, q) 的最低點是 q=p

1. 定義函數
   - log2(x)：以 2 為底的 log
   - cross_entropy(p, q)：計算交叉熵
   - entropy(p)：計算 p 自己的熵（理論最小值）
2. 設定資料
   - p：目標機率分佈
   - q：初始機率分佈（平均值）
3. 執行多次迭代更新 q

   1. grad.append(-p[i] / q[i])
      為了最小化交叉熵，對 H(p,q) 對 q_i 求偏導得到梯度 grad[i] = -p[i]/q[i]。
      ![partial_derivati](/pic/hw12/partial_derivative.png)
   2. 乘上指數做更新（不調整總和）
      - factor = math.exp(-learning_rate \* grad[i])
      - new_q_unnormalized.append(q[i] \* factor)
        ![multiplicative weight update method](/pic/hw12/exp.png)
   3. 歸一化，把總和調回 1
      - total = sum(new_q)
        算總和
      - q[i] = new_q[i] / total
        每個 x 除以這個總和
        ![mirror descent](/pic/hw12/mirror.png)
