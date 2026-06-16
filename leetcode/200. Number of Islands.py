from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    result = 0
    m = len(grid)
    n = len(grid[0])
    def mark(i: int, j: int):
      if i < 0 or i >= m or j < 0 or j >= n:
        return
      if grid[i][j] == "1":
        grid[i][j] = "#"
      else:
        return
      mark(i - 1, j) # travel up
      mark(i + 1, j) # travel down
      mark(i, j - 1) # travel left
      mark(i, j + 1) # travel right
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1":
          result += 1
          mark(i, j)
    return result

  def numIslands(self, grid): # optimalize solution
      result = 0
      m, n = len(grid), len(grid[0])

      def mark(start_i, start_j):
          stack = [(start_i, start_j)]
          grid[start_i][start_j] = "#"
          while stack:
              i, j = stack.pop()
              for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                  if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                      grid[ni][nj] = "#"
                      stack.append((ni, nj))

      for i in range(m):
          for j in range(n):
              if grid[i][j] == "1":
                  result += 1
                  mark(i, j)
      return result