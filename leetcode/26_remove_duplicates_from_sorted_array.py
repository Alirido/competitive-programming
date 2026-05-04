class Solution(object):
  def removeDuplicates(self, nums):
    if not nums:
      return 0
    
    k = 1
    for i in range(0, len(nums) - 1):
      if nums[i] != nums[i+1]:
        nums[k] = nums[i+1]
        k += 1
    
    return k
