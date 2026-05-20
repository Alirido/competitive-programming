class Solution(object):
  def minSubArrayLen(self, target, nums):
    i = j = 0
    current = 0
    result = 0
    while i <= j and j < len(nums):
      current += nums[j]
      if current >= target:
        if result == 0:
          result = j - i + 1
        else:
          result = min(result, j - i + 1)
        if current == target:
          j += 1
        else:
          current -= nums[i] + nums[j]
          i += 1
      else:
        j += 1
    
    return result

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2