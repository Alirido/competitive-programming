from typing import List
class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    result = 1
    n = len(points)
    for i, v in enumerate(points):
      if result >= n - i:
        break
      else:
        j = i + 1
        if j == n:
          break
        formula = {}
        while j < n:
          delta_y = points[j][1] - points[i][1]
          delta_x = points[j][0] - points[i][0]
          m = None
          if delta_y == 0:
            m = "delta_y"
          elif delta_x == 0:
            m = "delta_x"
          else:
            m = delta_y / delta_x

          if m not in formula:
            formula[m] = 2
          else:
            formula[m] += 1
          result = max(result, formula[m])
          j += 1
    return result
