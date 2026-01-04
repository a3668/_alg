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

def is_legal(state):
    M, W, S, C = state
    if(W == S) and (M != W):
        return False
    if(S == C) and (M != S):
        return False
    return True

def can_take(move, state):
    man_side = state[idx['M']]
    for ch in move:
        if ch == 'M':
            continue
        if state[idx[ch]] != man_side:
            return False
    return True

def apply_move(state, move):
    lst = list(state)
    for ch in move:
        lst[idx[ch]] = 1 - lst[idx[ch]]
    return tuple(lst)

def neighbors(state):
    out = []
    for mv in moves:
        if not can_take(mv, state):
            continue
        nxt = apply_move(state, mv)
        if is_legal(nxt):
            out.append((nxt, mv))
    return out 

def build_path(start, goal, visited):
    cur = goal
    path = [goal]
    while cur != start:
        prev = visited[cur]
        path.append(prev)
        cur = prev
    path.reverse()
    return path


def solve_puzzle():
    q = deque([start])
    visited = {start: None}
    while q:
        cur = q.popleft()
        if cur == goal:
            return build_path(start, goal, visited)
        for nxt, _ in neighbors(cur):
            if nxt not in visited:
                visited[nxt] = cur
                q.append(nxt)
    return None


solution_states = solve_puzzle()

if solution_states:
    print("Path from 0000 to 1111:")
    for state in solution_states:
        print(''.join(map(str, state)))
else:
    print("No solution found.")