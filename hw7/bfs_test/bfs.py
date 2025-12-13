def enqueue(a, o):
    a.append(o)

def dequeue(a):
    return a.pop(0)

g = {
    '1': {'n': ['2', '5'], 'v': 0},
    '2': {'n': ['3', '4'], 'v': 0},
    '3': {'n': ['4', '5', '6'], 'v': 0},
    '4': {'n': ['5', '6'], 'v': 0},
    '5': {'n': ['6'], 'v': 0},
    '6': {'n': [], 'v': 0}
}

def init(g):
    for i in g:
        g[i]['v'] = 0

def bfs(g, q):
    while len(q) > 0:
        node = dequeue(q) #pop(0)
        if g[node]['v'] == 0:
            print(node, '=> ', end='')
            g[node]['v'] = 1

            for n in g[node]['n']:
                if g[n]['v'] == 0:
                    enqueue(q,n)




# 主程式
print('bfs:', end='')
init(g)
queue = ['1']
bfs(g, queue)
print('')