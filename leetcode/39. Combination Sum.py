from typing import List

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n = len(candidates)
    result = []
    combination = []
    def dfs(remaining: int, idx: int):
      if remaining == 0:
        result.append(combination[:])
        return
      for i in range(idx, n):
        if candidates[i] > remaining:
          break
        combination.append(candidates[i])
        dfs(remaining - candidates[i], i)
        combination.pop()
      
    dfs(target, 0)
    return result
