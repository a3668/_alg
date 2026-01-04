import itertools

def truth_table_product(n):
    return list(itertools.product([0, 1], repeat=n))


# 範例：3 個變數
for row in truth_table_product(3):
    print(row)


