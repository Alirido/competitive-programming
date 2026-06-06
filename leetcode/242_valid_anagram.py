from collections import Counter

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)
    return s == t
  
  def isAnagram(self, s: str, t: str) -> bool:
    count = {}
    for c in s:
      if c not in count:
        count[c] = 1
      else:
        count[c] += 1
    for c in t:
      if c not in count:
        return False
      else:
        count[c] -= 1
        if count[c] == 0:
          count.pop(c, None)
    
    if not count:
      return True
    else:
      return False
    

  def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
