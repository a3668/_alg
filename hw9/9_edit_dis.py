import json
#a = 'ATGCAATCCC'
#b = 'ATGATCCG'

# b -> a
def editDistance (b, a):
    a_len, b_len = len(a), len(b)
    rows = b_len + 1
    cols = a_len + 1
    m = [0] * (rows)#就像雙重for的i
    for i in range(rows):
        m[i] = [0] * (cols)
        m[i][0] = i

    for j in range(cols):
        m[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            # a,b長度會比m的[i]短
            if b[i - 1] == a[j - 1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(
                    #insert, a要-1去對齊
                    m[i][j-1] + 1,
                    #replace ㄧ樣長
                    m[i-1][j-1] + 1,
                    #delete,b比a長
                    m[i-1][j] + 1
                )
    return {'d': m[b_len][a_len], 'm': m}
            





# ======= 測試 =======
a = 'ATGCAATCCC'
b = 'ATGATCCG'

e = editDistance(b, a)
print(f'editDistance({b},{a}) = {e["d"]}')
print('====m======')
dump(e['m'])
print('===========\n')
align(b, a, e['m'])