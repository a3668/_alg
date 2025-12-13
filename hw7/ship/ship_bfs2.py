from collections import deque


idx = {'M': 0, 'W': 1, 'S': 2, 'C': 3}
moves = [
    ('M',),
    ('M', 'W'),
    ('M', 'S'),
    ('M', 'C'),
]

start = (0, 0, 0, 0)
goal  = (1, 1, 1, 1)

def is_safe(state):
    M, W, S, C = state
    if(W == S) and (M != W):
        return False
    if(S == C) and (M != S):
        return False
    return True

def can_take(state, move):
    M_side = state[idx['M']]
    for x in move:
        if x == 'M':
            continue
        if state[idx[x]] != M_side:
            return False
    return True

def get_next_states(state):
    next_states = []
    for move in moves:
        if not can_take(state,move):
            continue

        new_states = list(state)
        for x in move:
            new_states[idx[x]] = 1 - new_states[idx[x]] #0,0,0,0 -> 1,0,1,0
        new_states = tuple(new_states)

        if is_safe(new_states):
            next_states.append(new_states)
    return next_states

def bfs_path():
    q = deque([(start, [])])
    seen = {start}
    while q:
        state, path = q.popleft()
        if state == goal:
            return path + [state]
        for ns in get_next_states(state):
            if ns not in seen:
                seen.add(ns)
                q.append((ns, path + [state]))


path = bfs_path() 
for s in path: 
    print(s)


# print(get_next_states((0,0,0,0)))


'''state = (0, 1, 0, 0)  # 農夫左、狼右、羊左、菜左
print(can_take(state, ('M','S')))  # True
print(can_take(state, ('M','W')))  # False
'''











