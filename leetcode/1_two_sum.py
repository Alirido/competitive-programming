class Solution(object):
  def twoSum(self, nums, target):
    i = 0
    n = len(nums)
    for i in range(n):
      x = target - nums[i]
      if x in nums:
        if x == nums[i]:
          if nums.count(x) == 1:
            continue
          else:
            j = 0
            while j < range(n) and (nums[j] != x or j == i):
              j += 1
            return [i, j]
        else:
          j = 0
          while j < range(n) and (nums[j] != x or j == i):
            j += 1
          return [i, j]
  def twoSum(self, nums, target): # optimized solution
    hashmap = {}

    for i, value in enumerate(nums):
      x = target - value
      if x in hashmap:
        return [i, hashmap[x]]
      hashmap[value] = i
    return []