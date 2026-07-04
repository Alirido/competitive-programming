from typing import List
from collections import Counter

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    nc = Counter(nums)
    for k, v in nc.items():
      if v == 1:
        return k