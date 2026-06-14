from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    idx = {}
    for i, v in enumerate(nums):
      if v not in idx:
        idx[v] = i
      else:
        if i - idx[v] <= k:
          return True
        else:
          idx[v] = i
    return False