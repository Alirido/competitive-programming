class Solution(object):
    def longestConsecutive(self, nums): # my solution
        if not nums:
          return 0
        else:
          parsed_nums = sorted(set(nums))
          print(parsed_nums)
          i = 1
          result = 0
          counter = 1
          while i < len(parsed_nums):
              if parsed_nums[i] - parsed_nums[i-1] == 1:
                  counter += 1
              else:
                  result = max(result, counter)
                  counter = 1
              i += 1
          return max(result, counter)
    def longestConsecutive(self, nums): # optimized solution
      if not nums:
        return 0;
      nums = set(nums)
      longest = 0
      for x in nums:
         if x - 1 not in nums:
            counter = 1
            while x + counter in nums:
              counter += 1
            longest = max(longest, counter)
      return longest
