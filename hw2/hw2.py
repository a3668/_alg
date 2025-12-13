# 方法 1
def power2n(n):
    return 2**n

# 方法 2：用遞迴
def power2n(n):
    if n == 0:
        return 1
    return power2n(n -1) + power2n(n - 1)
    # power2n(n-1)+power2n(n-1)

# 方法3：用遞迴
def power2n(n):
    if n == 0:
        return 1
    return 2 * power2n(n - 1)
    # 2*power2n(n-1)

power2 = [None] * 10000
power2[0] = 1
power2[1] = 2

# 方法 4：用遞迴+查表
def power2n4(n):
    if power2[n] is not None:
        return power2[n]
    power2[n] = power2n4(n - 1) << 1
    return power2[n]
    
print(power2n4(10))




