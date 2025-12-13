import json

def editDistance(a, b):
    alen, blen = len(a), len(b)
    if alen == 0: 
        return blen
    if blen == 0: 
        return alen

    # 建立二維矩陣 m，尺寸為 (alen+1) × (blen+1)
    m = [[0] * (blen + 1) for _ in range(alen + 1)]

    # 初始化第一列與第一行
    for i in range(alen + 1):
        m[i][0] = i
    for j in range(blen + 1):
        m[0][j] = j

    # 填表
    for i in range(1, alen + 1):
        for j in range(1, blen + 1):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(
                    m[i-1][j-1] + 1,  # 替換
                    m[i][j-1] + 1,    # 插入 b[j-1]
                    m[i-1][j] + 1     # 刪除 a[i-1]
                )
    return {'d': m[alen][blen], 'm': m}


def align(a, b, m):
    i, j = len(a), len(b)
    ax, bx = '', ''
    while i > 0 and j > 0:
        if m[i][j] == m[i-1][j] + 1:
            # 刪除 a[i-1]
            i -= 1
            ax = a[i] + ax
            bx = ' ' + bx
        elif m[i][j] == m[i][j-1] + 1:
            # 插入 b[j-1]
            j -= 1
            ax = ' ' + ax
            bx = b[j] + bx
        else:
            # 相同或替換
            i -= 1
            j -= 1
            ax = a[i] + ax
            bx = b[j] + bx

    while i > 0:
        i -= 1
        ax = a[i] + ax
        bx = ' ' + bx

    while j > 0:
        j -= 1
        bx = b[j] + bx
        ax = ' ' + ax

    print('ax =', ax)
    print('bx =', bx)


def dump(m):
    for row in m:
        print(json.dumps(row))


# 範例
a = 'ATGCAATCCC'
b = 'ATGATCCG'
e = editDistance(a, b)
print(f'editDistance({a},{b}) = {e["d"]}')
dump(e['m'])
align(a, b, e['m'])
