from typing import List

class Solution: # my own solution
  def solve(self, board: List[List[str]]) -> None:
    i = 0
    n = len(board)
    m = len(board[i])
    visited = set()
    oList = set()
          
    def bfs(a: int, b: int) -> bool:
      if a < 0 or a >= n or b < 0 or b >= m:
        return False
      if (a, b) in visited:
        return True
      visited.add((a, b))
      if board[a][b] == "X":
        return True
      oList.add((a, b))
      # travel
      left = bfs(a, b - 1)
      right = bfs(a, b + 1)
      up = bfs(a + 1, b)
      down = bfs(a - 1, b)

      return left and right and up and down
      
    while i < n:
      j = 0
      while j < m:
        if (i, j) in visited:
          j += 1
          continue
        if board[i][j] == "O":
          surrounded = bfs(i, j)
          if surrounded:
            while oList:
              x, y = oList.pop()
              board[x][y] = "X"
          else:
            oList.clear
        j += 1
      i += 1

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    if not board or not board[0]:
      return

    n, m = len(board), len(board[0])

    def dfs(i: int, j: int) -> None:
      if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O':
        return
      board[i][j] = '#'
      dfs(i + 1, j)
      dfs(i - 1, j)
      dfs(i, j + 1)
      dfs(i, j - 1)

    # 1. Flood-fill from every border 'O'
    for i in range(n):
      dfs(i, 0)
      dfs(i, m - 1)
    for j in range(m):
      dfs(0, j)
      dfs(n - 1, j)

    # 2. Flip: 'O' (interior) → 'X', '#' (border-connected) → 'O'
    for i in range(n):
      for j in range(m):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == '#':
          board[i][j] = 'O'
