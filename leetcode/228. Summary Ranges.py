from typing import List

class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
      return []
    
    result = []
    start = nums[0]
    for i in range(1, len(nums)):
      if nums[i] - nums[i - 1] != 1:
        str = f"{start}" if start == nums[i - 1] else f"{start}->{nums[i - 1]}"
        result.append(str)
        start = nums[i]
    str = f"{start}" if start == nums[-1] else f"{start}->{nums[-1]}"
    result.append(str)
    return result