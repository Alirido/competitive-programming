class Solution(object):
  def rotate(self, nums, k):
    n = len(nums)
    k = k % n

    def reverse(l, r):
      while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    
    reverse(0, n-1) # first reverse entire array
    reverse(0, k-1) # second reverse the first k elements
    reverse(k, n-1) # thrid reverse the remaining elements
