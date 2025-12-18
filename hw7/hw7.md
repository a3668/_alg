因為求最少過河次數，所以用 BFS 較好

核心 function

- state = (M, W, S, C)
  每個狀態 = 圖的一個節點。

- def is_legal(state)

  - 判斷狀態是否合法

- def can_take(move, state)

  - 用來判斷這次要過河的對象，是否和 man 在同一邊

- def apply_move(state, move)

  - 計算過河後的狀態

- def neighbors(state)

  - 檢查每一種過河方式，確認現在能不能帶、帶過去之後合不合法
    最後把所有合法的下一步狀態列出來。
    neighbors 把 edge 實作出來

- def solve_puzzle()

  - BFS 從起始狀態搜尋到目標狀態，並回傳一條最短的合法解路徑

- def build_path(start, goal, visited).

  - 還原從起點到終點的路徑

- solution_states = solve_puzzle()
  - 存起點到終點的路徑

[什麼是 BFS](https://zh.wikipedia.org/zh-tw/广度优先搜索)
