from typing import List

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left = 0
    right = n - 1
    idx = None
    while left <= right and idx is None:
      mid = (right + left) // 2
      if target == nums[mid]:
        idx = mid
      elif target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    if idx is None:
      return [-1, -1]
    else:
      # def searchStart(left: int, right: int) -> int:
      #   while left < right and idx is None:
      #     mid = (right + left) // 2
      #     if target == nums[mid]:
      #       idx = mid
      #     elif target < nums[mid]:
      #       right = mid - 1
      #     else:
      #       left = mid + 1

      # start = searchStart(0, idx - 1)
      # end = searchEnd(idx + 1, n - 1)
      n_left = 0
      left = idx - 1
      while left >= 0 and nums[left] == target:
        n_left += 1
        left -= 1
      n_right = 0
      right = idx + 1
      while right < n and nums[right] == target:
        n_right += 1
        right += 1
      return [idx - n_left, idx + n_right]
