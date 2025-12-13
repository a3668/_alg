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
    if (W == S) and (M != W):
        return False
    if (S == C) and (M != S):
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

def dfs(state, goal, visited, path):
    if state == goal:
        return path + [goal]
    visited.add(state)
    for next_state, _ in neighbors(state):
        if next_state not in visited:
            result = dfs(next_state, goal, visited, path + [next_state])
            if result is not None:
                return result
    return None

def solve_river_puzzle_dfs():
    visited = set()
    return dfs(start, goal, visited, [start])

solution_states = solve_river_puzzle_dfs()

if solution_states:
    print("Path from 0000 to 1111 (DFS):")
    for state in solution_states:
        print(''.join(map(str, state)))
else:
    print("No solution found.")
