from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    checker = {}
    grouped = {}
    idx = 0
    for s in strs:
      cs = tuple(sorted(s))
      if cs not in checker:
        checker[cs] = idx
        idx += 1
      if checker[cs] in grouped:
        grouped[checker[cs]].append(s)
      else:
        grouped[checker[cs]] = [s]
    result = []
    for _, v in grouped.items():
      result.append(v)
    return result