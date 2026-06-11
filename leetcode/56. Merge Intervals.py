from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    start = intervals[0][0]
    end = intervals[0][1]
    result = []
    for v in intervals[1:]:
      if v[0] > end:
        result.append([start, end])
        start = v[0]
        end = v[1]
      elif v[1] > end:
        end = v[1]
    result.append([start, end])
    return result
