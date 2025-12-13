import itertools

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
n = 3  # 範例長度
target = input("target: ")

for tup in itertools.product(charset, repeat=n):
    candidate = ''.join(tup)
    if candidate == target:
        print("找到:", candidate)
        break
else:
    print("未找到")
