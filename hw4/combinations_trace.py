import itertools

n = 3
for r in range(n+1):  # r 表示有幾個位置放 1
    a = itertools.combinations(range(n), r)
    for combo in a:
        row = []
        for i in range(n):
            if i in combo:
                row.append(1)
            else:
                row.append(0)
            #print(row)
        print(row)

