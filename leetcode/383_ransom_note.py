class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rnDict = {}
    for v in ransomNote:
      if v not in rnDict:
        rnDict[v] = 1
      else:
        rnDict[v] += 1

    mDict = {}
    for v in magazine:
      if v not in mDict:
        mDict[v] = 1
      else:
        mDict[v] += 1
    
    for k in rnDict:
      if k not in mDict:
        return False
      if mDict[k] < rnDict[k]:
        return False
    
    return True

# Solution using Counter in python
# Note: Counter is a dict subclass that defaults to 0 for missing keys — no .get() needed.  
from collections import Counter

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rn = Counter(ransomNote)
    mag = Counter(magazine)
    for char, count in rn.items():
      if mag[char] < count:
        return False
    return True
