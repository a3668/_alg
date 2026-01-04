<!-- ![mc](/pic/hw10/mc.png) -->
# 用蒙地卡羅積分   
## [mc_n.py](/hw10/10.2/mc_n.py)  
[對話](https://chatgpt.com/share/69528989-5010-8006-8271-16fec0ce4574)  
[蒙地卡羅](https://zh.wikipedia.org/zh-tw/蒙地卡羅積分)  

### def mcInt_nD(f, bounds, n=100000)

回傳 f 的 n 維定積分近似值

- dim = len(bounds)
  先計算維度
- value = random.uniform(low, high)
  取該維度的隨機點

- point.append(value)
  將 value 放進 point 這個[]

- f(\*point)
  函數在該抽樣座標上的函數值

- volume \*= length
  要算 n 維積分的體積，就要把每一維的範圍長度相乘
- average = total / n
  積分區域的平均高度估計

---  

# 用黎曼幾分 (n 維) 
## [rm_n.py](/hw10/10.1/rm_n.py)

- def rm_n_loop(f, ranges, step)
  函數 f 在指定 n 維區間上的積分近似值

##### rm_n_loop 的第一部分：建立每個維度的取樣點

```
  axes = []
  for r in ranges:
      start = r[0]
      end = r[1]
      axis_points = np.arange(start, end, step)
      axes.append(axis_points)
  total = 0.0
  cell_volume = step ** len(axes)
```

axes 代表的是每個維度的座標點列表
cell_volume 代表的是 n 維體積
cell_volume = step \*\* len(axes)
因為每一維的邊長都是 step，所以體積是 step 的維度次方

###### rm_n_loop 的第二部分：展開所有多維座標並做 Riemann 累積

```
  for point in product(*axes):
    total += f(*point) * cell_volume
```

product(\*axes)展開多維座標
f(\*point)得到該 point 在函數上的值
最後 total 把所有小區塊的積分加起來  
[對話](https://chatgpt.com/share/695391b8-0c30-8006-9321-d5d7b2e35500)
