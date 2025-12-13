import random

def greedyHillClimbing(f, x, h=0.1, n=20):
    while True:
        fnow = f(x)
        print('x={0:.5f} f(x)={1:.5f}'.format(x, fnow))

        # 產生 n 個鄰居
        neighbors = [x + random.uniform(-h, h) for _ in range(n)]

        # 找出函數值最高的鄰居
        best = max(neighbors, key=f) #比較每個nei帶進f(nei),result最大的nei給best
        fbest = f(best)# nei中帶入f最大的

        # 如果找到比現在高的就移動過去
        if fbest > fnow:
            x = best
        else:
            break  # 沒有更高的就停止

    return x

def f(x):
    return -1*(x*x - 2*x + 1) 
    # = −(x−1)²，最大值在 x=1，f(x)=0

greedyHillClimbing(f, 0)
