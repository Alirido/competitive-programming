class Solution(object):
  def removeElement(self, nums, val):
    k = 0

    for value in nums:
      if value != val:
        nums[k] = value
        k += 1

    return k
