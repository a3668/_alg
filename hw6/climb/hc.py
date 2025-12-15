import random

# 產生隨機鄰居 (隨機往各個維度偏移一點點)
def neighbor(p, h=0.01):
    p1 = [0]*len(p)
    for i in range(len(p)):
        d = random.uniform(-h, h) # d 為左右隨機偏移量
        p1[i] = p[i] + d
    return p1

def hillClimbing(f, p, h=0.001, max_fail=10000):
    failCount = 0                    # 失敗次數歸零
    fnow = f(p)                      # 計算目前的 Loss (誤差)
    
    # 只要失敗次數還沒爆表，就繼續找
    while (failCount < max_fail):       
        p1 = neighbor(p, h)          # 取一個隨機鄰居
        f1 = f(p1)                   # 算鄰居的 Loss
        
        if f1 < fnow:                # ★關鍵修改：如果鄰居的誤差「更小」(更好)
            fnow = f1
            p = p1
            # print('p=', p, 'loss=', fnow) # 註解掉以免輸出太多雜訊
            failCount = 0            # 既然成功移動了，失敗計數器歸零
        else:                        # 若沒有更好
            failCount = failCount + 1#   那就記一次失敗
            
    return p                         # 修改：只傳回最佳參數 p