def enqueue(a, o):
    a.insert(0, o)

def dequeue(a):
    return a.pop()

g = {  # graph: 被搜尋的網路
    '1': {'n': ['2', '5'], 'v': 0},  # n: neighbor (鄰居), v: visited (是否被訪問過)
    '2': {'n': ['3', '4'], 'v': 0},
    '3': {'n': ['4', '5', '6'], 'v': 0},
    '4': {'n': ['5', '6'], 'v': 0},
    '5': {'n': ['6'], 'v': 0},
    '6': {'n': [], 'v': 0}
}

def init(g):  # 初始化、設定 visited 為 0
    for i in g:
        g[i]['v'] = 0

def bfs(g, q):  # 廣度優先搜尋
    if len(q) == 0:                 # 如果 queue 已空，則返回。
        return
    node = dequeue(q)               # 取出 queue 的第一個節點。
    if g[node]['v'] == 0:           # 如果該節點尚未拜訪過。
        g[node]['v'] = 1            # 標示為已拜訪
    else:                           # 否則 (已訪問過)
        return                      # 不繼續搜尋。
    print(node, '=> ', end='')      # 印出節點
    neighbors = g[node]['n']        # 取出鄰居。
    for n in neighbors:             # 對於每個鄰居
        if not g[n]['v']:           # 若該鄰居還沒被拜訪過
            enqueue(q, n)           # 就放入 queue 中
    bfs(g, q)

# 主程式
print('bfs:', end='')
init(g)
queue = ['1']  # BFS 用的 queue, 起始點為 1。
bfs(g, queue)
print('')
