from typing import Optional, List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    def compare(a: str, b: str) -> str:
      i = 0
      n = min(len(a), len(b))
      while i < n and a[i] == b[i]:
        i += 1
      return a[:i]
    longest = strs[0]
    for i in range(1, len(strs)):
      longest = compare(longest, strs[i])
      if longest == "":
        break
    return longest
