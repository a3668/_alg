import random

def f(x):
    return -1 * (x*x - 2*x + 1)  # = -(x-1)^2

def hill_climb_int():
    x = random.randint(-10, 10)  # 隨機起點
    print("起點：x =", x, "f(x) =", f(x))
    
    for step in range(100):
        current = f(x)
        left = f(x - 1)
        right = f(x + 1)

        # 顯示目前狀態
        print(f"Step {step}: x={x}, f(x)={current:.5f}, left={left:.5f}, right={right:.5f}")

        # 看附近誰比較大
        if left > current and left >= right:
            x = x - 1
        elif right > current and right >= left:
            x = x + 1
        else:
            print("停止：左右都不再上升。")
            break

    print("最終結果：x =", x, "f(x) =", f(x))
    return x, f(x)

# 執行
hill_climb_int()
