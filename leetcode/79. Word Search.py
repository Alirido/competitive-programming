from typing import List

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    n, m = len(board), len(board[0])

    def dfs(i: int, j: int, idx: int) -> bool:
      if idx == len(word):
        return True
      if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[idx]:
        return False
      board[i][j] = '#'                      # mark as visited
      found = (dfs(i + 1, j, idx + 1) or dfs(i - 1, j, idx + 1)
               or dfs(i, j + 1, idx + 1) or dfs(i, j - 1, idx + 1))
      board[i][j] = word[idx]                # restore (backtrack)
      return found

    return any(dfs(i, j, 0) for i in range(n) for j in range(m))
