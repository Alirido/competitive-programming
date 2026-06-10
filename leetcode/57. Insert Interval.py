from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
      return [newInterval]
    result = []
    start = None
    inserted = False
    for it in intervals:
      if inserted:
        result.append(it)
        continue

      skip = False
      if start is not None:
        if newInterval[1] < it[0]:
          result.append([start, newInterval[1]])
          inserted = True
        elif newInterval[1] <= it[1]:
          skip = True
          result.append([start, it[1]])
          inserted = True
        else:
          skip = True
      else:
        if newInterval[0] < it[0]:
          start = newInterval[0]
          if newInterval[1] < it[0]:
            result.append([start, newInterval[1]])
            inserted = True
          elif newInterval[1] <= it[1]:
            skip = True
            result.append([start, it[1]])
            inserted = True
          else:
            skip = True
        elif newInterval[0] <= it[1]:
          start = it[0]
          if newInterval[1] <= it[1]:
            inserted = True
          else:
            skip = True

      if skip:
        continue
      else:
        result.append(it)

    if not inserted:
      result.append([start, newInterval[1]]) if start is not None else result.append(newInterval)
    return result
