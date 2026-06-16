from typing import List

class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    # NOTE: This is algorithm for calculating the total possibility for this problem
    # k = min(k, n - k)
    # if k == 0:
    #   return [i for i in range(1, n + 1)]
    # up = down = 1
    # for i in range(1, k + 1):
    #   up *= n - i + 1
    #   down *= i
    # return up // down

    result = []
    def dfs(start: int, path: List[int]):
      if len(path) == k:
        result.append(path[:])   # copy
        return
      # prune: not enough numbers left to fill path
      for i in range(start, n - (k - len(path)) + 2):
        path.append(i)
        dfs(i + 1, path)
        path.pop()               # backtrack

    dfs(1, [])
    return result
