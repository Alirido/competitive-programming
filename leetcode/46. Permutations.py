from typing import List

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)
    def dfs(cur: List[int], numList: List[int]):
      if len(cur) == n:
        result.append(cur)
        return
      for i in range(len(numList)):
        dfs(cur[:] + [numList[i]], numList[:i] + numList[i + 1:])
      
    dfs([], nums[:])
    return result

class Solution: # backtrack using in-place swaps (avoids the slicing/copying overhead)
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(start: int):
            if start == n:
                result.append(nums[:])
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # undo swap

        backtrack(0)
        return result

