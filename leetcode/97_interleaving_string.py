from functools import lru_cache

class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
      return False

    @lru_cache(maxsize=None) # memoized recursion
    def dfs(i: int, j: int) -> bool:
      if i == len(s1) and j == len(s2):
        return True
      k = i + j   # implied position in s3
      if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j):
        return True
      if j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1):
        return True
      return False

    return dfs(0, 0)
