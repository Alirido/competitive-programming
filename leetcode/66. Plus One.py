from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)
    result = digits[::-1]
    rest = 0
    result[0] += 1
    if result[0] == 10:
      rest = 1
      result[0] = 0
    if rest == 0:
      return result[::-1]
    i = 1
    while rest == 1 and i < n:
      result[i] += rest
      if result[i] == 10:
        rest = 1
        result[i] = 0
      else:
        rest = 0
      i += 1
    if rest == 1:
      result.append(1)
    return result[::-1]