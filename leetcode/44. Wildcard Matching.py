from functools import lru_cache

class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    np = len(p)
    ns = len(s)
    @lru_cache(None)
    def dfs(si: int, sp: int, star: bool) -> bool:
      if sp >= np:
        return star or si >= ns
      elif si >= ns:
        n = np - sp
        return p[sp:] == "*" * n
      if p[sp] == "*":
        return dfs(si, sp + 1, True)
      elif p[sp] == "?":
        return dfs(si + 1, sp + 1, star)
      else:
        add = 0
        while sp + add + 1 < np and p[sp + add + 1] != "*" and p[sp + add + 1] != "?":
          add += 1
        if not star:
          if s[si:si + add + 1] != p[sp:sp + add + 1]:
            return False
          else:
            return dfs(si + add + 1, sp + add + 1, False)
        else:
          result = False
          i = si
          while i + add < ns:
            if s[i:i + add + 1] == p[sp:sp + add + 1]:
              result = result or dfs(i + add + 1, sp + add + 1, False)
              if result:
                return result
            i += 1
          return result
    return dfs(0, 0, False)


# my test case:
# s = "abcdabcdefg"
# p1 = "*b*?c*"
# p2 = "*b??e*"