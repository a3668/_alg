# 方法 1
def power2n_1(n):
    return 2**n

# 方法 2：用遞迴
def power2n_2(n):
    if n == 0:
        return 1
    prev = power2n_2(n - 1)
    return prev + prev
    # power2n(n-1)+power2n(n-1)

# 方法3：用遞迴
def power2n_3(n):
    if n == 0:
        return 1
    return 2 * power2n_3(n - 1)
    # 2*power2n_3(n-1)

power2 = [None] * 10000
power2[0] = 1
power2[1] = 2

# 方法 4：用遞迴+查表
def power2n4(n):
    if power2[n] is not None:
        return power2[n]
    power2[n] = power2n4(n - 1) << 1
    return power2[n]
    
n = 10

print("method 1:", power2n_1(n))
print("method 2:", power2n_2(n))
print("method 3:", power2n_3(n))
print("method 4:", power2n4(n))


