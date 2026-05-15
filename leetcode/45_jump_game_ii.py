class Solution(object):
  def jump(self, nums):
    n = len(nums)
    i = 0
    jump_count = 0
    if n == 1:
      return jump_count
    current_end = 0
    max_reach = 0

    for i, v in enumerate(nums):
      max_reach = max(max_reach, i + v)
      if max_reach >= n - 1:
        jump_count += 1
        return jump_count
      if i == current_end:
        jump_count += 1
        current_end = max_reach
    return jump_count
