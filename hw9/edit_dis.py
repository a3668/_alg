import json

# b -> a
def editDistance (b, a):
    a_len, b_len = len(a), len(b)
    if a_len == 0:
        return b_len
    if b_len == 0:
        return a_len

    m = [0] * (b_len + 1)
    for i in range(b_len + 1):
        m[i] = [0] * (a_len + 1)
        m[i][0] = i

    for j in range(a_len + 1):
        m[0][j] = j

    for i in range(1, b_len + 1):
        for j in range(1, a_len + 1):
            if b[i-1] == a[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(
                    m[i-1][j-1] + 1,  # replace
                    m[i][j-1] + 1,    # insert
                    m[i-1][j] + 1     # delete
                )
    return {'d': m[b_len][a_len], 'm': m}


# === 最正確 backtracking align() ===
def align(b, a, m):
    i, j = len(b), len(a)
    bx, ax = "", ""

    while i > 0 and j > 0:
        # match
        if b[i-1] == a[j-1] and m[i][j] == m[i-1][j-1]:
            i -= 1
            j -= 1
            bx = b[i] + bx
            ax = a[j] + ax

        # replace
        elif b[i-1] != a[j-1] and m[i][j] == m[i-1][j-1] + 1:
            i -= 1
            j -= 1
            bx = b[i] + bx
            ax = a[j] + ax

        # delete from b (move up)
        elif m[i][j] == m[i-1][j] + 1:
            i -= 1
            bx = b[i] + bx
            ax = " " + ax

        # insert from a (move left)
        elif m[i][j] == m[i][j-1] + 1:
            j -= 1
            bx = " " + bx
            ax = a[j] + ax

        else:
            raise ValueError("Backtrack error at i={}, j={}".format(i, j))

    while i > 0:
        i -= 1
        bx = b[i] + bx
        ax = " " + ax

    while j > 0:
        j -= 1
        bx = " " + bx
        ax = a[j] + ax

    print("bx=", bx)
    print("ax=", ax)


def dump(m):
    for row in m:
        print(json.dumps(row))


# ======= 測試 =======
a = 'ATGCAATCCC'
b = 'ATGATCCG'

e = editDistance(b, a)
print(f'editDistance({b},{a}) = {e["d"]}')
print('====m======')
dump(e['m'])
print('===========\n')
align(b, a, e['m'])