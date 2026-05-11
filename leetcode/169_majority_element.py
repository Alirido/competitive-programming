class Solution(object):
  def majorityElement(self, nums):
    counter = {}
    n = len(nums)
    result = 0
    for v in nums:
      if v in counter:
        counter[v] += 1
      else:
        counter[v] = 1
      if counter[v] > n // 2:
        result = v
        break

    return result
        
class Solution(object): # Boyer-Moore Voting Algorithm
  def majorityElement(self, nums):
    candidate = 0
    count = 0
    for v in nums:
      if count == 0:
        candidate = v
      if v == candidate:
        count += 1
      else:
        count -= 1
    return candidate
