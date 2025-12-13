import itertools

n = 3
for r in range(n+1):  # r 表示有幾個位置放 1
    for combo in itertools.combinations(range(n), r):
        row = []
        for i in range(n):
            if i in combo:
                row.append(1)
            else:
                row.append(0)
        print(row)

