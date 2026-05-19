class Solution(object):
  def threeSum(self, nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
      # Skip duplicate first elements
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      # Early termination: all remaining are positive → impossible to sum to 0
      if nums[i] > 0:
        break

      left, right = i + 1, n - 1
      target = -nums[i]

      while left < right:
        total = nums[left] + nums[right]

        if total == target:
          result.append([nums[i], nums[left], nums[right]])
          # Skip duplicates on both sides
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1
          left += 1
          right -= 1
        elif total < target:
          left += 1
        else:
          right -= 1

    return result
