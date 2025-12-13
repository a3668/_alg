import itertools

def truth_table_product(n):
    return list(itertools.product([0, 1], repeat=n))


# 範例：3 個變數
for row in truth_table_product(3):
    print(row)



"""import itertools

# 先問 n
n = int(input("請輸入變數個數 n: "))

# 算出所有 0/1 組合
rows = list(itertools.product([0, 1], repeat=n))

# 輸出
for row in rows:
    print(row)
"""