def editDistance(b, a):
    """
    計算字串 b 與 a 之間的 Levenshtein Distance（最小編輯距離）

    dp[i][j] 表示：
    將 b 的前 i 個字元轉換成 a 的前 j 個字元所需的最少操作數

    允許的操作：
    1. 刪除（delete）
    2. 插入（insert）
    3. 取代（substitute）
    每個操作成本皆為 1
    """
    len_b = len(b)
    len_a = len(a)

    # 建立 DP 矩陣，大小為 (len_b+1) x (len_a+1)
    dp = []

    for i in range(len_b + 1):
        row = []
        for j in range(len_a + 1):
            row.append(0)
        dp.append(row)

    # 初始化第一col：將 b[:i] 轉成空字串，只能一直刪除
    for i in range(len_b + 1):
        dp[i][0] = i

    # 初始化第一row：將空字串轉成 a[:j]，只能一直插入
    for j in range(len_a + 1):
        dp[0][j] = j

    # 填 DP 表
    for i in range(1, len_b + 1):
        for j in range(1, len_a + 1):
            # 判斷目前字元是否相同
            if b[i - 1] == a[j - 1]:
                cost = 0
            else:
                cost = 1

            # 三種操作的成本
            insert_cost = dp[i][j - 1] + 1
            delete_cost = dp[i - 1][j] + 1
            substitute_cost = dp[i - 1][j - 1] + cost

            # 取最小值
            dp[i][j] = min(delete_cost, insert_cost, substitute_cost)

    return {
        "distance": dp[len_b][len_a],  # 最小編輯距離
        "dp_matrix": dp                # DP 矩陣
    }


def dump(dp_matrix):
    """
    以整齊格式輸出 DP 矩陣
    """
    for row in dp_matrix:
        line = []
        for val in row:
            line.append(f"{val:2d}")
        print(" ".join(line))


def align(b, a, dp_matrix):
    """
    根據 DP 矩陣，回推出其中一組最佳對齊結果
    以 '-' 表示插入或刪除
    """
    i = len(b)
    j = len(a)

    aligned_b = []
    aligned_a = []

    # 從右下角一路回推到左上角
    while i > 0 or j > 0:
        # 嘗試走「對角線」（取代或配對）
        if i > 0 and j > 0:
            if b[i - 1] == a[j - 1]:
                cost = 0
            else:
                cost = 1

            if dp_matrix[i][j] == dp_matrix[i - 1][j - 1] + cost:
                aligned_b.append(b[i - 1])
                aligned_a.append(a[j - 1])
                i -= 1
                j -= 1
                continue

        # 嘗試走「往上」（刪除 b 的字元）
        if i > 0:
            if dp_matrix[i][j] == dp_matrix[i - 1][j] + 1:
                aligned_b.append(b[i - 1])
                aligned_a.append("-")
                i -= 1
                continue

        # 嘗試走「往左」（插入 a 的字元）
        if j > 0:
            if dp_matrix[i][j] == dp_matrix[i][j - 1] + 1:
                aligned_b.append("-")
                aligned_a.append(a[j - 1])
                j -= 1
                continue

        # 理論上不應發生，作為保底處理
        if i > 0 and j > 0:
            aligned_b.append(b[i - 1])
            aligned_a.append(a[j - 1])
            i -= 1
            j -= 1
        elif i > 0:
            aligned_b.append(b[i - 1])
            aligned_a.append("-")
            i -= 1
        else:
            aligned_b.append("-")
            aligned_a.append(a[j - 1])
            j -= 1

    # 因為是從後往前推，需反轉
    aligned_b.reverse()
    aligned_a.reverse()

    # 建立中間對齊標記
    alignment_markers = []
    for char_b, char_a in zip(aligned_b, aligned_a):
        if char_b == char_a:
            alignment_markers.append("|")
        elif char_b == "-" or char_a == "-":
            alignment_markers.append(" ")
        else:
            alignment_markers.append("*")

    # 輸出結果
    print("b:", "".join(aligned_b))
    print("  ", "".join(alignment_markers))
    print("a:", "".join(aligned_a))


# ======= 測試 =======
a = "ATGCAATCCC"
b = "ATGATCCG"

result = editDistance(b, a)

print("editDistance(" + b + ", " + a + ") =", result["distance"])
print("==== DP Matrix ====")
dump(result["dp_matrix"])
print("===================")
align(b, a, result["dp_matrix"])
