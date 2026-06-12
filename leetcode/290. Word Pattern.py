class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split(" ")
    map = {}
    claimed = set()
    n = len(pattern)
    if len(words) != n:
      return False
    for i in range(n):
      if pattern[i] not in map:
        if words[i] in claimed:
          return False
        map[pattern[i]] = words[i]
        claimed.add(words[i])
      if words[i] != map[pattern[i]]:
        return False
    return True
