class Solution(object):
  def canJump(self, nums):
    n = len(nums)
    max_reach = nums[0]
    for i in range(1, n):
      if i > max_reach:
        return False
      elif max_reach >= n - 1:
        return True
      max_reach = max(max_reach, i + nums[i])
    
    return True # This is because every index was reachable (including the last one), so it's true